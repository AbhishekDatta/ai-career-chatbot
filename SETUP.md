# Setup Guide - AI Career Chatbot

This guide will walk you through setting up the AI Career Chatbot from scratch.

## Prerequisites

Before you begin, ensure you have:

- **Python 3.8 or higher** installed ([Download Python](https://www.python.org/downloads/))
- **Git** installed ([Download Git](https://git-scm.com/downloads))
- **OpenAI API account** with credits ([Sign up](https://platform.openai.com/signup))
- **Pushover account** (optional, for notifications) ([Sign up](https://pushover.net/))

## Step 1: Check Python Installation

Open your terminal/command prompt and verify Python is installed:

```bash
python --version
# or
python3 --version
```

You should see something like `Python 3.8.x` or higher.

## Step 2: Clone the Repository

```bash
# Clone the repository
git clone https://github.com/AbhishekDatta/ai-career-chatbot.git

# Navigate to the project directory
cd ai-career-chatbot
```

## Step 3: Create Virtual Environment

Creating a virtual environment keeps your project dependencies isolated.

### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` at the beginning of your command prompt.

## Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- `openai` - For GPT-4o-mini API
- `gradio` - For the web interface
- `pypdf` - For PDF processing
- `python-dotenv` - For environment variables
- `requests` - For HTTP requests

## Step 5: Get Your API Keys

### OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign in or create an account
3. Navigate to API Keys section
4. Click "Create new secret key"
5. Copy and save the key (you won't see it again!)

### Pushover API (Optional)

1. Go to [Pushover](https://pushover.net/)
2. Create an account
3. Create a new application/API token
4. Note your User Key from the dashboard
5. Note your Application Token

## Step 6: Configure Environment Variables

Create a `.env` file in the project root directory:

### On macOS/Linux:
```bash
touch .env
```

### On Windows:
```bash
type nul > .env
```

Open `.env` in a text editor and add:

```env
# OpenAI API Configuration
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxx

# Pushover Notification Configuration (optional)
PUSHOVER_TOKEN=your_application_token_here
PUSHOVER_USER=your_user_key_here
```

**Important**: Replace the placeholder values with your actual keys!

## Step 7: Prepare Your Career Data

### Create the data directory:

```bash
mkdir me
```

### Add Your LinkedIn Profile:

1. Go to your LinkedIn profile
2. Click "More" → "Save to PDF"
3. Save the file as `linkedin.pdf`
4. Move it to the `me/` directory

### Create Your Summary File:

Create `me/summary.txt` with your personal information:

```text
Personal:
My name is [Your Name], and I'm a [Your Title/Role].
Originally from [Your Location], I relocated to [Current Location] in [Year].
Beyond my professional work, I'm passionate about [Your Interests].

Career Breaks (if applicable):
1. [Reason] - [Start Date] to [End Date]
    [Brief explanation]
```

## Step 8: Test the Application

Run the application:

```bash
python app.py
```

You should see output like:

```
Running on local URL:  http://127.0.0.1:7860

To create a public link, set `share=True` in `launch()`.
```

Open your browser and go to `http://127.0.0.1:7860`

## Step 9: Test the Chatbot

Try asking some questions:

- "What is your experience?"
- "Tell me about your skills"
- "What technologies do you work with?"

## Troubleshooting

### Issue: "ModuleNotFoundError"

**Solution**: Make sure your virtual environment is activated and dependencies are installed:
```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Issue: "OpenAI API Error"

**Solution**: Check that:
1. Your `OPENAI_API_KEY` in `.env` is correct
2. You have credits in your OpenAI account
3. The `.env` file is in the project root directory

### Issue: "File not found: me/linkedin.pdf"

**Solution**: Ensure:
1. The `me/` directory exists
2. Your PDF is named exactly `linkedin.pdf`
3. The file is in the correct location: `me/linkedin.pdf`

### Issue: Pushover notifications not working

**Solution**: 
1. Check your `PUSHOVER_TOKEN` and `PUSHOVER_USER` in `.env`
2. Verify the Pushover app is installed on your device
3. Note: Pushover is optional - the chatbot will work without it

## Customization

### Change the Name

Edit `app.py` line 80:
```python
self.name = "Your Name"
```

### Modify the Behavior

Edit the `system_prompt()` method in `app.py` to change how the chatbot responds.

### Change the Model

Edit line 119 in `app.py`:
```python
model="gpt-4o-mini"  # Change to "gpt-4o" for more powerful responses
```

Note: Different models have different costs!

## Next Steps

### Deploy to Hugging Face Spaces

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

### Customize the UI

Check Gradio documentation for UI customization options.

### Add New Features

Review the codebase and consider adding:
- More function tools
- Analytics tracking
- Multi-language support
- Voice interface

## Getting Help

If you encounter issues:

1. Check the [Troubleshooting](#troubleshooting) section above
2. Review existing [GitHub Issues](https://github.com/AbhishekDatta/ai-career-chatbot/issues)
3. Create a new issue with:
   - Your Python version
   - Complete error message
   - Steps to reproduce

## Security Notes

⚠️ **Important Security Reminders**:

- Never commit your `.env` file to Git
- Never share your API keys publicly
- Keep your `linkedin.pdf` and `summary.txt` private if they contain sensitive information
- The `.gitignore` file is configured to protect these files

## Success!

If you've made it this far and the chatbot is running, congratulations! 🎉

You now have a working AI-powered career chatbot. Feel free to:
- Customize it for your needs
- Deploy it to the web
- Share it with potential employers
- Contribute improvements back to the project

Happy chatting! 🤖
