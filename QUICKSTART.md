# Quick Start Guide

Get your AI Career Chatbot up and running in 5 minutes!

## Prerequisites

- Python 3.8+
- OpenAI API key

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/AbhishekDatta/ai-career-chatbot.git
cd ai-career-chatbot

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY

# 5. Prepare your data
mkdir me
# Add your linkedin.pdf and summary.txt to the me/ directory

# 6. Run the application
python app.py
```

## Open in Browser

Navigate to: `http://127.0.0.1:7860`

## Test Questions

Try asking:
- "What is your experience in DevOps?"
- "Tell me about your leadership skills"
- "What are your key achievements?"

## Customization

1. Edit `app.py` line 80 to change the name
2. Replace `me/linkedin.pdf` with your LinkedIn profile
3. Update `me/summary.txt` with your information

## Deploy

See [DEPLOYMENT.md](DEPLOYMENT.md) for Hugging Face Spaces deployment.

## Need Help?

Check [SETUP.md](SETUP.md) for detailed instructions.

---

That's it! You're ready to go! 🚀
