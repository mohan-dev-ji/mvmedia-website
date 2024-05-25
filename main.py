from flask import Flask, render_template, request
import requests
import smtplib

MY_EMAIL = "moveraitch@gmail.com"
MY_PASSWORD = "drrr ivsh tzon rkgg"

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html", highlight="home")

@app.route('/services')
def services_page():
    return render_template("services.html", highlight="services")

@app.route('/pricing')
def pricing_page():
    return render_template("pricing.html", highlight="pricing")

@app.route('/contact', methods=["GET", "POST"])
def contact_page():
    if request.method == "POST":
        data = request.form
        send_msg(data["name"], data["email"], data["subject"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False, highlight="contact")

def send_msg(name, email, subject, message):
    email_message = f"Subject:Message from {name}\n\nName: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # transport layer security
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="moveraitch@yahoo.com",
                            msg=email_message
                            )

if __name__ == "__main__":
    app.run(debug=True)