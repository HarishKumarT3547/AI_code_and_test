import os
import sys
import ast
import coverage
from pathlib import Path

def get_uncovered_lines():
    cov = coverage.Coverage()
    cov.load()
    return cov.get_data().missing_lines()

def generate_test_file(file_path, uncovered_lines):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Parse the Python file
    tree = ast.parse(content)
    
    # Get the module name
    module_name = Path(file_path).stem
    
    # Generate test file content
    test_content = f"""import pytest
from {module_name} import *

# Tests for uncovered lines
"""
    
    # Add test cases for each uncovered line
    for line in uncovered_lines:
        # Get the line content
        line_content = content.split('\n')[line-1].strip()
        
        # Skip empty lines and comments
        if not line_content or line_content.startswith('#'):
            continue
            
        # Generate test case
        test_content += f"""
def test_line_{line}():
    # Test for line {line}: {line_content}
    # TODO: Implement test case
    pass
"""
    
    # Write test file
    test_file = Path('tests') / f'test_{module_name}.py'
    test_file.parent.mkdir(exist_ok=True)
    
    with open(test_file, 'w') as f:
        f.write(test_content)
    
    return test_content

def main():
    # Get uncovered lines
    uncovered = get_uncovered_lines()
    
    # Generate test files
    test_suggestions = []
    for file_path, lines in uncovered.items():
        if not file_path.endswith('.py'):
            continue
            
        test_content = generate_test_file(file_path, lines)
        test_suggestions.append(f"# Test file for {file_path}\n{test_content}")
    
    # Write suggestions to file
    with open('test_suggestions.txt', 'w') as f:
        f.write('\n\n'.join(test_suggestions))

if __name__ == "__main__":
    main() 