day=input("enter the day")
menu=input("enter the menu")
if day=="monday":
    if menu=="breakfast":
        print("maggi")
    elif menu=="lunch":
        print("roti")
    elif menu=="dinner":
        print("sabji and chawal")
elif day=="tuesday":
    if menu=="breakfast":
        print("halwa")
    elif menu=="lunch":
        print("chapati")
    elif menu=="dinner":
        print("pavbhaji")
elif day=="wednesday":
    if menu=="breakfast":
        print("poha")
    elif menu=="lunch":
        print("dosa")
    elif menu=="dinner":
        print("biryani")
elif day=="thursday":
    if menu=="breakfast":
        print("tea")
    elif menu=="lunch":
        print("daliya")
    elif menu=="dinner":
        print("khichadi")
else:
    print(" nothing")