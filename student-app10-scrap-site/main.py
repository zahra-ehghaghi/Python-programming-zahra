import requests
import selectorlib
import  ssl
import  smtplib
import sqlite3
from datetime import  datetime

URL="http://programmer100.pythonanywhere.com/"
connection = sqlite3.connect("temperature.db")
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


def write(extracted):
    now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    sql = "insert into Temperatures values(?,?)"
    cursor = connection.cursor()
    cursor.execute(sql,(extracted,now))
    connection.commit()


if __name__ == "__main__":
    scrapped = scraping(URL)
    extracted = extracting(scrapped)
    write(extracted)
    print(extracted)
    print(read())
