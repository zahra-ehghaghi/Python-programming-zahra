import smtplib
import ssl
import  requests
import selectorlib


URL="http://programmer100.pythonanywhere.com/tours/"


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
   with open("data.txt","a") as file:
       file.write(extracted+"\n")

def  read():
   with open("data.txt","r") as file:
       return  file.read()


if __name__ == "__main__":
   scrap =  scraping(URL)
   extract = extracting(scrap)
   if extract !='No upcoming tours':
       data = read()
       if extract not in data:
           store(extract)
           send_email(message="Hey new event was found")
   print(extract)
