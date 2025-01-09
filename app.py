from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur mon applicatrion web !"
            "Il s'agit d'un test pour le stage 2025 Alvarez Diaz Quentin "

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
