import  pandas as pd

df = pd.read_csv("hotels.csv",dtype={"id":str})



class Hotel:

  def __init__(self,hotel_id):
    self.hotel_id = hotel_id
    self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()



  def book(self):
    df.loc[df["id"] == self.hotel_id, "available"] = "no"
    df.to_csv("hotels.csv",index=False)

  def available(self):
    availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
    if availability == "yes":
      return  True
    else:
      return False

class ReservationTicket:

  def __init__(self,customer_name,hotel_object):
    self.customer_name=customer_name
    self.hotel_object =hotel_object


  def generate(self):
    content = f"""
    Thanks you for your reservation!
    Here are you booking  data:
    Name: {self.customer_name}
    Hotel Name  {self.hotel_object.name}
"""
    return content

print(df)
hotel_ID = input("Enter the id of the hotel:")
print(hotel_ID)
hotel = Hotel(hotel_ID)
if  hotel.available():
   hotel.book()
   name = input("Enter your name:")
   reservation_ticket = ReservationTicket(name,hotel)
   print(reservation_ticket.generate())
else:
   print("hotel is not free")

