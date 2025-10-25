"""
AI Career Chatbot for YOUR NAME HERE

This application creates an intelligent chatbot that serves as a virtual career assistant,
answering questions about YOUR NAME HERE's professional background, skills, and experience.

The chatbot uses OpenAI's GPT-4o-mini model with function calling capabilities to:
1. Answer career-related questions using LinkedIn profile and personal summary
2. Capture visitor contact information for lead generation
3. Record questions it cannot answer for continuous improvement
4. Send real-time notifications via Pushover for important interactions

IMPORTANT - Security & Deployment Checklist:
⚠️ Replace all placeholder values (YOUR NAME HERE, your_email@example.com)
⚠️ Store API keys securely in environment variables (never commit to git)
⚠️ Monitor OpenAI API usage regularly to control costs
⚠️ Review career data for sensitive information before deploying
⚠️ Test thoroughly in development before production deployment
⚠️ Consider adding rate limiting to prevent API abuse

Author: YOUR NAME HERE
Contact: your_email@example.com
License: MIT
"""

from dotenv import load_dotenv
from openai import OpenAI
import json
import os
import requests
from pypdf import PdfReader
import gradio as gr


# Load environment variables from .env file
# override=True ensures .env values take precedence over system environment variables
load_dotenv(override=True)


def push(text):
    """
    Send a push notification via Pushover service.
    
    Pushover is used to send real-time alerts to mobile devices when:
    - A visitor provides their contact information
    - A question cannot be answered by the chatbot
    
    Args:
        text (str): The message content to send in the notification
        
    Returns:
        None
        
    Environment Variables Required:
        PUSHOVER_TOKEN: Application token from Pushover
        PUSHOVER_USER: User key from Pushover account
    """
    requests.post(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": os.getenv("PUSHOVER_TOKEN"),
            "user": os.getenv("PUSHOVER_USER"),
            "message": text,
        }
    )


def record_user_details(email, name="Name not provided", notes="not provided"):
    """
    Record visitor contact details and send notification.
    
    This function is called by the AI when a visitor expresses interest in getting
    in touch and provides their email address. It triggers a Pushover notification
    to alert about the new lead.
    
    Args:
        email (str): Visitor's email address (required)
        name (str, optional): Visitor's name. Defaults to "Name not provided"
        notes (str, optional): Additional context from the conversation. 
                              Defaults to "not provided"
    
    Returns:
        dict: Confirmation message {"recorded": "ok"}
        
    Example:
        >>> record_user_details("john@example.com", "John Doe", "Interested in SRE role")
        {"recorded": "ok"}
    """
    push(f"Recording {name} with email {email} and notes {notes}")
    return {"recorded": "ok"}


def record_unknown_question(question):
    """
    Record questions that the chatbot cannot answer.
    
    This function helps identify knowledge gaps and areas for improvement.
    When the AI doesn't know how to answer a question, it calls this function
    to log the question for later review.
    
    Args:
        question (str): The question that couldn't be answered
    
    Returns:
        dict: Confirmation message {"recorded": "ok"}
        
    Example:
        >>> record_unknown_question("What is your favorite programming language?")
        {"recorded": "ok"}
    """
    push(f"Recording {question}")
    return {"recorded": "ok"}


# OpenAI Function Calling Schema: record_user_details
# This JSON schema defines how the AI should call the record_user_details function
record_user_details_json = {
    "name": "record_user_details",
    "description": "Use this tool to record that a user is interested in being in touch and provided an email address",
    "parameters": {
        "type": "object",
        "properties": {
            "email": {
                "type": "string",
                "description": "The email address of this user"
            },
            "name": {
                "type": "string",
                "description": "The user's name, if they provided it"
            },
            "notes": {
                "type": "string",
                "description": "Any additional information about the conversation that's worth recording to give context"
            }
        },
        "required": ["email"],  # Only email is mandatory
        "additionalProperties": False
    }
}

