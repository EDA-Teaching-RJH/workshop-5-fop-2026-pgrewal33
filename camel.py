# Enter your code here
def main():

    camel = input(" write a sentence in camel case: ")
    camel_ = ''.join(['_' + char.lower() if char.isupper() else char for char in camel])
    
    snake = camel_.lower()
            
    
    print (snake)
main()