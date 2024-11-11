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

### 1. 📂 Use this repo as a template and Clone the Repository
Clone it locally * via terminal of your favourite code editor):
```bash
git clone repo url for example https://github.com/NYGCEDRIC/lica.git
cd <name of the repo>(i.e lica)
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
#### Open and Edit the `.env` File:
1. **Using a Code Editor**: Open the `.env` file in your code editor.
2. **Using the Terminal**: You can also open it directly in the terminal using `nano` (Linux/macOS) or `notepad` (Windows):
   - For Linux/macOS:
     ```bash
     nano .env
     ```
   - For Windows:
     ```bash
     notepad .env
     ```
3. Replace the placeholders with your actual API keys:
   ```ini
   LLAMA_CLOUD_API_KEY=your_actual_llama_cloud_api_key
   NIM_API_KEY=your_actual_nim_api_key

### 4. ▶️ Run the Application
Start the Gradio app:
```bash
python app.py
```
