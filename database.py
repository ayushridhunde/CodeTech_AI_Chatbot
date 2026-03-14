import sqlite3

def init_db():
    # Connect to the database file (it will be created if it doesn't exist)
    conn = sqlite3.connect('chat_logs.db')
    c = conn.cursor()
    # Create the table to store user messages and bot responses
    c.execute('''CREATE TABLE IF NOT EXISTS logs 
                 (user_msg TEXT, bot_res TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def log_chat(user_msg, bot_res):
    conn = sqlite3.connect('chat_logs.db')
    c = conn.cursor()
    # Insert the interaction into the logs table
    c.execute("INSERT INTO logs (user_msg, bot_res) VALUES (?, ?)", (user_msg, bot_res))
    conn.commit()
    conn.close()