import requests

from send_email import send_email

apikey="5aae834347ea42eaa2cc7ff5aa3a196d"
url=f"https://newsapi.org/v2/everything?q=tesla&from=2023-04-22&sortBy=publishedAt&apiKey={apikey}"
request = requests.get(url)
content = request.json()

for item in content["articles"]:
 print(item['title'])
 print(item['description'])