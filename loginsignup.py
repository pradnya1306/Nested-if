print("*****WELCOME TO LONGIN SINGUP PAGE****")
name="pradnya"
password="pra@123"
user_name=input("enter the name : ")
user_password=input("enter the number : ")
if user_name==name:
    if user_password==password:
        print("login sucessfully")
    else:
        print("user password is worng")
elif (user_name!=name and user_password!=password):
    print("both are wrong")
    print("creat new account")
    user1=input("Enter your name : ")
    user2=int(input("Enter your number : "))
    print("your new account is successfully created ")
else:
    print("user name is worng")