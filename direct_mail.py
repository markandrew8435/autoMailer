import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import base64

# Input job role and job URL
job_role = input("interested to work as ")
job_url = input("Job URL: ")

# Set the email subject, body, and attachment path
email_subject = f"Interested to work as a {job_role}"
email_body = f"""Hi,
I’m Mark Andrew, a B.Tech IT graduate from IIIT Lucknow (2023).
Since my knowledge in Data Structures and Algorithms, and my 1+ years of experience in Software Development aligns with the requirements at your company, I’d like you to consider my application.
Notice period: 0 days
{"Job: "+ job_url if len(job_url.strip())>0 else ""}
Best Regards,
Mark Andrew
+918435720545"""
attachment_path = "D:/Downloads/Mark - Andrew.pdf"    #backend
# attachment_path = "D:/Mark_Andrew.pdf" #mobile

# Define sender's email credentials
sender_email = "markandrew8435@gmail.com"
sender_password = "fkffvubojfuuptkw"

# Recipients' emails
recipient_emails = "shristi.singh@zyoin.com".split(',')
recipient_emails = set([x.strip().lower() for x in recipient_emails])

def send_email(sender_email, sender_password, recipient_email, subject, body, attachment_path):
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = "Mark Andrew"
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # Open the file in binary mode
    with open(attachment_path, "rb") as attachment:
        # Add the attachment to the message
        part = MIMEApplication(attachment.read(), Name=os.path.basename(attachment_path))
        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
        msg.attach(part)

    # Connect to Gmail's SMTP server
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(sender_email, sender_password)  # Login with sender's credentials
        text = msg.as_string()  # Convert the message to a string format
        server.sendmail(sender_email, recipient_email, text)  # Send the email
        server.quit()
        print(f"Email sent successfully to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}. Error: {str(e)}")

if __name__ == '__main__':
    for recipient in recipient_emails:
        send_email(sender_email, sender_password, recipient.strip().lower(), email_subject, email_body, attachment_path)
