import requests
import selectorlib
import  ssl
import  smtplib
from datetime import  datetime

URL="http://programmer100.pythonanywhere.com/"

def scraping(url):
    response = requests.get(url)
    return  response.text

def extracting(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    extracted = extractor.extract(source)["tours"]
    return  extracted


def send_email(message):
    username = "z.ehghaghi@gmail.com"
    password = "kenkxjzrnbjoxvuv"
    host = "smtp.gmail.com"
    port = 465
    reciever = username
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)


def write(contect):
    now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    with open("data.txt","a") as file:
        file.write(f"{now},{contect}\n")
def read():
    with open("data.txt","r") as file:
        file.read()

if __name__ == "__main__":
    scrapped = scraping(URL)
    extracted = extracting(scrapped)
    write(extracted)
    print(extracted)

