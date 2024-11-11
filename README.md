# 💸 Financial Literacy Chatbot

This project is a Gradio-based chatbot designed to provide financial advice by analyzing financial documents like credit reports using LlamaIndex and NVIDIA technologies.

## ✨ Features
- 📄 Upload PDFs or images for analysis
- 🤖 Personalized financial advice based on uploaded documents

## 🛠️ Prerequisites
- 🐍 Python 3.7+
- 🔑 An API key for Llama Cloud and NVIDIA NIM

## 🚀 Getting Started

### 1. 📂 Clone the Repository
Fork the repository and clone it locally:
```bash
git clone https://github.com/yourusername/my-financial-chatbot.git
cd my-financial-chatbot
```
### 2. 📦 Install Dependencies
Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```
### 3. 🔧 Set Up Environment Variables
Create a `.env` file in the project root by copying the `.env.example` file:
```bash
cp .env.example .env
```
Open `.env` and replace the placeholders with your actual API keys:

```ini
LLAMA_CLOUD_API_KEY=your_actual_llama_cloud_api_key
NIM_API_KEY=your_actual_nim_api_key
```
### 4. ▶️ Run the Application
Start the Gradio app:
```bash
python app.py
```
