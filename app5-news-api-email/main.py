import requests

from send_email import send_email
keysearch= "tesla"
apikey="5aae834347ea42eaa2cc7ff5aa3a196d"
url=f"https://newsapi.org/v2/everything?q={keysearch}&from=2023-04-22&sortBy=publishedAt&apiKey={apikey}&language=en"
request = requests.get(url)
content = request.json()

body="Subject:New NewsLetter Email \n"
for item in content["articles"][:20]:
    if item['title'] is not None:
       body = body + item['title'] +"\n"+item['description'] + "\n" + item['url']+ 2*"\n"

print(body)
body= body.encode("utf-8")
send_email(body)
print("ok")
