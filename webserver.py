from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home(): 
    return "Discord bot ok"

def run():
    port = int(os.environ.get("PORT", 8080))  # Render te donne dynamiquement le port
    app.run(host="0.0.0.0", port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()




