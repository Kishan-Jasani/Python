# --> Let us consider a scenario where a customer can have many credit cards which he can use for purchasing. 
# --> Each credit card has a number and a balance.
# --> Let us consider a purchase_item() method which takes the price of the item and card number as an input. 
# --> In case price is invalid or price is beyond the credit card balance, 
# --> we can transfer the control to an except block by raising an exception. 
# --> In Python, we can raise exception by using the raise keyword.


lass InvalidPrice(Exception):
    pass
class WrongCard(Exception):
    pass
class CreditCard:
    def __init__(self, card_no, balance):
        self.card_no=card_no
        self.balance=balance
class Customer:
    def __init__(self,cards):
        self.cards=cards
    def purchase_item(self,price,card_no):
        if price < 0:
            raise InvalidPrice("The price is wrong")
        if card_no not in self.cards:
            raise WrongCard("Card is invalid")
        if price>self.cards[card_no].balance:
            raise WrongCard("Card has insufficient balance")
card1=CreditCard(101,800)
card2=CreditCard(102,2000)
cards={card1.card_no:card1,card2.card_no:card2}
c=Customer(cards)
while(True):
    card_no=int(input("Please enter a card number"))
    try:
        c.purchase_item(1200,card_no)
        break
    except InvalidPrice as e:
        print(str(e))
        break
    except WrongCard as e:
        print(str(e))
        continue
    except Exception as e:
        print("Something went wrong. "+str(e))
        
        
        
#Order of except:-
try:
    1/0             #This should raise Zero Division error.
except Exception:
    print("Exception")  #According to order this general exception comes before Zero Division Error. So this will print.
except ZeroDivisionError:
    print("Zero division")
