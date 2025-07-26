import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ======== CONFIGURATION ========
EMAIL_ADDRESS = "omwegajoseph01@gmail.com"
EMAIL_PASSWORD = "fioxrwymexppvvoq"
TO_EMAIL = "omwegajoseph01@gmail.com"  

# ======== DATE CHECKING ========
today = datetime.date.today()

# Calculate last day of this month
if today.month == 12:
    last_day = datetime.date(today.year, 12, 31)
else:
    next_month = datetime.date(today.year, today.month + 1, 1)
    last_day = next_month - datetime.timedelta(days=1)

# Check if today is 7 days before end of the month
reminder_day = last_day - datetime.timedelta(days=7)

if today == reminder_day:
    # ======== CREATE EMAIL ========
    subject = "Rent Reminder"
    body = f"""Hello,

This is a friendly reminder that your rent is due soon — in 7 days (on {last_day.strftime('%B %d')}).

Please make sure to pay your rent on time.

Thanks!
- Your Python Script 
"""

    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # ======== SEND EMAIL ========
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, TO_EMAIL, msg.as_string())
        server.quit()
        print("Rent reminder sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")
else:
    print(f"Today is {today}. Rent reminder will be sent on {reminder_day}.")