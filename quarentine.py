print("welcome to navgurukul")
name=input("what is your name : ")
incharge=input("have you covid report : ")
if incharge=='yes':
    state=input("which state form you?: ")
    if state=='maharashtra':
        print("7 day quarentine")
        print("kichen turn wii be after 4 days")
        day1=input("enter your day : ")
        if day1=="monday:":
            print("chawal and sabji")
        elif day1=="tuesday":
            print("kadhi vada")
        elif day1=="wednesday":
            print("vada")
        elif day1=="thursday":
            print("samosa and chatni")
    else:
        print("14 days quarentine")
        print("kichen turn wii be after 5 days")
        day=input("enter your day : ")
        if day=="monday":
            print("roti and sabji")
        elif day=="tuesday":
            print("halwa")
        elif day=="wednesday":
            print("pavbhaji")
        elif day=="thursday":
            print("misal pav")
else:
    print("you have to go to hospital")
    print("do your covid test")
    report=input("what about your report : ")
    if report=='positive':
        print("you should admit into hospital")
    else:
        print("welcome to navgurukul")