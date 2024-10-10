import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pyttsx3
import stdiomask

engine = pyttsx3.init()

def send_email(sender_email, receiver_email, subject, message_body, smtp_server, smtp_port, login, password):
    try:
        # Create message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(message_body, "plain"))
        
        # Setup the server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Enable security
            server.login(login, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")


def initiate_send():
    engine.say("Which email would you like to use?")
    engine.runAndWait()
    sender_email = input("Enter sender email: ").lower()
    
    engine.say("Who would you like to send it to?")
    engine.runAndWait()
    receiver_email = input("Enter receiver email: ").lower()

    engine.say("What would be the subject of this email?")
    engine.runAndWait()
    subject = input("Enter subject: ").lower()

    engine.say("What would you like me to write?")
    engine.runAndWait()
    message_body = input("Enter body message: ").lower()

    smtp_server = "smtp.gmail.com"  # For Gmail
    smtp_port = 587  # For Gmail

    password = stdiomask.getpass(prompt="Password: ") # Be cautious with sensitive data

    print(f"Sending email to {receiver_email} ...")
    send_email(sender_email, receiver_email, subject, message_body, smtp_server, smtp_port, sender_email, password)

# Usage example
if __name__ == "__main__":
    initiate_send()
