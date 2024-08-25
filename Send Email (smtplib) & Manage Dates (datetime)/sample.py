import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(subject_, message_, to_email_):
    # Your email credentials
    sender_email = "pyth128@gmaill.com"
    sender_password = "N7G!xYWYXC7kmbY"

    # Email server configuration (Gmail example)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create a message object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email_
    msg['Subject'] = subject_

    # Attach the message to the email
    msg.attach(MIMEText(message_, 'plain'))

    try:
        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # Start TLS for security
            server.starttls()

            # Login to the email account
            server.login(sender_email, sender_password)

            # Send the email
            server.sendmail(sender_email, to_email_, msg.as_string())

        print("Email sent successfully!")

    except Exception as e:
        print(f"Error: {e}")


# Example usage
subject = "Hello, this is the subject"
message = "Hello, this is the body of the email."
to_email = "pythsec650@gmail.com"

send_email(subject, message, to_email)
