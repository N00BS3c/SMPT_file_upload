import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import argparse
import os

def send_email(smtp_server, smtp_port, username, password, to_email, subject, body, file_path=None):
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    # Attach the file if provided
    if file_path and os.path.isfile(file_path):
        with open(file_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file_path)}')
            msg.attach(part)

    # Connect to the server and send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # Omit the following line if the server does not support STARTTLS
            # server.starttls()  
            server.login(username, password)
            server.send_message(msg)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Send an email via SMTP with optional file attachment.')
    parser.add_argument('--smtp_server', required=True, help='SMTP server address')
    parser.add_argument('--smtp_port', type=int, required=True, help='SMTP server port')
    parser.add_argument('--username', required=True, help='Email username')
    parser.add_argument('--password', required=True, help='Email password')
    parser.add_argument('--to_email', required=True, help='Recipient email address')
    parser.add_argument('--subject', required=True, help='Email subject')
    parser.add_argument('--body', required=True, help='Email body')
    parser.add_argument('--file', help='Path to file to attach')

    args = parser.parse_args()

    send_email(
        smtp_server=args.smtp_server,
        smtp_port=args.smtp_port,
        username=args.username,
        password=args.password,
        to_email=args.to_email,
        subject=args.subject,
        body=args.body,
        file_path=args.file
    )
