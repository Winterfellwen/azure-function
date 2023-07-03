from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from Peter Flask"

if __name__ == '__main__':
    app.run()
