import smtplib
import ssl
import time

import  requests
import selectorlib
import  sqlite3


URL="http://programmer100.pythonanywhere.com/tours/"


connection = sqlite3.connect("data.db")





def scraping(url):
    response = requests.get(url)
    content = response.text
    return  content

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


def extracting(source):
    extractor =  selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return  value





def store(extracted):

    row = extracted.split(",")
    row=[item.strip() for item in row]
    cursor =connection.cursor()
    cursor.execute("insert into events values(?,?,?)",row)
    connection.commit()



def read(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band, city,date = row
    cursor = connection.cursor()
    sql="SELECT * FROM events where band = ? and city = ? and date = ?"
    row = cursor.execute(sql,(band,city,date)).fetchall()
    #print(row)
    return  row

if __name__ == "__main__":
    while True:
       scrap =  scraping(URL)
       extracted = extracting(scrap)
       print(extracted)

       if extracted !='No upcoming tours':
           row = read(extracted)
           if not row:
               store(extracted)
              # send_email(message="Hey new event was found")
       time.sleep(2)

