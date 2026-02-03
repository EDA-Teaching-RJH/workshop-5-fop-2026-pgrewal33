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

def calculate_change(change_ammount):
    coins = [50, 20, 10, 5]
    change_coins = []

    for coin in coins:
          while change_ammount >= coin:
               change_coins.append(coin)
               change_ammount -= coin
    return change_coins

def dispense_product(ammount_due):
    if ammount_due < 0:
            change_ammount = abs(ammount_due)
            change_coins = calculate_change(change_ammount)
          
            if len(change_coins) == 0:
               change_message = "no change"
            
            elif len(change_coins) == 1:
                 change_message = f"returning: {change_coins[0]}"

            else:
                coins_str = ", ".join([f"{coin}p" for coin in change_coins[:-1]])
                coins_str += f" and {change_coins[-1]}p"
                change_message = f"Returning: {coins_str}"
            
            print(change_message)

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