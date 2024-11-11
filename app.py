from openai import OpenAI
import os
import gradio as gr
from dotenv import load_dotenv
from llama_index.core import Document, VectorStoreIndex
from llama_index.core.settings import Settings
import pytesseract
from PIL import Image
from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader

# Load environment variables
load_dotenv()
api_key = os.getenv("NIM_API_KEY")

# Set up Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'  # Adjust this path if necessary

# Define the disclaimer
DISCLAIMER = """
IMPORTANT: I am LICA, an AI assistant designed to provide general financial education. 
Please note:
- I may make mistakes and my responses should not be considered as professional financial advice
- For specific financial decisions, please consult with a qualified financial advisor
- The information provided is for educational purposes only
- Response times may vary:
  • nvidia/nemotron-4-340b-instruct: May take over 2 minutes as it provides more detailed, customized advice

  • meta/llama-3.1-405b-instruct: Faster responses for quick inquiries

- Remember: Good things take time! For the most comprehensive analysis, please be patient.
"""

def parse_image(file_path: str) -> str:
    """Extract text from an image using Tesseract."""
    try:
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        print(f"Error parsing image: {e}")
        return ""

def parse_pdf(file_path: str) -> str:
    """Extract text from a PDF using LlamaParse."""
    try:
        parser = LlamaParse(result_type="markdown")
        file_extractor = {".pdf": parser}
        documents = SimpleDirectoryReader(input_files=[file_path], file_extractor=file_extractor).load_data()
        return " ".join([doc.text for doc in documents])
    except Exception as e:
        print(f"Error parsing PDF: {e}")
        return ""

def get_model_response(query, model_choice, context=""):
    try:
        # Prepare the prompt based on whether there's a context
        if context:
            prompt = f"""
            You are a financial education assistant. You have been provided with a credit report or financial document.
            Please analyze the following content and provide detailed, educational guidance:

            DOCUMENT CONTENT:
            {context}

            USER QUESTION:
            {query}

            Provide a comprehensive response that includes:
            1. Analysis of the provided document (if it's a credit report, analyze the key components)
            2. Detailed explanation of relevant financial concepts
            3. Specific recommendations based on the document content
            4. Step-by-step guidance for improvement
            5. Common pitfalls to avoid
            6. Additional resources or next steps

            Remember to maintain a helpful, educational tone while avoiding specific financial advice.
            """
        else:
            prompt = f"""
            Provide clear, practical financial education advice about: {query}
            
            Include:
            1. Basic concept explanation
            2. Real-world examples and scenarios
            3. Step-by-step guidance
            4. Common pitfalls to avoid
            5. Practical tips for implementation

            Remember to:
            - Use simple, clear language
            - Provide actionable advice
            - Include relevant examples
            - Highlight important warnings or considerations
            - Focus on practical implementation
            """

        # Rest of the model configuration and response generation
        valid_models = {
            "nvidia/nemotron-4-340b-instruct": {
                "base_url": "https://integrate.api.nvidia.com/v1",
                "api_key": os.getenv("NIM_API_KEY")
            },
            "meta/llama-3.1-405b-instruct": {
                "base_url": "https://integrate.api.nvidia.com/v1",
                "api_key": os.getenv("NIM_API_KEY")
            }
        }

        if model_choice not in valid_models:
            return f"Error: Invalid model choice."

        client = OpenAI(
            base_url=valid_models[model_choice]["base_url"],
            api_key=valid_models[model_choice]["api_key"]
        )

        completion = client.chat.completions.create(
            model=model_choice,
            messages=[{
                "role": "user",
                "content": prompt
            }],
            temperature=0.2,
            top_p=0.7,
            max_tokens=1024,
            stream=True
        )

        response_text = ""
        for chunk in completion:
            if chunk.choices[0].delta.content is not None:
                response_text += chunk.choices[0].delta.content
                print(chunk.choices[0].delta.content, end="")

        return response_text

    except Exception as e:
        print(f"Error getting model response: {e}")
        return f"Error: {str(e)}"

def process_file(file, query, model_choice):
    try:
        # Handle case when no file or query is provided
        if not file and not query.strip():
            return f"""{DISCLAIMER}

            👋 Welcome! You can:
            1. Ask any financial question directly
            2. Upload a document (PDF, Image) and ask questions about it
            
            Note: For document analysis, we automatically use meta/llama-3.1-405b-instruct model.
            The nvidia/nemotron-4-340b-instruct model currently doesn't support document analysis.
            
            Example: Upload your credit score report and ask "What steps can I take to improve my credit score?"
            Our AI will analyze your report and provide personalized recommendations!
            
            Currently using model: {model_choice}"""

        # Force model choice to meta/llama for file uploads
        if file and model_choice == "nvidia/nemotron-4-340b-instruct":
            model_choice = "meta/llama-3.1-405b-instruct"

        # Extract text from uploaded file if present
        file_content = ""
        if file:
            if file.name.lower().endswith(('.png', '.jpg', '.jpeg')):
                file_content = parse_image(file.name)
            elif file.name.lower().endswith('.pdf'):
                file_content = parse_pdf(file.name)
            else:
                return "Unsupported file format. Please upload a PDF or image file."

        # Get response from the model
        response = get_model_response(query, model_choice, file_content)
        
        return f"""{DISCLAIMER}

        💡 ANALYSIS & GUIDANCE (Using {model_choice})
        {'-' * 50}
        {response}

        📚 RECOMMENDED RESOURCES
        {'-' * 50}
        - Consumer Financial Protection Bureau: https://www.consumerfinance.gov/
        - Financial Planning Association: https://www.plannersearch.org/
        - Khan Academy Finance: https://www.khanacademy.org/economics-finance-domain
        
        ❓ Want to learn more? Feel free to ask follow-up questions!"""

    except Exception as e:
        return f"Error processing request: {e}"

# Update Gradio interface
interface = gr.Interface(
    fn=process_file,
    inputs=[
        gr.File(
            label="Upload a document (PDF, Image) - Note: Document analysis only available with meta/llama-3.1-405b-instruct model",
            file_types=[".pdf", ".png", ".jpg", ".jpeg"]
        ),
        gr.Textbox(
            label="What would you like to know?",
            placeholder="Ask a question about the uploaded document or any financial topic"
        ),
        gr.Radio(
            choices=["nvidia/nemotron-4-340b-instruct", "meta/llama-3.1-405b-instruct"],
            label="Choose AI Model",
            value="meta/llama-3.1-405b-instruct"
        )
    ],
    outputs="text",
    title="LICA - Your Financial Education Assistant",
    description=f"""Welcome to LICA, your interactive financial education assistant! 
    Ask questions directly or upload documents (PDF, Images) for analysis and customized advice.
    
    Note: For document analysis, we automatically use meta/llama-3.1-405b-instruct model.
    The nvidia/nemotron-4-340b-instruct model currently doesn't support document analysis.
    
    Example: Upload your credit score report and ask "What steps can I take to improve my credit score?"
    Our AI will analyze your report and provide personalized recommendations!
    
    {DISCLAIMER}"""
)

# Launch the interface
if __name__ == "__main__":
    interface.launch()
