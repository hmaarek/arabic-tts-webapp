from flask import Flask, request, send_file, render_template
from gtts import gTTS
import os
from uuid import uuid4

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        if not text.strip():
            return render_template("index.html", error="Please enter some Arabic text.")

        filename = f"{uuid4()}.mp3"
        tts = gTTS(text, lang="ar")
        tts.save(filename)

        return send_file(filename, as_attachment=True, download_name="arabic_audio.mp3", mimetype="audio/mpeg")

    return render_template("index.html")

iif __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

