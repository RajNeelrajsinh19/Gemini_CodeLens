# 🤖 Gemini AI Code Reviewer

An AI-powered Code Reviewer built with **Streamlit** and **Google Gemini AI**.

This application allows users to paste or upload source code written in multiple programming languages and receive an AI-generated review including bugs, security issues, performance improvements, coding best practices, and an overall quality score.

---

# ✨ Features

- 🤖 Powered by Google Gemini AI
- 🐍 Supports Python
- ☕ Supports Java
- 💻 Supports C
- ⚡ Supports C++
- 🌐 Supports JavaScript
- 🐘 Supports PHP
- 💎 Supports Ruby
- 📊 Supports R
- 🐹 Supports Go
- 🦀 Supports Rust
- 📂 Upload source code files
- ✍️ Paste code directly
- 🔍 Detect bugs
- 🔒 Find security vulnerabilities
- ⚡ Suggest performance improvements
- 📖 Recommend coding best practices
- ⭐ Give overall code quality score
- 🎨 Clean Streamlit interface

---

# 📸 Screenshots

## Home Page

(Add your own screenshot here)

Example:

assets/home.png

---

## AI Review Result

(Add your review screenshot here)

Example:

assets/review.png

---

# 🚀 Demo

Coming Soon

---

# 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- python-dotenv

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/RajNeelrajsinh19/gemini-ai-code-reviewer.git
```

Go inside the folder

```bash
cd gemini-ai-code-reviewer
```

Create virtual environment

```bash
python -m venv .venv
```

Activate virtual environment

Windows

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Create API Key

Go to

https://aistudio.google.com/app/apikey

Create a Gemini API Key.

Create a file named

```
api.env
```

Inside it write

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

Application will open at

```
http://localhost:8501
```

---

# 💻 Supported Languages

- Python (.py)
- C (.c)
- C++ (.cpp)
- Java (.java)
- JavaScript (.js)
- TypeScript (.ts)
- PHP (.php)
- Ruby (.rb)
- R (.r)
- Go (.go)
- Rust (.rs)
- Kotlin (.kt)
- Swift (.swift)
- SQL (.sql)

---

# 📂 Project Structure

```
gemini-ai-code-reviewer/
│
├── app.py
├── api.env
├── requirements.txt
├── README.md
├── LICENSE
│
├── gemini_reviewer/
│   ├── __init__.py
│   ├── code_reviewer.py
│   ├── config.py
│   ├── gemini_client.py
│   ├── github_client.py
│   └── models.py
│
└── assets/
    ├── home.png
    └── review.png
```

---

# 🧠 How It Works

1. User uploads or pastes source code.
2. Streamlit sends the code to Gemini AI.
3. Gemini analyzes the code.
4. AI returns:
   - Bugs
   - Security Issues
   - Performance Improvements
   - Best Practices
   - Overall Rating
5. Results are displayed in a clean interface.

---

# 🎯 Future Improvements

- AI Chat
- Download Review as PDF
- Code Complexity Analysis
- Dark / Light Theme
- GitHub Integration
- Multi-file Review
- AI Fix Suggestions
- Code Comparison

---

# 👨‍💻 Author

**Raj Neelrajsinh**

GitHub

https://github.com/RajNeelrajsinh19

---

# 📄 License

MIT License

---

# ⭐ Support

If you like this project, please give it a ⭐ on GitHub.

It motivates future development.
