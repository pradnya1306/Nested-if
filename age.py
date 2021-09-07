age=int(input("enter the age : "))
if age>=18:
    collage=input("collage jata hai : ")
    if collage=="yes":
        collagename=input("enter the collage name : ")
        field=input("which field ?:")
        print(" you will get job : ")
        if field=="maths":
            print("after two year")
        elif field=="science":
            print("after three year")
        elif field=="commerce":
            print("after four year")
        elif field=="art":
            print("after five year")
        else:
            print(" nothing")
    elif collage=="no":
        marriage=input("are you married ? ")
        if marriage=="yes":
            marriage1=input("love marriage or arrange marriage ? :")
            if marriage1=="love marriage":
                lovemarriage=input("temple or court")
                if lovemarriage=="temple":
                    print("god bless you")
                elif lovemarriage=="court":
                    print("friend cricle")
            elif marriage1=="arrange marriage":
                print("happy ending")
            else:
                print("nothing")
        else:
            print("nothing")
elif age<18:
    school=input("school jata hai ya nahi")
    if school=="yes":
        schoolage=int(input("enter the age"))
        if schoolage<10:
           print("good")
        else:
            subject=input("which subject")
            sub1=("history,hindi,marathi,english")
            if subject=='history'or'hindi'or'marathi'or'english':
                print("its nice field")
            else:
                print("its bad")
    else:
        print("do your study")
else:
    print("nothing")

       

