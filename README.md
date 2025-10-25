# AI Career Chatbot - Abhishek Datta's Virtual Assistant

[![Hugging Face Space](https://img.shields.io/badge/🤗%20Hugging%20Face-Space-yellow)](https://huggingface.co/spaces/AbhishekDatta/AbhishekDatta-Career-Journey)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-green.svg)](https://openai.com/)
[![Gradio](https://img.shields.io/badge/Gradio-UI-orange.svg)](https://gradio.app/)

An intelligent AI-powered chatbot that serves as a virtual career assistant for Abhishek Datta, answering questions about his professional background, skills, and experience. Built with OpenAI's GPT-4o-mini and Gradio, this chatbot provides an interactive way for potential employers, clients, and recruiters to learn about Abhishek's 20+ years of experience in DevOps, SRE, and Chaos Engineering.

> **💡 Make It Your Own:** This project is fully open-source and customizable! Download the code, replace the career data with your own, and deploy your personalized AI career assistant in minutes. Perfect for professionals looking to create an interactive portfolio or automated career information hub.

## ⚠️ Important Disclaimers

> **Before Deploying:**
> 
> - **🔐 Security**: This application requires API keys stored as environment variables. Never commit API keys to version control. Use secure secret management for production deployments.
> 
> - **💰 API Costs**: This application uses OpenAI's API which incurs costs per request. Monitor your usage on the [OpenAI dashboard](https://platform.openai.com/usage). Set up billing alerts and rate limits to prevent unexpected charges.
> 
> - **🔒 Privacy**: Your LinkedIn profile and personal summary will be publicly accessible through the chatbot. Only include information you're comfortable sharing publicly. Do not include sensitive personal data.
> 
> - **🚫 No Authentication**: This is a public-facing chatbot without built-in authentication or rate limiting. Anyone can interact with it, potentially leading to API abuse or unexpected costs.
> 
> - **⚙️ Customization Required**: This code must be customized with your own data before deployment. Replace placeholder values (`YOUR NAME HERE`, `your_email@example.com`) and add your career information.
> 
> - **📊 Data Collection**: The application collects visitor emails and logs questions via Pushover notifications. Ensure compliance with privacy regulations (GDPR, CCPA, etc.) in your jurisdiction.
> 
> **Recommendation**: Test thoroughly in a development environment before deploying publicly. Monitor costs and usage regularly after deployment.

## 🌟 Live Demo

Try the chatbot here: [AbhishekDatta Career Chatbot](https://huggingface.co/spaces/AbhishekDatta/AbhishekDatta-Career-Journey)

![Thumbnail](thumbnail.jpg)

## 📚 Additional Documentation

This repository includes comprehensive documentation to help you get started:

- **[QUICKSTART.md](QUICKSTART.md)** - Get up and running in 5 minutes
- **[SETUP.md](SETUP.md)** - Detailed step-by-step installation and configuration guide
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Complete guide for deploying to Hugging Face Spaces
- **[SECURITY.md](SECURITY.md)** - Security best practices, risk assessment, and compliance guidelines
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Guidelines for contributing to the project
- **[CODE_COMPARISON.md](CODE_COMPARISON.md)** - Comparison between app.py and app_documented.py versions
- **[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)** - Detailed explanation of repository structure and file organization
- **[GITIGNORE_GUIDE.md](GITIGNORE_GUIDE.md)** - Understanding what files are ignored and why
- **[CHECKLIST.md](CHECKLIST.md)** - Step-by-step checklist for setting up your GitHub repository
- **[PACKAGE_SUMMARY.md](PACKAGE_SUMMARY.md)** - Overview of all files included in this package


## 📋 Table of Contents

- [Features](#-features)
- [How It Works](#-how-it-works)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Code Explanation](#-code-explanation)
- [Deployment](#-deployment)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

## ✨ Features

- **Intelligent Conversation**: Powered by OpenAI's GPT-4o-mini model for natural, context-aware responses
- **Career Information**: Answers questions about professional experience, skills, achievements, and career trajectory
- **Lead Capture**: Automatically collects contact information from interested visitors
- **Question Tracking**: Records unanswerable questions for continuous improvement
- **Real-time Notifications**: Sends instant alerts via Pushover when visitors express interest
- **Context-Aware**: Uses LinkedIn profile and personal summary for accurate, detailed responses
- **Professional Tone**: Maintains a professional and engaging communication style
- **24/7 Availability**: Always available to answer questions about Abhishek's career

## 🔍 How It Works

```
User Query → Gradio Interface → OpenAI GPT-4o-mini → Response Generation
                                        ↓
                              Function Calling (Tools)
                                        ↓
                    ┌───────────────────┴───────────────────┐
                    ↓                                       ↓
          record_user_details                   record_unknown_question
                    ↓                                       ↓
              Pushover Notification              Pushover Notification
```

1. **User Interaction**: Visitor asks a question through the Gradio chat interface
2. **Context Loading**: System loads Abhishek's LinkedIn profile and personal summary
3. **AI Processing**: GPT-4o-mini processes the query with full context
4. **Response Generation**: AI generates a professional, accurate response
5. **Tool Execution**: If needed, the AI can:
   - Record visitor contact details
   - Log questions it cannot answer
6. **Notification**: Pushover sends real-time alerts for important interactions

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Core programming language |
| **OpenAI GPT-4o-mini** | Large Language Model for conversation |
| **Gradio 5.31.0** | Web UI framework for chat interface |
| **pypdf** | PDF parsing for LinkedIn profile |
| **Pushover** | Real-time push notifications |
| **python-dotenv** | Environment variable management |
| **Hugging Face Spaces** | Deployment platform |

## 📁 Project Structure

```
.
├── app.py                      # Main application file
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── .env                        # Environment variables (not tracked)
├── me/
│   ├── linkedin.pdf           # LinkedIn profile data
│   └── summary.txt            # Personal summary and career breaks
└── thumbnail.jpg              # Project thumbnail
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Pushover account (for notifications)

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/AbhishekDatta/ai-career-chatbot.git
   cd ai-career-chatbot
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   PUSHOVER_TOKEN=your_pushover_app_token
   PUSHOVER_USER=your_pushover_user_key
   ```

   **Note:** Simply visit https://pushover.net/ and sign up for a free account, and create your API keys.
   
   Create two tokens in Pushover:
   1. **The User token** which you get from the home page of Pushover
   2. **The Application token** which you get by going to https://pushover.net/apps/build and creating an app

5. **Prepare your data**
   - Create a `me/` directory
   - Add your `linkedin.pdf` (export your LinkedIn profile as PDF)
   - Add your `summary.txt` with personal background information

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |
| `PUSHOVER_TOKEN` | Pushover application token | Yes |
| `PUSHOVER_USER` | Pushover user key | Yes |

### Customization

To customize the chatbot for your own use:

1. **Update Personal Information** in `app.py`:
   ```python
   self.name = "Your Name"
   ```

2. **Modify System Prompt**: Edit the `system_prompt()` method to adjust the chatbot's behavior

3. **Replace Data Files**:
   - Replace `me/linkedin.pdf` with your LinkedIn profile
   - Update `me/summary.txt` with your personal information

## 💻 Usage

### Running Locally

```bash
python app.py
```

The application will start a local Gradio server. Access it at:
```
http://127.0.0.1:7860
```

### Interacting with the Chatbot

Example queries you can ask:
- "Tell me about your experience in Site Reliability Engineering"
- "What is your leadership experience?"
- "Have you worked with Chaos Engineering?"
- "What are your key achievements?"
- "Can you explain your career breaks?"
- "What technologies do you specialize in?"

## 📖 Code Explanation

### Main Components

#### 1. **Notification System** (`push()` function)
```python
def push(text):
    """
    Sends push notifications via Pushover API
    
    Args:
        text (str): Message to send
    """
    requests.post(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": os.getenv("PUSHOVER_TOKEN"),
            "user": os.getenv("PUSHOVER_USER"),
            "message": text,
        }
    )
```
- Sends real-time notifications when important events occur
- Uses Pushover service for reliable push notifications
- Alerts when visitors provide contact info or ask unanswerable questions

#### 2. **Tool Functions**

**`record_user_details()`**
- Captures visitor contact information (email, name, notes)
- Triggers notification for lead follow-up
- Returns confirmation of successful recording

**`record_unknown_question()`**
- Logs questions the AI cannot answer
- Helps identify knowledge gaps
- Enables continuous improvement of the chatbot

#### 3. **OpenAI Function Calling Tools**

The chatbot uses OpenAI's function calling feature to execute specific actions:

```python
record_user_details_json = {
    "name": "record_user_details",
    "description": "Use this tool to record that a user is interested...",
    "parameters": {
        "type": "object",
        "properties": {
            "email": {"type": "string", "description": "The email address..."},
            "name": {"type": "string", "description": "The user's name..."},
            "notes": {"type": "string", "description": "Any additional information..."}
        },
        "required": ["email"]
    }
}
```

These JSON schemas define:
- Function name and description
- Expected parameters
- Required vs. optional fields
- Help GPT understand when and how to use each tool

#### 4. **The `Me` Class** (Core Application Logic)

**Initialization (`__init__`)**
```python
def __init__(self):
    self.openai = OpenAI()                    # Initialize OpenAI client
    self.name = "YOUR NAME HERE"              # Set identity
    
    # Load LinkedIn profile from PDF
    reader = PdfReader("me/linkedin.pdf")
    self.linkedin = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            self.linkedin += text
    
    # Load personal summary
    with open("me/summary.txt", "r", encoding="utf-8") as f:
        self.summary = f.read()
```
- Creates OpenAI client instance
- Extracts text from LinkedIn PDF using pypdf
- Loads personal summary from text file
- Prepares all context data for the AI

**Tool Call Handler (`handle_tool_call`)**
```python
def handle_tool_call(self, tool_calls):
    """
    Executes function calls requested by the AI model
    
    Args:
        tool_calls: List of tool calls from OpenAI response
        
    Returns:
        List of tool execution results
    """
    results = []
    for tool_call in tool_calls:
        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)
        print(f"Tool called: {tool_name}", flush=True)
        
        # Dynamically call the function by name
        tool = globals().get(tool_name)
        result = tool(**arguments) if tool else {}
        
        # Format result for OpenAI
        results.append({
            "role": "tool",
            "content": json.dumps(result),
            "tool_call_id": tool_call.id
        })
    return results
```
- Processes tool calls made by GPT
- Dynamically executes the requested function
- Returns results in OpenAI-compatible format
- Enables the conversation to continue with tool outputs

**System Prompt Generator (`system_prompt`)**
```python
def system_prompt(self):
    """
    Creates the system prompt with context for the AI model
    
    Returns:
        Complete system prompt string with career context
    """
    system_prompt = f"You are acting as {self.name}. ..."
    system_prompt += f"\n\n## Summary:\n{self.summary}\n\n"
    system_prompt += f"## LinkedIn Profile:\n{self.linkedin}\n\n"
    system_prompt += f"With this context, please chat with the user..."
    return system_prompt
```
- Defines the AI's role and behavior
- Injects LinkedIn profile and summary as context
- Sets conversation guidelines and objectives
- Instructs AI on when to use tools

**Chat Handler (`chat`)**
```python
def chat(self, message, history):
    """
    Main chat processing function with tool call support
    
    Args:
        message (str): User's current message
        history (list): Conversation history from Gradio
        
    Returns:
        AI's response as a string
    """
    # Build message list with system prompt and history
    messages = [
        {"role": "system", "content": self.system_prompt()}
    ] + history + [
        {"role": "user", "content": message}
    ]
    
    done = False
    while not done:
        # Call OpenAI API
        response = self.openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=tools
        )
        
        # Check if AI wants to call a tool
        if response.choices[0].finish_reason == "tool_calls":
            message = response.choices[0].message
            tool_calls = message.tool_calls
            
            # Execute the tool calls
            results = self.handle_tool_call(tool_calls)
            
            # Add tool calls and results to conversation
            messages.append(message)
            messages.extend(results)
        else:
            done = True
    
    return response.choices[0].message.content
```

**Key Features of the Chat Loop**:
1. **System Prompt Injection**: Every conversation includes the system prompt with context
2. **History Management**: Maintains conversation continuity
3. **Tool Call Loop**: Keeps calling OpenAI until no more tools are needed
4. **Gradio Integration**: Compatible with Gradio's message format

### Application Flow

```
Start
  ↓
Load LinkedIn PDF & Summary
  ↓
Initialize Gradio Interface
  ↓
Wait for User Message
  ↓
Build Messages Array (System + History + User)
  ↓
Call OpenAI API
  ↓
Check Response ──→ [Tool Call?] ──→ Yes ──→ Execute Tool
  │                                            ↓
  │                                      Add to Messages
  │                                            ↓
  │                                     Call OpenAI Again
  │                                            ↓
  └────────────←─────────────────────────────┘
  ↓
No (Regular Response)
  ↓
Return Response to User
  ↓
Display in Gradio
```

## 🌐 Deployment

### Deploying to Hugging Face Spaces

1. **Create a new Space** on [Hugging Face](https://huggingface.co/spaces)
2. **Select Gradio SDK** with Python 3.8+
3. **Upload files**:
   - `app.py`
   - `requirements.txt`
   - `me/linkedin.pdf`
   - `me/summary.txt`
   - `README.md` (optional, but recommended)
4. **Add secrets** in Space settings:
   - `OPENAI_API_KEY`
   - `PUSHOVER_TOKEN`
   - `PUSHOVER_USER`
5. **The Space will automatically build and deploy**

### Alternative Deployment Options

- **Docker**: Containerize the application
- **AWS/GCP/Azure**: Deploy on cloud platforms
- **Heroku**: Use for simple deployment
- **Railway**: Quick deployment with environment variables

## 🔮 Future Enhancements

Potential features and improvements:

- [ ] **Multi-language Support**: Add support for multiple languages
- [ ] **Voice Interface**: Integrate speech-to-text and text-to-speech
- [ ] **Analytics Dashboard**: Track conversation metrics and popular questions
- [ ] **Resume Generation**: Automatically generate formatted resumes
- [ ] **Interview Prep**: Practice interview questions with AI feedback
- [ ] **Skill Assessment**: Provide detailed technical skill assessments
- [ ] **Video Responses**: Generate short video responses for key questions
- [ ] **CRM Integration**: Connect with Salesforce, HubSpot, etc.
- [ ] **Calendar Integration**: Schedule meetings directly through the chat
- [ ] **Custom Branding**: White-label solution for other professionals
- [ ] **A/B Testing**: Test different conversation strategies
- [ ] **Sentiment Analysis**: Analyze visitor sentiment and engagement

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Contribution Guidelines

- Follow PEP 8 style guidelines
- Add comments and docstrings
- Update README if adding new features
- Test thoroughly before submitting PR

## 🔒 Security Best Practices

When deploying this application, follow these security guidelines:

### API Key Management
- ✅ Store all API keys in environment variables or secure secret management systems
- ✅ Never commit `.env` files or API keys to version control
- ✅ Rotate API keys regularly
- ✅ Use separate API keys for development and production

### Cost Control
- ✅ Set up billing alerts in your OpenAI account
- ✅ Implement rate limiting to prevent API abuse
- ✅ Monitor API usage regularly via OpenAI dashboard
- ✅ Set maximum spending limits on your OpenAI account

### Data Privacy
- ✅ Only include information you're comfortable making public
- ✅ Review your LinkedIn profile and summary for sensitive data
- ✅ Comply with privacy regulations (GDPR, CCPA) in your jurisdiction
- ✅ Add a privacy policy if collecting user data

### Production Deployment
- ✅ Test thoroughly in a staging environment first
- ✅ Implement proper logging and monitoring
- ✅ Consider adding authentication for sensitive deployments
- ✅ Set up error tracking (e.g., Sentry, Rollbar)
- ✅ Have a rollback plan ready

### Hugging Face Spaces Specific
- ✅ Use Spaces Secrets for all sensitive credentials
- ✅ Set Space visibility to Private if needed
- ✅ Monitor Space logs regularly
- ✅ Be aware that free tier has resource limitations

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

**Abhishek Datta**
- Email: contactabhishekdatta@gmail.com
- LinkedIn: [linkedin.com/in/a-datta](https://www.linkedin.com/in/a-datta)
- GitHub: [github.com/AbhishekDatta](https://github.com/AbhishekDatta)
- Medium: [@AbhishekDatta22](https://medium.com/@AbhishekDatta22)

---

## 🙏 Acknowledgments

- **Ed Donner** - Udemy trainer whose excellent [Agentic AI Engineering course](https://www.udemy.com/course/the-complete-agentic-ai-engineering-course/?im_ref=xTdU8FyE2xycRDfQPrT4BXOzUkpUVXX0ETqW080&sharedid=bing&irpid=2003851&utm_medium=affiliate&utm_source=impact&utm_audience=mx&utm_tactic=%22Loyalty%22%2C%22US+-+North+America%22&utm_content=3260104&utm_campaign=2003851&irgwc=1&couponCode=KEEPLEARNING) provided the foundational knowledge and implementation patterns for this project
- **OpenAI** for providing the GPT-4o-mini model
- **Gradio** for the amazing UI framework
- **Hugging Face** for free hosting on Spaces
- **Pushover** for reliable push notifications

---

<div align="center">

**⭐ If you find this project useful, please consider giving it a star!**

Made with ❤️ by [Abhishek Datta](https://github.com/AbhishekDatta)

</div>