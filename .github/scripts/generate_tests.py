#!/usr/bin/env python3
"""
Script to generate test suggestions based on coverage data.
This script reads the coverage data and suggests test files for uncovered lines.
"""

import os
import sys
import json
from pathlib import Path

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

def generate_test_suggestions(uncovered):
    """Generate test suggestions for uncovered lines."""
    suggestions = []
    for file_path, lines in uncovered.items():
        test_file_name = f"test_{Path(file_path).stem}.py"
        suggestions.append(f"# Suggested test file: {test_file_name}")
        suggestions.append(f"# For file: {file_path}")
        suggestions.append(f"# Uncovered lines: {', '.join(map(str, lines))}")
        suggestions.append("")
    return suggestions

def write_suggestions(suggestions):
    """Write test suggestions to a file."""
    with open('test_suggestions.txt', 'w') as f:
        f.write('\n'.join(suggestions))

def main():
    """Main function to generate test suggestions."""
    coverage_data = read_coverage_data()
    uncovered = analyze_uncovered_lines(coverage_data)
    suggestions = generate_test_suggestions(uncovered)
    write_suggestions(suggestions)
    print("Test suggestions generated in test_suggestions.txt")

if __name__ == "__main__":
    main() 