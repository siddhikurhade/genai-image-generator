import os
import uuid

from flask import Flask, render_template, request, send_file, jsonify
from dotenv import load_dotenv
from huggingface_hub import InferenceClient


# ============================================================
# LOAD .ENV
# ============================================================

load_dotenv()


# ============================================================
# FLASK APP
# ============================================================

app = Flask(__name__)


# ============================================================
# HUGGING FACE TOKEN
# ============================================================

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise RuntimeError(
        "HF_TOKEN not found.\n"
        "Create a .env file beside app.py and add:\n"
        "HF_TOKEN=your_token_here"
    )


# ============================================================
# MODEL
# ============================================================

MODEL = "black-forest-labs/FLUX.1-dev"


# ============================================================
# HUGGING FACE CLIENT
# ============================================================
# IMPORTANT:
# We are NOT forcing fal-ai.
# Hugging Face automatically selects the provider.

client = InferenceClient(
    api_key=HF_TOKEN,
    provider="auto"
)


# ============================================================
# HOME PAGE
# ============================================================

@app.route("/")
def home():
    return render_template("index.html")


# ============================================================
# GENERATE IMAGE
# ============================================================

@app.route("/generate", methods=["POST"])
def generate_image():

    try:

        # ----------------------------------------------------
        # Receive JSON
        # ----------------------------------------------------

        data = request.get_json()

        if not data:

            return jsonify({
                "success": False,
                "error": "No request data received."
            }), 400


        # ----------------------------------------------------
        # Read prompt
        # ----------------------------------------------------

        prompt = data.get("prompt", "").strip()


        # ----------------------------------------------------
        # Validate prompt
        # ----------------------------------------------------

        if not prompt:

            return jsonify({
                "success": False,
                "error": "Please enter a prompt."
            }), 400


        print("\n")
        print("=" * 60)
        print("GENERATIVE AI IMAGE GENERATION")
        print("=" * 60)
        print("Prompt:", prompt)
        print("Model:", MODEL)
        print("Provider: AUTO")
        print("=" * 60)


        # ----------------------------------------------------
        # GENERATE IMAGE
        # ----------------------------------------------------

        image = client.text_to_image(

            prompt=prompt,

            model=MODEL

        )


        # ----------------------------------------------------
        # CREATE GENERATED FOLDER
        # ----------------------------------------------------

        generated_folder = "generated"

        os.makedirs(
            generated_folder,
            exist_ok=True
        )


        # ----------------------------------------------------
        # CREATE UNIQUE FILE NAME
        # ----------------------------------------------------

        filename = (
            str(uuid.uuid4()) + ".png"
        )


        filepath = os.path.join(

            generated_folder,

            filename

        )


        # ----------------------------------------------------
        # SAVE IMAGE
        # ----------------------------------------------------

        image.save(

            filepath,

            format="PNG"

        )


        print("SUCCESS!")
        print("Image saved:", filepath)
        print("=" * 60)
        print()


        # ----------------------------------------------------
        # SEND RESPONSE
        # ----------------------------------------------------

        return jsonify({

            "success": True,

            "image": "/generated/" + filename,

            "message": "Image generated successfully."

        })


    except Exception as e:

        print("\n")
        print("=" * 60)
        print("IMAGE GENERATION ERROR")
        print("=" * 60)
        print(str(e))
        print("=" * 60)
        print()


        error_message = str(e)


        # ----------------------------------------------------
        # Friendly authentication message
        # ----------------------------------------------------

        if "401" in error_message:

            error_message = (
                "Hugging Face authentication failed. "
                "Please create a new Fine-grained token "
                "with 'Make calls to Inference Providers' "
                "permission and update your .env file."
            )


        return jsonify({

            "success": False,

            "error": error_message

        }), 500


# ============================================================
# SERVE GENERATED IMAGE
# ============================================================

@app.route("/generated/<filename>")
def generated_image(filename):

    filepath = os.path.join(

        "generated",

        filename

    )


    if not os.path.exists(filepath):

        return jsonify({

            "success": False,

            "error": "Image file not found."

        }), 404


    return send_file(

        filepath,

        mimetype="image/png"

    )


# ============================================================
# HEALTH CHECK
# ============================================================

@app.route("/health")
def health():

    return jsonify({

        "status": "running",

        "model": MODEL,

        "provider": "auto"

    })


# ============================================================
# RUN SERVER
# ============================================================

if __name__ == "__main__":

    print()
    print("=" * 60)
    print("       GENERATIVE AI IMAGE GENERATOR")
    print("=" * 60)
    print("Model    :", MODEL)
    print("Provider :", "AUTO")
    print("Server   :", "http://127.0.0.1:5000")
    print("Health   :", "http://127.0.0.1:5000/health")
    print("=" * 60)
    print()


    app.run(

        host="127.0.0.1",

        port=5000,

        debug=True

    )