import os
import smtplib
import logging
from dotenv import load_dotenv

# Logging configuration
logging.basicConfig(
    filename='reminder.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def reminder_email():
    # Load and set env variables
    load_dotenv(override=True)
    sender        = os.getenv("SENDER")
    recipient     = os.getenv("RECIPIENT")
    gmail_smtp_pw = os.getenv("GMAIL_SMTP_PW")

    # Construct email
    subject = "Quote Added"
    message = """\
    Hey there, a new quote has been added <3<br><br>

    Check it out <a href="https://example.com/">here</a>."""
    content = f'Subject: {subject}\nContent-Type: text/html\n\n{message}'

    try:
        # Start up SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, gmail_smtp_pw)
        logging.info("SMTP server login successful.")

        # Send email
        server.sendmail(sender, recipient, content)
        logging.info(f"Email sent to {recipient} successfully.")

    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {e}")

    finally:
        server.quit()
        logging.info("SMTP server connection closed.")
