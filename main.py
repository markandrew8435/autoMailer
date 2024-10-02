import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import base64

# Set your email and password
sender_email = "markandrew8435@gmail.com"
sender_password = "fkffvubojfuuptkw"
attachment_path = "D:/Downloads/Mark - Andrew.pdf"
# attachment_path = "D:/Mark_Andrew.pdf" #mobile


# File to keep track of sent emails
sent_file = "sent.txt"
def read_sent_file(sent_file):
    if os.path.exists(sent_file):
        with open(sent_file, "r") as file:
            return set(line.strip() for line in file)
    return set()

def write_sent_file(sent_file, recipient):
    with open(sent_file, "a") as file:
        file.write(recipient + "\n")

class AutoMail:
    def __init__(self):
        self.sent_recipients = read_sent_file(sent_file)


    def send_email(self, sender_email, sender_password, recipients, subject, body, attachment_path):
        recipient = recipients[0]
        if recipient in self.sent_recipients:
            print(f"Email already sent to {recipient}")
            return
        # Create the MIME object
        message = MIMEMultipart()
        message["From"] = sender_email
        message["Subject"] = subject

        # Add body text to the email
        message.attach(MIMEText(body, "plain"))

        # Attach the file with its original name
        attachment_filename = os.path.basename(attachment_path)
        with open(attachment_path, "rb") as attachment:
            part = MIMEApplication(attachment.read(), Name=attachment_filename)
            part['Content-Disposition'] = f'attachment; filename="{attachment_filename}"'
            message.attach(part)

        # Establish a connection with the SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            # Start TLS for security
            server.starttls()

            # Login to your email account
            server.login(sender_email, sender_password)

            # Send the email to each recipient in the list
            for recipient in recipients:
                print(recipient)
                message["To"] = recipient
                server.sendmail(sender_email, recipient, message.as_string())
                print(f"Email with attachment sent successfully to {recipient}")
                write_sent_file(sent_file, recipient)
                self.sent_recipients.add(recipient)

# Set the list of recipients
recipient_emails = "".split(",")

# Set the email subject, body, and attachment path
email_subject = "Interested to work as Springboot Developer"
email_body = """Hi,
I’m Mark Andrew a B.tech IT graduate from IIIT Lucknow 2023,
Since my Knowledge in Data Structures and Algorithms, and my 1yr+ experience in Software Development aligns with the requirements at your company, therefore I’d like you to consider my application
Notice period : 0 days
current ctc: 9.5 LPA

Regards,
Mark Andrew
+918435720545"""
# Send the email to each recipient in the l
# ist with attachment
if __name__=='__main__':
    for i in recipient_emails:
        recipient = i.strip().lower()
        AutoMail().send_email(sender_email, sender_password, [recipient], email_subject, email_body, attachment_path)

automail = AutoMail()
def sendMail(recipient):
    automail.send_email(sender_email, sender_password, [recipient.lower().strip()], email_subject, email_body, attachment_path)
    


