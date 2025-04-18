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
    all_rules = []
    
    # Get all markdown files in the rules directory
    for rule_file in rules_dir.glob('*.md'):
        with open(rule_file, 'r') as f:
            content = f.read()
            # Extract the title and file path for reference
            title = content.split('\n')[0].replace('#', '').strip()
            all_rules.append({
                'title': title,
                'content': content,
                'file_path': str(rule_file)
            })
    
    return all_rules

def get_pr_diff(github_token, repo_name, pr_number):
    g = Github(github_token)
    repo = g.get_repo(repo_name)
    pr = repo.get_pull(pr_number)
    
    # Get the diff
    diff = pr.get_files()
    
    # Filter for Python files and get their content
    changed_files = []
    for file in diff:
        if file.filename.endswith('.py'):
            # Get the patch content which contains the diff
            patch = file.patch
            # Get the file content
            content = repo.get_contents(file.filename, ref=pr.head.sha).decoded_content.decode()
            changed_files.append({
                'filename': file.filename,
                'content': content,
                'patch': patch
            })
    
    return changed_files

def analyze_code(file_content, patch, rules):
    # Extract changed lines from the patch
    changed_lines = []
    for line in patch.split('\n'):
        if line.startswith('+') and not line.startswith('+++'):
            changed_lines.append(line[1:])  # Remove the '+' prefix
    
    changed_code = '\n'.join(changed_lines)
    
    prompt = f"""
    Please review the following Python code changes against these rules:
    
    {json.dumps([rule['content'] for rule in rules], indent=2)}
    
    Changed code to review:
    {changed_code}
    
    For each line of code that violates any of the rules:
    1. Identify the specific line number
    2. Reference the exact rule that was violated
    3. Provide a specific suggestion for how to fix the code
    4. Include the file path of the rule that was violated
    
    Format your response as a JSON object with the following structure:
    {{
        "violations": [
            {{
                "line_number": <line number>,
                "rule_reference": <rule title>,
                "rule_file": <path to rule file>,
                "suggestion": <suggested code change>,
                "explanation": <brief explanation of the violation>
            }}
        ]
    }}
    """
    
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert Python code reviewer. Provide specific line-by-line feedback with code suggestions."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content

def post_github_comment(github_token, repo_name, pr_number, filename, violations):
    g = Github(github_token)
    repo = g.get_repo(repo_name)
    pr = repo.get_pull(pr_number)
    
    # Create a comment for each violation
    for violation in violations:
        comment = f"""
        ## Rule Violation: {violation['rule_reference']}
        
        **File:** {filename}
        **Line:** {violation['line_number']}
        
        **Violation:** {violation['explanation']}
        
        **Suggestion:**
        ```python
        {violation['suggestion']}
        ```
        
        **Reference:** See [{violation['rule_reference']}]({violation['rule_file']}) for more details.
        """
        
        # Create a review comment on the specific line
        pr.create_review_comment(
            body=comment,
            commit_id=pr.head.sha,
            path=filename,
            line=violation['line_number']
        )

def main():
    load_dotenv()
    
    # Get GitHub context
    github_token = os.getenv('GITHUB_TOKEN')
    repo_name = os.getenv('GITHUB_REPOSITORY')
    pr_number = int(os.getenv('GITHUB_REF').split('/')[-2])
    
    # Load rules and get PR diff
    rules = load_rules()
    changed_files = get_pr_diff(github_token, repo_name, pr_number)
    
    # Analyze each changed file
    for file_info in changed_files:
        analysis = analyze_code(file_info['content'], file_info['patch'], rules)
        violations = json.loads(analysis)['violations']
        
        if violations:
            post_github_comment(github_token, repo_name, pr_number, file_info['filename'], violations)

if __name__ == "__main__":
    main() 