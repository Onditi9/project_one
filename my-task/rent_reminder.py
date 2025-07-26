import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ========= CONFIGURATION VARIABLES =========

# Your email credentials
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "ghqtqjfroxecjeqf"


RECIPIENTS = ["your_email@gmail.com"] # 01otienokennedy@gmiail.com # alexelijah200@gmail.com

# Reminder settings
RENT_REMINDER_DAY = 26  # Day of the month to send reminder
SUBJECT = "Rent Reminder"
SENDER_NAME = "Rent Notifier Bot"

# ========= CHECK DATE =========

today = datetime.date.today()

if today.day == RENT_REMINDER_DAY:
    # Dynamic message body
    body = f"""
Hi,

This is a reminder that today is the 26th — your rent is due.

Please make sure to pay your rent on time.

Thanks,  
{SENDER_NAME}
"""

    # ========= EMAIL CONSTRUCTION =========
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = ", ".join(RECIPIENTS)
    msg["Subject"] = SUBJECT
    msg.attach(MIMEText(body, "plain"))

    # ========= EMAIL SENDING =========
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECIPIENTS, msg.as_string())
        server.quit()
        print("Rent reminder sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
else:
    print(f"Today is {today}. Rent reminder will only be sent on the 26th.")