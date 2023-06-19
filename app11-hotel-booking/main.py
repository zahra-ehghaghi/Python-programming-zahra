import  pandas as pd

df = pd.read_csv("hotels.csv",dtype={"id":str})
df_card = pd.read_csv("cards.csv",dtype=str).to_dict(orient="records")
df_secure_card = pd.read_csv("card_security.csv",dtype=str)



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
class CreditCard():
    def __init__(self,card_number):
        self.card_number = card_number

    def validate(self,expiration, holder, csv):
        card = {"number":self.card_number,"expiration":expiration,"cvc":csv,"holder":holder}
        print(card)
        if card in df_card:
            return True
        else:
            return False

class SecureCreditCard(CreditCard):
    def authenticate(self,given_passwoed):
        password = df_secure_card.loc[df_secure_card["number"]== self.card_number,"password"].squeeze()
        if password == given_passwoed:
            return True
        else:
            return  False

print(df)
hotel_ID = input("Enter the id of the hotel:")
print(hotel_ID)
hotel = Hotel(hotel_ID)
if  hotel.available():
    creditcard  = SecureCreditCard("1234567890123456")
    if creditcard.validate(expiration="12/26", holder="JOHN SMITH", csv="123"):
        if creditcard.authenticate("mypass"):
            hotel.book()
            name = input("Enter your name:")
            reservation_ticket = ReservationTicket(name,hotel)
            print(reservation_ticket.generate())
        else:
            print("CreditCard authentication failed")
    else:
        print("CreditCard is not available")
else:
   print("hotel is not free")

