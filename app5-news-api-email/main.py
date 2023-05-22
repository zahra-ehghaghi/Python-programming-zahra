import requests

from send_email import send_email

apikey="5aae834347ea42eaa2cc7ff5aa3a196d"
url=f"https://newsapi.org/v2/everything?q=tesla&from=2023-04-22&sortBy=publishedAt&apiKey={apikey}"
request = requests.get(url)
content = request.json()
body=""
for item in content["articles"]:
   if item['title'] is not None:
      body = body + item['title'] +"\n"+item['description'] + 2*"\n"

print(body)
body= body.encode("utf-8")
send_email(body)
print("ok")
