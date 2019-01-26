import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(fm_entry,tm_entry,s_entry,c_entry,p_entry ):

    message = MIMEMultipart()
    message['From'] = fm_entry
    message['To'] = tm_entry
    message['Subject'] = s_entry

    message.attach(MIMEText(c_entry, 'plain'))
    text = message.as_string()
    mail = smtplib.SMTP('smtp.gmail.com',587)
    #mail.ehlo()
    mail.starttls()
    mail.login(fm_entry,p_entry)
    mail.sendmail(fm_entry, tm_entry, text)
    mail.close()
