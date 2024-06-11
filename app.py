from flask import Flask, render_template, jsonify, request
import os
import uuid
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

@app.route("/")
def home():
    return render_template('todolist.html')

@app.route("/firebase-config")
def firebase_config():
    config = {
        'apiKey': os.getenv('FIREBASE_API_KEY'),
        'authDomain': os.getenv('FIREBASE_AUTH_DOMAIN'),
        'databaseURL': os.getenv('FIREBASE_DATABASE_URL'),
        'projectId': os.getenv('FIREBASE_PROJECT_ID'),
        'storageBucket': os.getenv('FIREBASE_STORAGE_BUCKET'),
        'messagingSenderId': os.getenv('FIREBASE_MESSAGING_SENDER_ID'),
        'appId': os.getenv('FIREBASE_APP_ID'),
    }
    return jsonify(config)

@app.route("/generate-uuid", methods=['POST'])
def generate_uuid():
    new_uuid = str(uuid.uuid4())
    return jsonify({"uuid": new_uuid})

@app.route("/<uuid:list_uuid>")
def list_page(list_uuid):
    return render_template('todolist.html')

if __name__ == "__main__":
    app.run(debug=True)
