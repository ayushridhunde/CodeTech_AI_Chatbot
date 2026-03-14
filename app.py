from flask import Flask, render_template, request, jsonify
import chatbot
import database

app = Flask(__name__)

# Initialize the database on startup
database.init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def chat():
    user_data = request.json
    user_message = user_data.get("message")
    
    # Generate a contextual response
    bot_reply = chatbot.get_response(user_message)
    
    # Save the interaction to logs
    try:
        database.log_chat(user_message, bot_reply)
    except Exception as e:
        print(f"Logging Error: {e}")
        
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)