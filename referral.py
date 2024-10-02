import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import base64

# Set your email and password
sender_email = "markandrew8435@gmail.com"
sender_password = "fkffvubojfuuptkw"
attachment_path = "D:/Downloads/Mark - Andrew.pdf"    #backend
# attachment_path = "D:/Mark_Andrew.pdf" #mobile

# File to keep track of sent emails
sent_file = "referral.txt"
job_url = input("job_url")

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

    def send_email(self, sender_email, sender_password, recipients, subject, name, attachment_path):
        recipient = recipients[0]
        if recipient in self.sent_recipients:
            print(f"Email already sent to {recipient}")
            return
        # Create the MIME object
        message = MIMEMultipart()
        message["From"] = sender_email
        message["Subject"] = subject

        # Add body text to the email
        body = f"""Hi,
I’m Mark Andrew a B.tech IT graduate from IIIT Lucknow 2023,
Since my Knowledge in Data Structures and Algorithms, and my 1yr+ experience in Software Development aligns with the requirements at your company, therefore I’d like you to refere me 
Notice period : 0 days
{"job url: " + job_url if len(job_url)>0 else ""} 

Regards,
Mark Andrew
+918435720545"""

        # # do checkout the app I've published on PlayStore :
        # # https://www.google.com/url?q=https://play.google.com/store/apps/details?id%3Dtech.maryandrew.mangacolorizer

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
recipient_names = "Saiesh Kaul, Karan Bhandari, Yash Gagneja, Vishakha Rathore, Shuvanshu Gupta, Rohit Kumar Singh, Ankur Ojha, Ishan Gupta, Somu Kumar, Adarsh Baranwal, Deepak Joshi, Chetanya Gupta, Ashi Srivastava, PRAVEEN BABU . M, Himanshu Pandey (he/him), Ravdeep Singh, Imran Ahmad ✅, Baljeet Malik, Divanshu Kapoor, Aditya Kumar, Deepak Tiwary, Sibasish Subhadarshee, Uday Prasad, Vandita Pandey, Amrit Pal Singh, Tanmay Awasthi, Siddharth Sanghvi, Rajeshkumar S, Aditya Roshan, Ranit Dey, Monty Verma, Rishabh Joshi, Yash Sharma, Sanath Salil, Kumar Ankit, Pavithra Hegde, Bubesh P, Harsh Mani Tripathi, Aman Kumar Sharma, Samriddhi Srivastava, Udaya Yadav, Sajan Grover, Mayank Jain, prachi agrawal, Ragavendra S., Srinandan D Pai, Pratik Agarwal, M Jeffin Manuel, Vikas BG, Goldi Saini, Piyus Rout, Ram Choudhary, Deepak K., Afroz Alam, Himanshu Jain, Pritam Nayak, Srinivas A, Deepak Brahmania, Hariom Sharma, Faizan Khan, Shril Kumar, Sauvik Samanta, Aakash Suman, Vishnu Satheesan, Vibus Krishnan, Krishna Shetty, Vidya Adavalli, Lakshay Gogia, Naveenkumar S., Shubham Kumar, Sridhar V., Karthick Jayakumar, Ankur Singh, Ayush Khanduri, Manjunath B, C Piyush Parimal, Gaurav Pahwa, Niveditha Ram, Rajan Mishra, Pratyush Raizada, Harendra Kumar, Shivam Pandey, Gopakumar k, Shankar Golla, Wajahat Siddiqui, Sandesh Pandey, Kushal Katara, Zubair Ali Khan, Sahil Kukreja, Akhilesh Yede, Abhishek Kumar, Vaibhav Arora, Bhargav Khamar, Leninkarthik v, Aishwary Kumar Jain, Ramya J, Akshat Trivedi, Nirajkumar Shelke, Vijayamoorthy R, Akash Kedia, Ashwin Krishna, Muthukumar Lakshmanan, Thanikaivelan Maruthai, Rajeev Rathore, ABHISHEK GUPTA, Barnali Basu, LinkedIn Member, Abhishek Kumar, SIBANI PRASAD DASH, Arpit Singhal, Saket Thapliyal, Bhawani Singh, Arpit J., Sudhanshu Pandey, Ravi Kumar, Prashant Ranade, Agnideep Bagchi, Mahesh Chandak, Rohit Jain, Harsh Sachan, Ashwani Dwivedi, khushboo srivastava, Rajesh Kumar D., arjun tomar, Saurav Sneh, Malathy Natarajan, Bijendra singh, LinkedIn Member, Deepesh Mathew, LinkedIn Member, Nithish Veeravalli, Sunil Chohan, LinkedIn Member, LinkedIn Member, Vikas Bisht, LinkedIn Member, Prakash S, Bhaskar Mondal, Maneesh K., LinkedIn Member, Ashrut Bhatia, Ravinder Singh, Ankur Goyal, LinkedIn Member, Arivoli MV, shivam jha, Rakesh Haridas, LinkedIn Member, Deepika Mohan, LinkedIn Member, Bharath Valluru, LinkedIn Member, LinkedIn Member, Sandhya A., LinkedIn Member, Rajesh Ramakrishnan, Ayush Mishra, Prem Kumar, Sandeep B K, LinkedIn Member, LinkedIn Member, Harini Krishnamoorthy, Swetha Kanavi, Chandan Parameswaraiah, Nikash R., Deepak Mahato, LinkedIn Member, LinkedIn Member, LinkedIn Member, LinkedIn Member, LinkedIn Member, Shovon Bhattacharya, vijay vinoth chandra sekaran, LinkedIn Member, Gurunath Kumbar, Mimansa Shukla, Suresh Ramanaiah, LinkedIn Member, Letitia Romina, Mohamed Zulkifl, Gowtham san San, LinkedIn Member, LinkedIn Member, LinkedIn Member, mohan kumar, LinkedIn Member, LinkedIn Member, LinkedIn Member, LinkedIn Member, Bala Chandru, Prem Kumar, LinkedIn Member, LinkedIn Member, LinkedIn Member".split(
    ",")

# recipient_names = ["Mark Andrew"]
role = input("interested to work as")
# Set the email subject, body, and attachment path
email_subject = f"Interested to work as {role}"

# Send the email to each recipient in the l
# ist with attachment
if __name__ == '__main__':
    domain = input("domain:")
    automail = AutoMail()
    for i in recipient_names:
        j = i
        for s in j:
            if not (s.isalnum() or s == ' '):
                j = j.replace(s, '')
        a = j.split()
        if len(a) < 2:
            a.append('')

        f_name, l_name = a[0], a[-1]
        for recipient in [
            f"{f_name}.{l_name}@{domain}".replace("..", ""),
            f"{l_name}.{f_name}@{domain}".replace("..", ""),
            f"{f_name}@{domain}".replace("..", ""),
            f"{l_name}@{domain}".replace("..", ""),

        ]:
            recipient = recipient.strip().lower()
            automail.send_email(sender_email, sender_password, [recipient], email_subject, i, attachment_path)

# automail = AutoMail()
#
#
# def sendMail(recipient):
#     automail.send_email(sender_email, sender_password, [recipient.lower().strip()], email_subject, email_body,
#                         attachment_path)
