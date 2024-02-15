from flask import Flask, render_template, request, jsonify, redirect, url_for, Blueprint

app = Flask(__name__)

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("index.html", name="Joe")

@views.route("/profile")
def profile():
    args = request.args 
    name = args.get('name')
    return render_template("index.html", name=name)

@views.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # Add your authentication logic here
        # For example, you can check the username and password against a database
        # If the credentials are valid, you can redirect the user to the home page
        if username == "user" and password == "password":
            return redirect(url_for("home"))
        else:
            return "Invalid username or password"
    return render_template("login.html")

@views.route("/json")
def get_json():
    return jsonify({'name': 'tim', 'coolness': 10})

@views.route("/data", methods=["GET", "POST"])
def get_data():
    if request.method == "POST":
        data = request.json
        return jsonify(data)
    else:
        return "Send a POST request to this endpoint"

