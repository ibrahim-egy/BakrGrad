from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = "secretaryship"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/detect', methods=["POST"])
def detect():
    if request.method == "POST":
        image = request.files.get('image')
        # image.save(f"static/upload/{image.filename}")
        data = {
            "class": image.filename,
            "score": "99.9"
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
