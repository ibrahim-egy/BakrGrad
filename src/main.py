import os
from flask import Flask, render_template, request
from tf_model import tensorflow_detect
from yolo_model import yolo_detect
app = Flask(__name__)
app.secret_key = "secretaryship"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/detect-tf', methods=["POST"])
def detect_tensorflow():
    if request.method == "POST":

        for file in os.listdir("static/outputs/tf"):
            os.remove(f"static/outputs/tf/{file}")

        image = request.files.get('omarImage')
        path = f"static/upload/{image.filename}"
        image.save(path)
        result = tensorflow_detect(path)
        os.remove(path)
        data = {
            "class": result["class"],
            "score": result["score"],
            "result_image": result["result_image"]
        }
        return data


@app.route('/detect-yolo', methods=["POST"])
def detect_yolo():
    if request.method == "POST":

        for file in os.listdir("static/outputs/yolo"):
            os.remove(f"static/outputs/yolo/{file}")

        image = request.files.get('omarImage')
        path = f"static/upload/{image.filename}"
        image.save(path)
        result = yolo_detect(path)
        os.remove(path)
        data = {
            "class": result["class"],
            "score": result["score"],
            "result_image": result["result_image"]
        }
        return data


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)
