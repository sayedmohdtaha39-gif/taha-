from flask import Flask, request, render_template_string, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure your Gemini API key
genai.configure(api_key="AIzaSyARMu2ABhYK7YpS7rDM7P6Gkbp5G1kqynU")

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# HTML template embedded
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hertzsoft Chatbot</title>
    <style>
        body { font-family: Arial; background: black; color: yellow; padding: 20px; }
        .container { max-width: 700px; margin:auto; background:#222; padding:25px; border-radius:15px; box-shadow:0 0 20px yellow; }
        h1, h2 { text-align:center; text-shadow:0 0 10px yellow; }
        textarea { width:100%; height:80px; padding:10px; border-radius:8px; border:2px solid yellow; background:black; color:yellow; font-size:14px; }
        button { padding:10px 20px; background:yellow; color:black; border:none; border-radius:8px; cursor:pointer; font-weight:bold; transition:all 0.3s; }
        button:hover { background:gold; box-shadow:0 0 15px yellow; }
        .chatbox { margin-top:20px; }
        .message { margin-bottom:15px; padding:10px; border-radius:8px; }
        .user { background:#444; color:yellow; }
        .bot { background:green; color:black; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hertzsoft Chatbot</h1>
        <h2>Ask anything about Hertzsoft</h2>
        <textarea id="message" placeholder="Type your question..."></textarea><br><br>
        <button onclick="sendMessage()">Send</button>
        <div class="chatbox" id="chatbox"></div>
    </div>

    <script>
        async function sendMessage() {
            const msgBox = document.getElementById("message");
            const chatBox = document.getElementById("chatbox");
            const message = msgBox.value.trim();
            if (!message) return;

            const userDiv = document.createElement("div");
            userDiv.className = "message user";
            userDiv.textContent = message;
            chatBox.appendChild(userDiv);

            msgBox.value = "";

            try {
                const res = await fetch("/chat", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ message })
                });
                const data = await res.json();

                const botDiv = document.createElement("div");
                botDiv.className = "message bot";
                botDiv.innerHTML = data.reply;
                chatBox.appendChild(botDiv);

                chatBox.scrollTop = chatBox.scrollHeight;
            } catch (err) {
                alert("Error: " + err);
            }
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_template)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    try:
        response = model.generate_content(user_input)
        reply = response.text
    except Exception as e:
        reply = f"Error: {e}"
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)

