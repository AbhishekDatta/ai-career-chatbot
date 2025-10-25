# Contributing to AI Career Chatbot

First off, thank you for considering contributing to the AI Career Chatbot! It's people like you that make this project better for everyone.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

This project and everyone participating in it is governed by basic principles of respect and professionalism. By participating, you are expected to uphold these standards.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples** to demonstrate the steps
- **Describe the behavior you observed** and what you expected
- **Include screenshots** if applicable
- **Note your environment** (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a detailed description** of the suggested enhancement
- **Explain why this enhancement would be useful**
- **List any potential drawbacks** or challenges

### Pull Requests

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Test your changes thoroughly
5. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
6. Push to the branch (`git push origin feature/AmazingFeature`)
7. Open a Pull Request

## Development Setup

1. **Clone your fork**
   ```bash
   git clone https://github.com/your-username/ai-career-chatbot.git
   cd ai-career-chatbot
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file with your API keys:
   ```
   OPENAI_API_KEY=your_key_here
   PUSHOVER_TOKEN=your_token_here
   PUSHOVER_USER=your_user_key_here
   ```

5. **Create test data**
   ```bash
   mkdir me
   # Add your test linkedin.pdf and summary.txt files
   ```

6. **Run the application**
   ```bash
   python app.py
   ```

## Coding Standards

### Python Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 100 characters
- Use descriptive variable names

### Documentation

- Add docstrings to all functions and classes
- Use Google-style docstrings format:
  ```python
  def function_name(param1, param2):
      """
      Brief description of function.
      
      Args:
          param1 (type): Description of param1
          param2 (type): Description of param2
          
      Returns:
          type: Description of return value
      """
  ```

### Comments

- Write comments for complex logic
- Explain *why*, not *what*
- Keep comments up-to-date with code changes

### Code Organization

- Keep functions focused and single-purpose
- Limit function length (preferably under 50 lines)
- Group related functions together
- Use meaningful names

## Commit Message Guidelines

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, etc.)
- **refactor**: Code refactoring
- **test**: Adding or updating tests
- **chore**: Maintenance tasks

### Examples

```
feat(chat): add multi-language support

Implemented translation capability using Google Translate API.
Users can now chat in Spanish, French, and German.

Closes #42
```

```
fix(notifications): resolve Pushover timeout issue

Added retry logic with exponential backoff to handle
temporary network failures when sending notifications.

Fixes #38
```

## Pull Request Process

1. **Update Documentation**: Update the README.md with details of changes if applicable
2. **Update Dependencies**: Add any new dependencies to requirements.txt
3. **Test Thoroughly**: Ensure all tests pass and add new tests if needed
4. **Code Review**: Wait for at least one maintainer to review your PR
5. **Address Feedback**: Make requested changes promptly
6. **Squash Commits**: Consider squashing commits before merging

### PR Checklist

Before submitting your PR, ensure:

- [ ] Code follows the project's style guidelines
- [ ] Documentation has been updated
- [ ] All tests pass
- [ ] New code has appropriate comments
- [ ] Commit messages follow the guidelines
- [ ] No sensitive information (API keys, passwords) is included

## Testing

### Running Tests

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
pytest

# Run with coverage
pytest --cov=app
```

### Writing Tests

- Write tests for new features
- Maintain or improve code coverage
- Test edge cases and error handling

## Questions?

Feel free to open an issue with the tag `question` if you have any questions about contributing.

## Recognition

Contributors will be recognized in the project README.md. Thank you for your contributions!

---

**Remember**: Every contribution, no matter how small, is valuable and appreciated! 🙏
