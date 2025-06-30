import sqlite3
import os, shutil, smtplib
from datetime import datetime
from dotenv import load_dotenv
import logging
from email.message import EmailMessage

# backup.py info logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Output to backup.log
file_handler = logging.FileHandler('backup.log')
file_handler.setLevel(logging.INFO)

# Log time, level, location & msg
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.propagate = False  # Only propagate logs from this file

def backup_db():
    # Load env vars
    load_dotenv(override=True)
    sender = os.getenv("SENDER")
    recipient = os.getenv("SENDER")
    gmail_smtp_pw = os.getenv("GMAIL_SMTP_PW")

    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_filename = f"quotes_{now}.db"

    try:
        # Backup DB
        source = sqlite3.connect("quotes.db")
        dest = sqlite3.connect(backup_filename)
        with dest:
            source.backup(dest, pages=1, progress=None)
        source.close()
        dest.close()
        logger.info(f"Database safely backed up to {backup_filename}")

        # Prepare email
        msg = EmailMessage()
        msg["From"] = sender
        msg["To"] = recipient
        msg["Subject"] = f"Quotes DB Backup"
        msg.set_content("Attached is the latest backup of the quotes DB file.")

        # Attach file
        with open(backup_filename, "rb") as f:
            msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=backup_filename)

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, gmail_smtp_pw)
        server.send_message(msg)
        logger.info(f"Backup email sent to {recipient} successfully.")

    except Exception as e:
        logger.error(f"Failed during backup or email: {e}")

    finally:
        if 'server' in locals():
            server.quit()
            logger.info("SMTP server connection closed.")