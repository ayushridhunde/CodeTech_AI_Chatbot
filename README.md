# AI-Powered Contextual Chatbot

This project is an intelligent chatbot developed as part of an AI Internship task at **CodeTech IT Solutions**. It features a rule-based NLP engine and integrated database logging.

## 🚀 Key Features
- **Contextual Responses:** Provides smart answers for technical domains like **Blockchain** (Carbon Credit Tracking) and **Biomedical Signal Processing** (ECG Classification).
- **User Interaction Logs:** Automatically saves all chat history into a **SQLite database** with timestamps.
- **Web Interface:** A clean and responsive UI built using **Flask**.

## 🛠️ Tech Stack
- **Language:** Python
- **Backend Framework:** Flask
- **Database:** SQLite3
- **Frontend:** HTML5, CSS3

## 📂 Project Structure
- `app.py`: Main Flask application server.
- `chatbot.py`: Logic for generating intelligent responses.
- `database.py`: Database connection and logging functions.
- `read_logs.py`: Utility script to view interaction logs in the terminal.
- `templates/index.html`: The frontend user interface.

## 📝 How to Run
1. Install requirements: `pip install flask`
2. Start the server: `python app.py`
3. Open in browser: `http://127.0.0.1:5000`
4. To view logs: `python read_logs.py`
