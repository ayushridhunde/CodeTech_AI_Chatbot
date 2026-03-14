import sqlite3

def display_chat_history():
    try:
        # Connect to the database file
        conn = sqlite3.connect('chat_logs.db')
        cursor = conn.cursor()
        
        # Select all records from the logs table
        cursor.execute("SELECT user_msg, bot_res, timestamp FROM logs")
        rows = cursor.fetchall()
        
        if not rows:
            print("\n[!] No logs found. Please chat with the bot first to generate logs.")
        else:
            print("\n" + "="*50)
            print("        USER INTERACTION LOGS (SQLITE)")
            print("="*50)
            
            for row in rows:
                print(f"TIME: {row[2]}")
                print(f"USER: {row[0]}")
                print(f"BOT:  {row[1]}")
                print("-" * 50)
        
        conn.close()
        
    except sqlite3.OperationalError:
        print("\n[!] Error: chat_logs.db not found. Run app.py and send a message first.")
    except Exception as e:
        print(f"\n[!] An unexpected error occurred: {e}")

if __name__ == "__main__":
    display_chat_history()