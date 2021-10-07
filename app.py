import smtplib
from email.message import EmailMessage

print(f' *'*40,'\n',' *'*15, 'PYTHON GMAIL BOT',' *'*15,'\n',' *'*40)

email_address = str(input('Enter your email address: '))
email_password = str(input('Enter your password: '))

message_to_send = EmailMessage()

message_to_send['Subject'] = str(input('Write the subject of your message: '))
message_to_send['From'] = email_address
message_to_send['To'] = str(input('Write the email addres you want to send this message: '))
message_to_send.set_content(str(input('Write the content of your message: ')))

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_address, email_password)
    smtp.send_message(message_to_send)