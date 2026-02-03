#Your code goes here
def main():

    
    money = int(input("please pay £0.75: "))
    p = 75
    while money != 75:
        ammount_due = p - money
        
        if ammount_due >= 0 :
            print (ammount_due , " is due")
            
main()