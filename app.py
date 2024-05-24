from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    """
    This is use for hello purpose
    """
    return "Hello, Tuan has a nice day!"
