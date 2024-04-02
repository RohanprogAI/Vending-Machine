import sys

print("Welcome to Vending Machine\n")

print("Drinks available:")
print("1 : Coke: RM 3")
print("2 : Mountain Dew: RM 3")
print("3 : Pepsi: RM 3")
print("4 : Nescafe: RM 4")
print("5: Wonda Coffee: RM 4")
print("6: Iced Milo: RM 4")
print("7: Bubble Tea: RM 6\n")


drink_Choice = input("Select the respective number for the drink : ")


def get_price(drink):
    prices ={
        "1": 3,
        "2": 3,
        "3": 3,
        "4": 4,
        "5": 4,
        "6": 4,
        "7": 6
    }
    

    price = prices.get(drink)
    if price is None:
        print("No such drink")
        return None
    return price



tot_Price = get_price(drink_Choice)

if tot_Price is None:

    #exit()
    sys.exit("No such drink")

#print("Drinks price:", tot_Price)

pay_Amount = int(input("Enter the paying amount : "))

def pay_Amnt(Amt, tot_Price):
    if(Amt >= tot_Price):
        balance = Amt - tot_Price
        return balance
        
    else :
        print("Insufficient amount")
        sys.exit("Insufficient amount")
        #exit("Insufficient amount")
        return None

   
        

bal_Amount = pay_Amnt(pay_Amount, tot_Price)






if bal_Amount is not None:
    print("Balance:", bal_Amount)

    def notes_pieces(change):
        notes = [100, 50, 20, 10, 5, 1]

        for note in notes:
            count = change // note

            
            if count > 0:
                print(count, "x", "RM", note)
                change = change- count * note
        
            if change == 0:
                print("No change to give.")
                return

            
          

        

    notes_pieces(bal_Amount)

