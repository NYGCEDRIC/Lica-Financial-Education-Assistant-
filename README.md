# 💸 Lica (Financial Literacy Chatbot)

This project was created for the NVIDIA and LlamaIndex Developer Contest to address a pressing need for financial literacy. Despite the critical role financial knowledge plays in people's lives, studies show that **only 33% of adults worldwide** are financially literate, and many individuals struggle with understanding credit reports, debt management, and personal finance. By leveraging advanced technologies like **NVIDIA's NIM** and **LlamaIndex**, this Gradio-based chatbot aims to make financial advice more accessible, personalized, and actionable.

## Why Focus on Financial Literacy?

Financial literacy is a cornerstone for economic empowerment and stability. Inadequate financial knowledge can lead to poor credit scores, debt accumulation, and missed opportunities for wealth building. This chatbot was designed to simplify the process of analyzing financial documents like credit reports, offering tailored advice to help users make informed financial decisions, boost their creditworthiness, and achieve their financial goals.


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
git clone https://github.com/yourusername/lica.git
cd lica
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