# OpenAI Function Calling Schema: record_unknown_question
# This JSON schema defines how the AI should call the record_unknown_question function
record_unknown_question_json = {
    "name": "record_unknown_question",
    "description": "Always use this tool to record any question that couldn't be answered as you didn't know the answer",
    "parameters": {
        "type": "object",
        "properties": {
            "question": {
                "type": "string",
                "description": "The question that couldn't be answered"
            },
        },
        "required": ["question"],
        "additionalProperties": False
    }
}

# Tools array for OpenAI function calling
# These tools enable the AI to execute specific actions during conversations
tools = [
    {"type": "function", "function": record_user_details_json},
    {"type": "function", "function": record_unknown_question_json}
]


class Me:
    """
    Main chatbot class that manages the AI-powered career assistant.
    
    This class handles:
    - Loading and managing career data (LinkedIn profile, personal summary)
    - Processing chat messages with OpenAI GPT-4o-mini
    - Executing tool calls (recording contacts, logging questions)
    - Maintaining conversation context and history
    
    Attributes:
        openai (OpenAI): OpenAI API client instance
        name (str): The name of the person represented by this chatbot
        linkedin (str): Extracted text from LinkedIn profile PDF
        summary (str): Personal background and career summary text
    """

    def __init__(self):
        """
        Initialize the chatbot with OpenAI client and career data.
        
        This method:
        1. Creates an OpenAI client using API key from environment
        2. Loads and extracts text from LinkedIn profile PDF
        3. Reads personal summary from text file
        
        Environment Variables Required:
            OPENAI_API_KEY: API key for OpenAI services
            
        File Requirements:
            me/linkedin.pdf: LinkedIn profile exported as PDF
            me/summary.txt: Personal background and career breaks information
        """
        # Initialize OpenAI client (API key from environment variable)
        self.openai = OpenAI()
        
        # Set the identity for this chatbot
        self.name = "YOUR NAME HERE"
        
        # Load and extract text from LinkedIn profile PDF
        reader = PdfReader("me/linkedin.pdf")
        self.linkedin = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                self.linkedin += text
        
        # Load personal summary from text file
        with open("me/summary.txt", "r", encoding="utf-8") as f:
            self.summary = f.read()

    def handle_tool_call(self, tool_calls):
        """
        Execute function calls requested by the AI model.
        
        When the AI decides to use a tool (e.g., record_user_details), this method:
        1. Extracts the tool name and arguments from the AI's response
        2. Dynamically calls the corresponding Python function
        3. Returns the results in a format OpenAI can understand
        
        This enables a multi-turn conversation where the AI can:
        - Call a function
        - Receive the result
        - Continue the conversation with that information
        
        Args:
            tool_calls (list): List of ToolCall objects from OpenAI response
            
        Returns:
            list: List of dictionaries containing tool execution results,
                  formatted for OpenAI's chat completion API
                  
        Example Flow:
            AI wants to record email → handle_tool_call() executes function →
            Result returned to AI → AI continues conversation
        """
        results = []
        
        for tool_call in tool_calls:
            # Extract function name and arguments
            tool_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            
            # Log the tool call for debugging
            print(f"Tool called: {tool_name}", flush=True)
            
            # Dynamically get the function from global scope
            tool = globals().get(tool_name)
            
            # Execute the function with provided arguments
            result = tool(**arguments) if tool else {}
            
            # Format result for OpenAI API
            results.append({
                "role": "tool",
                "content": json.dumps(result),
                "tool_call_id": tool_call.id
            })
            
        return results
    
    def system_prompt(self):
        """
        Generate the system prompt with career context for the AI.
        
        The system prompt is crucial as it:
        1. Defines the AI's role and personality
        2. Provides career data (LinkedIn profile, summary) as context
        3. Sets behavioral guidelines (professional, engaging)
        4. Instructs when to use tools (record contacts, log questions)
        
        Returns:
            str: Complete system prompt including all career context
            
        Prompt Structure:
            1. Role definition and purpose
            2. Behavioral guidelines
            3. Tool usage instructions
            4. Career summary section
            5. LinkedIn profile section
            6. Final character instruction
        """
        # Define the AI's role and behavior
        system_prompt = f"You are acting as {self.name}. You are answering questions on {self.name}'s website, \
particularly questions related to {self.name}'s career, background, skills and experience. \
Your responsibility is to represent {self.name} for interactions on the website as faithfully as possible. \
You are given a summary of {self.name}'s background and LinkedIn profile which you can use to answer questions. \
Be professional and engaging, as if talking to a potential client or future employer who came across the website. \
If you don't know the answer to any question, use your record_unknown_question tool to record the question that you couldn't answer, even if it's about something trivial or unrelated to career. \
If the user is engaging in discussion, try to steer them towards getting in touch via email; ask for their email and record it using your record_user_details tool. "

        # Inject career data as context
        system_prompt += f"\n\n## Summary:\n{self.summary}\n\n## LinkedIn Profile:\n{self.linkedin}\n\n"
        
        # Final instruction to stay in character
        system_prompt += f"With this context, please chat with the user, always staying in character as {self.name}."
        
        return system_prompt
    
    def chat(self, message, history):
        """
        Process a chat message and generate a response using OpenAI.
        
        This is the main chat handler that:
        1. Builds the conversation context (system prompt + history + new message)
        2. Calls OpenAI's chat completion API with tool support
        3. Handles tool calls if the AI decides to use them
        4. Loops until the AI provides a final response (no more tool calls)
        5. Returns the AI's response to display in Gradio
        
        The tool call loop enables the AI to:
        - Decide it needs to call a function
        - Get the function result
        - Use that result to formulate the final response
        
        Args:
            message (str): The user's latest message
            history (list): Conversation history in Gradio format
                           [{"role": "user", "content": "..."}, 
                            {"role": "assistant", "content": "..."}, ...]
        
        Returns:
            str: The AI's response message to display to the user
            
        Example Flow:
            User: "My email is john@example.com"
            → AI calls record_user_details tool
            → Tool executes and returns {"recorded": "ok"}
            → AI receives confirmation
            → AI responds: "Thank you! I've recorded your information..."
        """
        # Build the complete message array for OpenAI
        # Format: [system_prompt, ...conversation_history..., new_user_message]
        messages = [
            {"role": "system", "content": self.system_prompt()}
        ] + history + [
            {"role": "user", "content": message}
        ]
        
        # Tool call loop: keep calling until no more tools are needed
        done = False
        while not done:
            # Call OpenAI API with tools enabled
            response = self.openai.chat.completions.create(
                model="gpt-4o-mini",      # Use GPT-4o-mini for efficiency
                messages=messages,         # Full conversation context
                tools=tools                # Available function tools
            )
            
            # Check if the AI wants to call a tool
            if response.choices[0].finish_reason == "tool_calls":
                # Extract tool calls from response
                message = response.choices[0].message
                tool_calls = message.tool_calls
                
                # Execute the requested tools
                results = self.handle_tool_call(tool_calls)
                
                # Add tool calls and results to conversation history
                messages.append(message)
                messages.extend(results)
                
                # Loop continues - AI will process tool results
            else:
                # No more tool calls - we have the final response
                done = True
        
        # Return the AI's final message content
        return response.choices[0].message.content
    

if __name__ == "__main__":
    """
    Application entry point.
    
    Creates a Gradio chat interface and launches the web server.
    The interface uses Gradio's ChatInterface component with:
    - type="messages": Uses the standard message format for history
    - me.chat: The chat processing function
    
    Access the interface at: http://127.0.0.1:7860
    """
    # Initialize the chatbot
    me = Me()
    
    # Create and launch Gradio interface
    # type="messages" ensures compatibility with the message format
    gr.ChatInterface(me.chat, type="messages").launch()
