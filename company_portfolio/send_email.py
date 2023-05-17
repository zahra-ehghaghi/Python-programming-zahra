import  smtplib as smtp
import  ssl
def send_email(message):
    host = "smtp.gmail.com"
    port=465
    user="z.ehghaghi@gmail.com"
    password="kenkxjzrnbjoxvuv"
    reciever = user
    context = ssl.create_default_context()
    with smtp.SMTP_SSL(host, port, context=context) as server:
        server.login(user,password)
        server.sendmail(user,reciever,message)