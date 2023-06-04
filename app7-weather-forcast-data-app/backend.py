import requests
API_KEY="2dad7640080366d5dac562c6a39608d2"
def get_date(city,forcatdays=None,kind=None):
    url=f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"
    data= requests.get(url).json()
    filter_date= data["list"]
    nr_values= 8* forcatdays
    filter_date=filter_date[:nr_values]
    if kind=="Temperature":
        filter_date=[dict["main"]["temp"] for dict in filter_date]
    if kind == "Sky":
        filter_date = [dict["weather"][0]["main"] for dict in filter_date]
    return filter_date

if __name__== "__main__":
    print(get_date(city="Tokyo"))