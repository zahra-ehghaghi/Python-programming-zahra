import smtplib
import ssl
import time

import  requests
import selectorlib
import  sqlite3


URL="http://programmer100.pythonanywhere.com/tours/"

class Event:
    def scraping(self,url):
        response = requests.get(url)
        content = response.text
        return  content
    def extracting(self,source):
        extractor =  selectorlib.Extractor.from_yaml_file("extract.yaml")
        value = extractor.extract(source)["tours"]
        return  value

class Email:
    def send(self,message):
        username = "z.ehghaghi@gmail.com"
        password = "kenkxjzrnbjoxvuv"
        host = "smtp.gmail.com"
        port = 465
        reciever = username
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, reciever, message)


class Database:

    def __init__(self,database_url):
        self.connection = sqlite3.connect(database_url)

    def store(self,extracted):

        row = extracted.split(",")
        row=[item.strip() for item in row]
        cursor =self.connection.cursor()
        cursor.execute("insert into events values(?,?,?)",row)
        self.connection.commit()



    def read(self,extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]
        band, city,date = row
        cursor = self.connection.cursor()
        sql="SELECT * FROM events where band = ? and city = ? and date = ?"
        row = cursor.execute(sql,(band,city,date)).fetchall()
        #print(row)
        return  row

if __name__ == "__main__":
    while True:
       event = Event()
       scrap =  event.scraping(URL)
       extracted = event.extracting(scrap)
       print(extracted)

       if extracted !='No upcoming tours':
           databse = Database("data.db")
           row = databse.read(extracted)
           if not row:
               databse.store(extracted)
               email =Email()
               email.send(message="Hey new event was found")
       time.sleep(2)

