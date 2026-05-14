from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask is working bro 😎"

if __name__ == "__main__":

    app.run(debug=True)
