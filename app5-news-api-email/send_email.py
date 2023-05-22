import  smtplib
import ssl


def send_email(message):
    username = "z.ehghaghi@gmail.com"
    password = "kenkxjzrnbjoxvuv"
    host = "smtp.gmail.com"
    port = 465
    reciever = username
#     message = """\
# Subject: Hi
# How are you?
# But!!
# """
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)

if __name__ == "__main__":
    send_email()

