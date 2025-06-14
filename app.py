from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session
import os
import uuid
from utils.pdf_generator import generate_pdf
from utils.barcode_generator import generate_barcode_image

app = Flask(__name__)
app.secret_key = "delivery_label_secret_key"
app.config["UPLOAD_FOLDER"] = "output"

USERNAME = "test"
PASSWORD = "test123"

@app.route("/", methods=["GET"])
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username == USERNAME and password == PASSWORD:
        session["user"] = username
        return redirect("/dashboard")
    return redirect("/")

@app.route("/dashboard", methods=["GET"])
def dashboard():
    if "user" not in session:
        return redirect("/")
    return render_template("dashboard.html")

@app.route("/generate", methods=["POST"])
def generate():
    if "user" not in session:
        return redirect("/")

    sender_name = request.form.get("sender_name")
    sender_address = request.form.get("sender_address")
    receiver_name = request.form.get("receiver_name")
    receiver_address = request.form.get("receiver_address")

    delivery_id = str(uuid.uuid4().int)[:12]
    generate_barcode_image(delivery_id, output_dir=app.config["UPLOAD_FOLDER"])
    file_path = generate_pdf(sender_name, sender_address, receiver_name, receiver_address, delivery_id, output_path=app.config["UPLOAD_FOLDER"])

    filename = os.path.basename(file_path)
    return render_template("label.html", delivery_id=delivery_id, file_url=url_for("download_file", filename=filename))

@app.route("/download/<filename>", methods=["GET"])
def download_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename, as_attachment=True)

@app.route("/logout", methods=["GET"])
def logout():
    session.pop("user", None)
    return redirect("/")

if __name__ == "__main__":
    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
        os.makedirs(app.config["UPLOAD_FOLDER"])
    app.run(debug=True)
