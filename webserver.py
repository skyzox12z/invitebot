import os
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Discord bot ok"

def run():
    port = int(os.environ.get('PORT', 8080))  # Use the port assigned by Render, default to 8080 locally
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()



