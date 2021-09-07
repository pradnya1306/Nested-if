
print("****welcome in SBI ATM****")
print(("insert your card"))
language=input("enter your language  : ")
if language=="english"or"hindi":
    pin=int(input("please enter your pin : "))
    print("please wait....\ncheck your pin")
    a=1234
    saving_balance=50000
    current_balance=4000
    credit_card=100000
    if a==pin:
        print (" your pin is correct ")
        transaction=input("select transaction :"  )
        if transaction=="cash withdrawl":
            amount=int(input("enter your amount"))
            account=input("select your account : ")
            if account=="saving":
                print("confirm")
                print("transaction in progress")
                print("take your money")
                rebal=saving_balance-amount
                print("avilable balance is", rebal)
                receipt=input("do you want receipt? : ")
            elif account=="current account":
                print("confirm")
                print("transaction in progress")
                print("take your money")
                rebal1=current_balance-amount
                print("available balance is Rs.", rebal1)
                receipt=input("do you want receipt? : ")
            elif account=="credit card":
                print("confirm")
                print("transaction in progress")
                print("take your money")
                rebal2=credit_card-amount
                print("avilable balance is",rebal2)
                receipt=input("do you want receipt? : ")
            else:
                print("invalid account")
        
        elif transaction=="balance enquiry":
            account=input("select your account : ")
            if account=="saving":
                print("Available balance is", saving_balance)
                print("thank you for using SBI ATM")
                receipt=input("do you want receipt? : ")
            elif account=="current account":
                print("Available balance is", current_balance)
                print("thank you for using SBI ATM")
                receipt=input("do you want receipt? : ")
        elif transaction=="change pin number":
            newpin=int(input("please enter new pin : "))
            newpin1=int(input("please re-enter your pin : "))
            print("transaction complete")
            print("please take your card")
    else:
        print("wrong your pin number")
else:
    print("thank you")

