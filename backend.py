from flask import Flask, request, jsonify
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Biar frontend boleh akses

# Ganti ini dengan API key kamu
openai.api_key = "ISI_API_KEY_KAMU_DI_SINI"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    try:
        # Panggil OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Kamu adalah HoshinoAi, teman ngobrol virtual yang ramah, cerdas, dan ceria."},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response.choices[0].message["content"].strip()
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": "Maaf, ada kesalahan saat menghubungi AI. 😢"}), 500

if __name__ == "__main__":
    app.run(debug=True)
