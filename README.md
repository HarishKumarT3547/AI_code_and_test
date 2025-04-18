# AI Code Review and Test Coverage

This project implements an automated code review and test coverage system using GitHub Actions. It automatically generates test suggestions for uncovered code, performs code reviews, and provides coverage reports on pull requests.

## Features

- Automated code review and test coverage analysis
- OpenAI-powered test suggestion generation
- GitHub Actions workflow for continuous integration
- AI-powered code review and suggestions
- Automated code quality checks
- Coverage reporting on pull requests
- Automatic test file generation for uncovered code


## Prerequisites

- Python 3.10 or higher
- GitHub repository with GitHub Actions enabled
- OpenAI API key (for test suggestion generation and code review)

## Project Structure

```
.
├── .github/
│   ├── workflows/
│   │   ├── test-coverage.yml          # GitHub Actions workflow
|   |   └── ai_code_review.yml         # GitHub Actions workflow
│   ├── scripts/
│   │   ├── generate_tests.py          # Test generation script
│   │   └── ai_code_review.py          # Code review script
│   └── requirements/
│        ├── generate_tests.txt        # Test python dependencies
│        └── ai_code_review.txt        # Code review python dependencies
├── tests/                             # For keeping test files
```

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/AI_code_and_test.git
   cd AI_code_and_test
   ```

2. **Run Code Review and Test**
   - Place new code rule markdown in .ai_code_rules folder in the master and push
   - Create new branch and place a python based code file at the root of the project
   - Push the new file to the repository
   - Now create a pull request between master(base) and new branch

## GitHub Actions Workflow

The project uses GitHub Actions to:

1. Run tests and generate coverage reports
2. Generate test suggestions for uncovered code
3. Perform automated code reviews
4. Create a new branch with test suggestions
5. Comment on pull requests with coverage information and code review feedback

### Workflow Triggers

The workflow runs on:

- Pull requests to `main` or `master` branches
- When Python files are modified
- When test files are modified
- When the test generation requirements are updated

## Code Review Process

The system automatically:

1. Analyzes code changes in pull requests
2. Checks for code quality issues
3. Provides suggestions for improvements
4. Identifies potential bugs and security issues
5. Reviews code style and best practices
6. Generates detailed review comments on pull requests

## Test Generation

The system automatically:

1. Analyzes code coverage
2. Identifies uncovered lines
3. Uses OpenAI to generate test suggestions
4. Creates test files in the `tests/recommendation/` directory

## Contributing

1. Create a new branch for your changes
2. Make your modifications
3. Run tests locally
4. Create a pull request
5. The system will automatically:
   - Run tests and generate coverage reports
   - Perform code review
   - Generate test suggestions if needed
   - Provide feedback on the pull request

## License



## Support

For issues and feature requests, please [create an issue](https://github.com/HarishKumarT3547/AI_code_and_test/issues) in the repository.
