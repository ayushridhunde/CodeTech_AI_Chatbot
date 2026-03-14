import sqlite3

def view_logs():
    try:
        conn = sqlite3.connect('chat_logs.db')
        c = conn.cursor()
        c.execute("SELECT * FROM logs")
        rows = c.fetchall()
        print("\n--- Interaction Logs ---")
        for row in rows:
            print(f"User: {row[0]} | Bot: {row[1]} | Time: {row[2]}")
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    view_logs()