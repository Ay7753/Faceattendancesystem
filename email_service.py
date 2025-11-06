import os
import aiosmtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import toml  # used to read .toml files


load_dotenv()

async def send_email(to_email: str, subject: str, body: str):
    msg = MIMEText(body)
    msg["From"] = os.getenv("SMTP_USER")
    msg["To"] = to_email
    msg["Subject"] = subject

    await aiosmtplib.send(
        msg,
        hostname=os.getenv("SMTP_HOST"),
        port=int(os.getenv("SMTP_PORT")),
        start_tls=True,
        username=os.getenv("SMTP_USER"),
        password=os.getenv("SMTP_PASS")
    )
