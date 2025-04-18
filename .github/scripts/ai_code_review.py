import os
import sys
import glob
import json
from pathlib import Path
from openai import OpenAI
from github import Github
from dotenv import load_dotenv

def load_rules():
    rules_dir = Path('.ai_code_rules')
    rules = []
    for rule_file in rules_dir.glob('*.md'):
        with open(rule_file, 'r') as f:
            rules.append(f.read())
    return '\n\n'.join(rules)

def get_changed_files():
    # Get the list of changed files from GitHub Actions environment
    changed_files = []
    for file in glob.glob('**/*.py', recursive=True):
        if not file.startswith('.github/'):
            changed_files.append(file)
    return changed_files

def generate_prompt(code, rules):
    # Extract categories from rules
    categories = []
    current_category = None
    current_rules = []
    
    for line in rules.split('\n'):
        if line.startswith('## '):
            if current_category:
                categories.append((current_category, current_rules))
            current_category = line[3:].strip()
            current_rules = []
        elif line.startswith('- '):
            current_rules.append(line[2:].strip())
    
    if current_category:
        categories.append((current_category, current_rules))
    
    # Build dynamic prompt
    prompt_parts = [
        "Please review the following Python code against these rules:",
        "",
        rules,
        "",
        "Code to review:",
        code,
        "",
        "Provide a detailed review focusing on:"
    ]
    
    # Add categories as review points
    for i, (category, _) in enumerate(categories, 1):
        prompt_parts.append(f"{i}. {category}")
    
    prompt_parts.extend([
        "",
        "For each category, provide specific examples from the code and suggest improvements where applicable.",
        "Format your response as a GitHub comment with markdown formatting."
    ])
    
    return "\n".join(prompt_parts)

def analyze_code(file_path, rules):
    with open(file_path, 'r') as f:
        code = f.read()
    
    prompt = generate_prompt(code, rules)
    
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert Python code reviewer."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content

def post_github_comment(review, file_path):
    github_token = os.getenv('GITHUB_TOKEN')
    repo_name = os.getenv('GITHUB_REPOSITORY')
    pr_number = int(os.getenv('GITHUB_REF').split('/')[-2])
    
    g = Github(github_token)
    repo = g.get_repo(repo_name)
    pr = repo.get_pull(pr_number)
    
    comment = f"## AI Code Review for {file_path}\n\n{review}"
    pr.create_issue_comment(comment)

def main():
    load_dotenv()
    rules = load_rules()
    changed_files = get_changed_files()
    
    for file_path in changed_files:
        review = analyze_code(file_path, rules)
        post_github_comment(review, file_path)

if __name__ == "__main__":
    main() 