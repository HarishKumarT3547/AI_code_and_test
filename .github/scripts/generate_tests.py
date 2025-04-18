#!/usr/bin/env python3
"""
Script to generate test suggestions based on coverage data using OpenAI.
This script reads the coverage data and suggests test files for uncovered lines.
"""

import os
import sys
import json
from openai import OpenAI
from pathlib import Path
from datetime import datetime

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def read_coverage_data():
    """Read the coverage data from the JSON file."""
    try:
        with open('coverage.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except UnicodeDecodeError:
        with open('coverage.json', 'r', encoding='latin-1') as f:
            return json.load(f)

def analyze_uncovered_lines(coverage_data):
    """Analyze coverage data to find uncovered lines."""
    uncovered = {}
    for file_path, file_data in coverage_data.items():
        if not file_path.startswith('tests/'):  # Skip test files
            uncovered_lines = [line for line, covered in file_data.items() if not covered]
            if uncovered_lines:
                uncovered[file_path] = uncovered_lines
    return uncovered

def generate_test_suggestions_with_openai(uncovered):
    """Generate test suggestions for uncovered lines using OpenAI."""
    suggestions = []
    for file_path, lines in uncovered.items():
        test_file_name = f"test_{Path(file_path).stem}.py"
        prompt = f"Generate a test function for the following lines in {file_path}:\nLines: {', '.join(map(str, lines))}\n\nTest function:"
        response = client.completions.create(
            model="text-davinci-003",  # Use the appropriate model
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )
        test_function = response.choices[0].text.strip()
        suggestions.append(f"# Suggested test file: {test_file_name}")
        suggestions.append(f"# For file: {file_path}")
        suggestions.append(f"# Uncovered lines: {', '.join(map(str, lines))}")
        suggestions.append(test_function)
        suggestions.append("")
    return suggestions

def write_suggestions(suggestions):
    """Write test suggestions to a file with the current date and time."""
    # Ensure the recommendation directory exists
    os.makedirs('tests/recommendation', exist_ok=True)
    # Get current date and time
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Create file name with date and time
    file_name = f'test_suggestions_{current_time}.txt'
    with open(f'tests/recommendation/{file_name}', 'w') as f:
        f.write('\n'.join(suggestions))

def main():
    """Main function to generate test suggestions."""
    coverage_data = read_coverage_data()
    uncovered = analyze_uncovered_lines(coverage_data)
    suggestions = generate_test_suggestions_with_openai(uncovered)
    write_suggestions(suggestions)
    print(f"Test suggestions generated in test_suggestions_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt")

if __name__ == "__main__":
    main() 