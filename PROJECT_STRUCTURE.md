# Project Structure

This document explains the organization and purpose of each file in the project.

```
ai-career-chatbot/
│
├── app.py                      # Main application file (original)
├── app_documented.py           # Fully documented version with detailed comments
├── requirements.txt            # Python package dependencies
│
├── README.md                   # Main project documentation
├── SETUP.md                    # Detailed setup instructions
├── QUICKSTART.md               # Quick 5-minute setup guide
├── DEPLOYMENT.md               # Deployment guide for Hugging Face Spaces
├── CONTRIBUTING.md             # Contribution guidelines
├── LICENSE                     # MIT License
│
├── .env.example                # Template for environment variables
├── .env                        # Your actual environment variables (not in git)
├── .gitignore                  # Files to ignore in version control
│
├── me/                         # Personal career data directory
│   ├── linkedin.pdf            # LinkedIn profile (PDF export)
│   └── summary.txt             # Personal summary and career breaks
│
├── thumbnail.jpg               # Project thumbnail image
│
└── tests/                      # Unit tests (optional, to be added)
    └── test_app.py             # Test cases for the application
```

## File Descriptions

### Core Application Files

#### `app.py`
- **Purpose**: Main application entry point
- **Contains**: 
  - OpenAI client initialization
  - PDF processing logic
  - Chat interface setup
  - Tool/function calling implementation
- **Key Classes**: `Me` (main chatbot class)
- **Key Functions**: `push()`, `record_user_details()`, `record_unknown_question()`

#### `app_documented.py`
- **Purpose**: Extensively documented version of app.py
- **Use Case**: Learning, understanding the codebase
- **Contains**: Same functionality as app.py with detailed comments
- **Note**: Use this version for development and understanding

#### `requirements.txt`
- **Purpose**: Lists all Python package dependencies
- **Packages**:
  - `openai`: OpenAI API client
  - `gradio`: Web UI framework
  - `pypdf`: PDF text extraction
  - `python-dotenv`: Environment variable management
  - `requests`: HTTP requests for Pushover

### Documentation Files

#### `README.md`
- **Purpose**: Main project documentation
- **Includes**:
  - Project overview and features
  - Technology stack
  - Installation instructions
  - Usage examples
  - Code explanations
  - Deployment guide
  - Contributing guidelines

#### `SETUP.md`
- **Purpose**: Detailed step-by-step setup guide
- **Target Audience**: First-time users, beginners
- **Includes**:
  - Prerequisites checklist
  - Detailed installation steps
  - API key setup
  - Troubleshooting section
  - Customization tips

#### `QUICKSTART.md`
- **Purpose**: Get started in 5 minutes
- **Target Audience**: Experienced developers
- **Includes**:
  - Condensed setup instructions
  - Minimal commands to get running
  - Quick customization tips

#### `DEPLOYMENT.md`
- **Purpose**: Guide for deploying to Hugging Face Spaces
- **Includes**:
  - Step-by-step deployment instructions
  - Environment variable configuration
  - Troubleshooting common issues
  - Performance optimization tips
  - Monitoring and maintenance

#### `CONTRIBUTING.md`
- **Purpose**: Guidelines for contributing to the project
- **Includes**:
  - Code of conduct
  - How to report bugs
  - How to suggest features
  - Pull request process
  - Coding standards
  - Commit message guidelines

#### `LICENSE`
- **Purpose**: Legal license for the project
- **Type**: MIT License
- **Permissions**: Commercial use, modification, distribution, private use

### Configuration Files

#### `.env.example`
- **Purpose**: Template for environment variables
- **Usage**: Copy to `.env` and fill in actual values
- **Contains**: Placeholders for:
  - `OPENAI_API_KEY`
  - `PUSHOVER_TOKEN`
  - `PUSHOVER_USER`

#### `.env` (not in repository)
- **Purpose**: Stores actual sensitive credentials
- **Security**: Never committed to git (in .gitignore)
- **Contains**: Your actual API keys and tokens

#### `.gitignore`
- **Purpose**: Specifies files Git should ignore
- **Ignores**:
  - Python cache files (`__pycache__`)
  - Virtual environments (`venv/`)
  - Environment variables (`.env`)
  - Personal data (`me/linkedin.pdf`, `me/summary.txt`)
  - IDE files (`.vscode/`, `.idea/`)

### Data Directory

#### `me/`
- **Purpose**: Stores personal career information
- **Privacy**: Excluded from git for privacy
- **Required Files**:
  - `linkedin.pdf`: Your LinkedIn profile as PDF
  - `summary.txt`: Personal background and career breaks

#### `me/linkedin.pdf`
- **Purpose**: Source of career information
- **Format**: PDF export from LinkedIn
- **Usage**: Parsed by pypdf in app.py
- **How to Get**: LinkedIn → Profile → More → Save to PDF

#### `me/summary.txt`
- **Purpose**: Additional personal context
- **Format**: Plain text
- **Contains**:
  - Personal background
  - Career breaks and explanations
  - Interests and hobbies

### Media Files

#### `thumbnail.jpg`
- **Purpose**: Visual representation of the project
- **Usage**: GitHub social preview, documentation
- **Dimensions**: Recommended 1920x1080
- **Format**: JPG or PNG

### Testing (Optional)

#### `tests/test_app.py`
- **Purpose**: Unit tests for the application
- **Framework**: pytest (recommended)
- **Tests**:
  - Function calling logic
  - PDF parsing
  - Environment variable loading
  - API interactions (mocked)

## Directory Ownership

```
.
├── Root Directory              # Public, version-controlled
│   ├── app.py                  # Public
│   ├── requirements.txt        # Public
│   └── README.md               # Public
│
├── me/                         # Private, not in version control
│   ├── linkedin.pdf            # Your private data
│   └── summary.txt             # Your private data
│
└── .env                        # Private, not in version control
```

## File Workflow

### Development Workflow
```
1. Clone repository
2. Copy .env.example → .env
3. Fill in API keys in .env
4. Create me/ directory
5. Add linkedin.pdf and summary.txt
6. Run app.py
7. Test functionality
8. Make changes
9. Commit (excluding private files)
```

### Deployment Workflow
```
1. Prepare files (app.py, requirements.txt, README.md)
2. Upload to Hugging Face Space
3. Add linkedin.pdf and summary.txt via web UI
4. Configure Secrets (API keys)
5. Wait for build
6. Test deployed application
```

## Best Practices

### Version Control
- ✅ Commit: Code files, documentation, requirements
- ❌ Don't commit: `.env`, personal data, API keys

### Security
- Store all secrets in `.env` (local) or Secrets (Hugging Face)
- Never hardcode API keys
- Keep personal data in `me/` directory

### Organization
- Keep related files together
- Use clear, descriptive file names
- Document everything
- Separate concerns (config, code, data, docs)

## Adding New Files

When adding new files:

1. **Update .gitignore** if file contains sensitive data
2. **Update README.md** if file affects user workflow
3. **Update this document** to maintain accuracy
4. **Follow naming conventions**: lowercase with hyphens

## Maintaining the Structure

- Keep documentation up-to-date
- Remove unused files
- Organize into subdirectories as project grows
- Use consistent naming conventions

---

This structure provides a clean, organized, and professional project layout that's easy to navigate and maintain.
