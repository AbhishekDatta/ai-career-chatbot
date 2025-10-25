# Deployment Guide - Hugging Face Spaces

This guide walks you through deploying your AI Career Chatbot to Hugging Face Spaces for free hosting.

## Why Hugging Face Spaces?

- ✅ **Free hosting** for open-source projects
- ✅ **Automatic builds** from your repository
- ✅ **Built-in GPU support** (for paid tiers)
- ✅ **Easy to use** interface
- ✅ **Gradio integration** out of the box

## Prerequisites

- Hugging Face account ([Sign up here](https://huggingface.co/join))
- Your chatbot working locally (see [SETUP.md](SETUP.md))
- OpenAI API key
- (Optional) Pushover credentials

## Step 1: Create a Hugging Face Account

1. Go to [huggingface.co](https://huggingface.co/)
2. Click "Sign Up"
3. Complete the registration process
4. Verify your email

## Step 2: Create a New Space

1. Go to [huggingface.co/spaces](https://huggingface.co/spaces)
2. Click "Create new Space"
3. Fill in the details:
   - **Owner**: Your username
   - **Space name**: `ai-career-chatbot` (or your preferred name)
   - **License**: MIT
   - **Select SDK**: Choose **Gradio**
   - **Hardware**: CPU Basic (free)
   - **Visibility**: Public or Private (your choice)
4. Click "Create Space"

## Step 3: Prepare Your Files

Your Space needs these files:

```
your-space/
├── app.py                 # Main application
├── requirements.txt       # Dependencies
├── README.md             # Space documentation
├── me/
│   ├── linkedin.pdf      # Your LinkedIn profile
│   └── summary.txt       # Your summary
└── .gitignore           # Git ignore rules
```

## Step 4: Set Up Environment Variables

Spaces uses **Secrets** instead of `.env` files.

1. Go to your Space's page
2. Click on **Settings** (gear icon)
3. Scroll to **Repository secrets**
4. Add these secrets:

| Name | Value |
|------|-------|
| `OPENAI_API_KEY` | Your OpenAI API key |
| `PUSHOVER_TOKEN` | Your Pushover app token (optional) |
| `PUSHOVER_USER` | Your Pushover user key (optional) |

**Important**: Make sure the names match exactly!

## Step 5: Upload Files via Web Interface

### Option A: Upload via Web UI

1. Go to **Files** tab in your Space
2. Click **Add file** → **Upload files**
3. Upload your files:
   - `app.py`
   - `requirements.txt`
   - `README.md`
4. Create `me/` directory:
   - Click **Add file** → **Create a new file**
   - Name it `me/linkedin.pdf`
   - Upload your LinkedIn PDF
   - Repeat for `summary.txt`
5. Click **Commit changes to main**

### Option B: Upload via Git (Advanced)

```bash
# Clone your space
git clone https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME
cd YOUR_SPACE_NAME

# Copy your files
cp /path/to/your/project/app.py .
cp /path/to/your/project/requirements.txt .
cp /path/to/your/project/README.md .
mkdir me
cp /path/to/your/project/me/linkedin.pdf me/
cp /path/to/your/project/me/summary.txt me/

# Commit and push
git add .
git commit -m "Initial deployment"
git push
```

## Step 6: Verify requirements.txt

Ensure your `requirements.txt` contains:

```txt
requests
python-dotenv
gradio
pypdf
openai
```

**Note**: Don't include `openai-agents` unless you're specifically using it.

## Step 7: Update app.py for Spaces

Make sure your `app.py` uses environment variables correctly:

```python
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv(override=True)

# OpenAI will automatically use OPENAI_API_KEY from environment
self.openai = OpenAI()
```

Spaces automatically provides environment variables from Secrets.

## Step 8: Wait for Build

After uploading:

1. Space will automatically start building
2. You'll see the build logs in real-time
3. Build typically takes 2-5 minutes
4. Status will show:
   - 🟡 Building...
   - 🟢 Running (success!)
   - 🔴 Build failed (check logs)

## Step 9: Test Your Deployed Chatbot

1. Once status shows **Running**
2. Your Space URL will be: `https://huggingface.co/spaces/YOUR_USERNAME/SPACE_NAME`
3. Test the chatbot with various questions
4. Verify notifications are working (if configured)

## Step 10: Customize Your Space

### Update README.md

Your Space's README appears on the main page. Make it attractive:

```markdown
---
title: AI Career Chatbot - Your Name
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 5.31.0
app_file: app.py
pinned: false
---

# Your Name - AI Career Assistant

Chat with my AI assistant to learn about my professional background!

## Features
- 20+ years of experience in [Your Field]
- Expert in [Your Skills]
- Available 24/7 to answer questions

Try asking:
- "What is your experience?"
- "Tell me about your skills"
- "What are your achievements?"
```

### Add a Thumbnail

1. Create a 1920x1080 image representing your chatbot
2. Name it `thumbnail.jpg` or `thumbnail.png`
3. Upload to your Space's root directory

## Troubleshooting

### Build Failed - Missing Dependencies

**Error**: `ModuleNotFoundError: No module named 'X'`

**Solution**: Add the missing module to `requirements.txt`

### Application Not Starting

**Error**: `Application startup failed`

**Solution**: 
- Check that `app.py` has `if __name__ == "__main__":` block
- Verify the launch command: `gr.ChatInterface(...).launch()`

### API Key Not Working

**Error**: `Incorrect API key provided`

**Solution**:
- Double-check your `OPENAI_API_KEY` in Secrets
- Ensure there are no extra spaces
- Verify the key is active in OpenAI dashboard

### File Not Found - linkedin.pdf

**Error**: `FileNotFoundError: me/linkedin.pdf`

**Solution**:
- Verify the `me/` directory exists
- Check file names match exactly (case-sensitive)
- Ensure files were uploaded to the correct location

### Out of Memory

**Error**: `Container exceeded memory limit`

**Solution**:
- Upgrade to a paid hardware tier
- Optimize your code to use less memory
- Reduce the size of your PDF files

## Updating Your Space

### Via Web Interface

1. Go to **Files** tab
2. Click on the file you want to update
3. Click **Edit** icon
4. Make your changes
5. Click **Commit changes**

### Via Git

```bash
# Make changes to your local files
nano app.py

# Commit and push
git add .
git commit -m "Update chatbot behavior"
git push
```

Space will automatically rebuild.

## Performance Optimization

### Reduce Cold Start Time

Add this to the top of `app.py`:

```python
import os
os.environ["GRADIO_ANALYTICS_ENABLED"] = "False"
```

### Cache Static Content

For faster loads, consider caching:

```python
@functools.lru_cache(maxsize=1)
def load_linkedin():
    reader = PdfReader("me/linkedin.pdf")
    # ... rest of code
```

## Monitoring

### View Logs

1. Go to your Space
2. Click **Logs** tab
3. See real-time application logs
4. Useful for debugging

### Track Usage

Spaces provides basic analytics:
- View count
- Unique visitors
- Active users

## Going Further

### Enable GPU (Paid)

For faster responses:
1. Go to Settings
2. Select **Hardware**
3. Upgrade to GPU tier

### Add Custom Domain

1. Purchase a domain
2. In Settings → **Domains**
3. Add your custom domain
4. Follow DNS configuration instructions

### Enable Gradio Analytics

```python
gr.ChatInterface(me.chat, type="messages", analytics_enabled=True).launch()
```

## Security Best Practices

✅ **DO:**
- Use Secrets for all API keys
- Keep your Space public for portfolio purposes
- Monitor your OpenAI usage

❌ **DON'T:**
- Commit API keys to the repository
- Share your Space's Secret values
- Include sensitive personal information in public Spaces

## Cost Considerations

### Hugging Face

- **CPU Basic**: Free
- **CPU Upgrade**: $0.03/hour
- **T4 Small GPU**: $0.60/hour
- **A100 GPU**: $4.13/hour

### OpenAI API

Monitor your usage:
- Go to [OpenAI Usage Page](https://platform.openai.com/usage)
- Set up billing alerts
- Consider rate limiting in your app

## Support

### Hugging Face Support

- [Documentation](https://huggingface.co/docs/hub/spaces)
- [Community Forum](https://discuss.huggingface.co/)
- [Discord](https://discord.gg/hugging-face)

### Issues with Your Space

1. Check the [troubleshooting section](#troubleshooting) above
2. Review Space logs for errors
3. Open an issue on the GitHub repository
4. Ask in Hugging Face forums

## Success!

Your chatbot is now live and accessible to the world! 🎉

Share your Space URL:
- On LinkedIn
- On your resume
- On your personal website
- In your email signature

Example: `https://huggingface.co/spaces/YOUR_USERNAME/SPACE_NAME`

Happy deploying! 🚀
