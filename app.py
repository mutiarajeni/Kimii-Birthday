from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("kue.html")


@app.route('/wish')
def wish():
    return render_template("index.html")

@app.route('/card')
def wish2():
    return render_template("asa.html")


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)