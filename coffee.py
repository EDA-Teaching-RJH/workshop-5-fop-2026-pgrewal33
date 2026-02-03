#Your code goes here
def main():
    
    total_paid = 0
    ammount_due = 75

    while total_paid < ammount_due:
        coin = int(input("please input a coin: "))
        
        if coin in [50,20,10,5]:
           total_paid += coin
        if total_paid < ammount_due:
            print(f"ammount due: {ammount_due - total_paid}p")

    change = total_paid - ammount_due

    if change > 0:
        print(f"change owed: {change}p")

    else:
        print("thank you for paying")
            
main()