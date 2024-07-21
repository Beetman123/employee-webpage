import smtplib
import ssl

def send_email(user_email, topic, message):
    host = "smtp.gmail.com"
    port = 465
    username = "jaedanparsons@gmail.com"
    password = "ntqxepzrkmuolnrq"

    context = ssl.create_default_context()

    '''
        message = f"""\
    Subject: Message from employee page app 
    
    From: {user_email}
    Topic: {topic}
    Message:
    {raw_message}"""
    '''

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, user_email, message)