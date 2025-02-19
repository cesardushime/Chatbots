# 🤖 AI Chatbots - Powered by OpenAI & Gemini  

### 🚀 **Overview**  
This repository contains two powerful AI-driven chatbots:  
1. **ChatGPT-powered chatbot** using `openai`'s GPT-3.5 Turbo  
2. **Google Gemini-powered chatbot** using `google.generativeai`  

Both chatbots generate high-quality responses to user inputs, making them ideal for tasks like **content generation, Q&A, tutoring, and automation.**  

---

## 📌 **Features**  
✅ **OpenAI Chatbot** (`chat_withMe` function)  
- Uses OpenAI's `gpt-3.5-turbo` for generating intelligent responses.  
- Can handle conversational inputs and structured requests (e.g., cover letters, summaries, etc.).  

✅ **Google Gemini Chatbot**  
- Uses Google's Gemini AI (`gemini-1.5-flash`) for creative and knowledge-based responses.  
- Ideal for unique insights and innovative solutions.  

✅ **Both models in one repo**  
- Choose between **GPT-3.5 Turbo** or **Gemini** based on your needs.  
- Easy-to-use Python functions for seamless integration.  

---

## ⚙️ **Setup & Installation**  
### 1️⃣ **Clone the repository**  
```sh
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ **Install dependencies**  
```sh
pip install openai google-generativeai
```

### 3️⃣ **Set up API Keys**  
Replace **your API keys** in the script with your actual keys:  

🔹 OpenAI API Key (`openai.api_key = "your-openai-key"`)  
🔹 Google API Key (`genai.configure(api_key = "your-google-key")`)  

---

## 🚀 **Usage**  
### ✨ **Using OpenAI Chatbot**
```python
from chatbot_openai import chat_withMe

user_input = "Explain quantum computing in simple terms"
response = chat_withMe(user_input)
print("Chatbot:", response)
```

### ✨ **Using Google Gemini Chatbot**
```python
from chatbot_gemini import model

response = model.generate_content("Teach me something new")
print(response.text)
```

---

## 🔥 **Why Use This Repository?**  
✅ Compare **OpenAI's GPT-3.5 Turbo** vs. **Google Gemini** in real-time.  
✅ Simple API integration for personal or business use.  
✅ Customizable chatbot responses for different use cases.  

---

## 🛠 **Future Improvements**  
🔹 Add **prompt engineering techniques** for better responses.  
🔹 Implement a **web-based UI (Streamlit/Flask)** for interaction.  
🔹 Enable **memory** for continuous conversations.  

---

## 💡 **Contributing**  
Want to improve the chatbot? Feel free to **fork this repo** and submit pull requests! 🚀  

📧 **For inquiries:** [dushimezar2003@gmail.com ]  
