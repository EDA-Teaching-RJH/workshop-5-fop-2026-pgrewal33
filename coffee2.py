
def get_coin():
        valid = False
        while not valid:
            try:
                coin = int(input("please input a coin: "))
        
                if coin in [50,20,10,5]:
                    valid = True
                    return coin
            
                else:
                    print("invalid input")
            except ValueError:
                print("invalid input")



def update_total(ammount_due, coin):
        ammount_due -= coin
        return ammount_due

def dispense_product(ammount_due):
     if ammount_due < 0:
          change = abs(ammount_due)
          print(f"change owed: {change}p")
print("thank you for paying")

def main():
    ammount_due = 75
    while ammount_due > 0:
        
        coin = get_coin()
        
        ammount_due = update_total(ammount_due, coin)

        if ammount_due > 0:
            print(f"ammount due: {ammount_due}p")
    
    dispense_product(ammount_due)

main()