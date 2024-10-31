from dotenv import load_dotenv
import smtplib, ssl
import os

load_dotenv()

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    receiver = os.getenv("USERNAME")
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("Failed to authenticate. Check your username and password.")
    except Exception as e:
        print(f"An error occurred: {e}")
