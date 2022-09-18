################# BREAKFAST TIME  MENU CARD ######################
menucard_breakfast=["idli","dosa","pongal","appam","vada","set_poori"]
idli=6
dosa=15
pongal=30
appam=15
vada=7
set_poori=20
################## LUNCH TIME MENU CARD ########################
menucard_lunch=["biriyani","fullmeals","parotta","curdrice"]
biriyani=150
fullmeals=80
parotta=15
curdrice=35
################## DINNER TIME MENU CARD #######################
menucard_dinner=["chapati","noodles","parotta","friedrice"]
chapati=20
noodles=100
parotta=15
friedrice=100

import datetime

Date_and_Time=datetime.datetime.now()


import mysql.connector

mydb=mysql.connector.connect(
   host="localhost",
   user="root",
   password="21102002",
   database="management"

)
mycursor=mydb.cursor()


def breakfast_data(Name,Mobile_No,Time,Food,Bill):
    sql="insert into customer_Bill (Name,Mobile_No,Time,Food,Bill) values (%s,%s,%s,%s,%s)"
    val=(Name,Mobile_No,Time,Food,Bill)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Get Your Bill")
    print("**************************************************")
    print(f"\t\t\t{Date_and_Time}")
    print(f"Name:{Name}\n\nMobile No:{Mobile_No}\n\nTime:{Time}\n\nFood:{Food}\n\nTotal Bill:{Bill}")
    print("**************************************************")


user=input("Enter **start** to Order:").lower().strip()
if user=="start":
    Name=input("Enter Your Name:")
    Mobile_No=int(input("Enter Your Mobile No:"))
    print("***Enter your choice breakfast or lunch or dinner***")
    Time=input("Enter Time:").lower().strip()
    if(Time=="breakfast"):
        print("")
        print("***Breakfast List***")
        print("idli\ndosa\npongal\nappam\nvada\npoori")
        print("")
        Food=input("Enter your order:").lower().strip()
        if(Food in menucard_breakfast):
            if(Food=="idli"):
                print(f"Your {Food} is available...")
                breakfast_count=int(input(f"Enter how many {Food} you want:"))
                Price=breakfast_count*idli
            elif(Food=="poori"):
                print(f"Your {Food} is available...")
                breakfast_count=int(input(f"Enter how many {Food} you want:"))
                Price=breakfast_count*poori
            elif(Food=="dosa"):
                print(f"Your {Food} is available...")
                breakfast_count=int(input(f"Enter how many {Food} you want:"))
                Price=breakfast_count*dosa
            elif(Food=="pongal"):
                print(f"Your {Food} is available...")
                breakfast_count=int(input(f"Enter how many {Food} you want:"))
                Price=breakfast_count*pongal
            elif(Food=="appam"):
                print(f"Your {Food} is available...")
                breakfast_count=int(input(f"Enter how many {Food} you want:"))
                Price=breakfast_count*appam
            elif(Food=="vada"):
                print(f"Your {Food} is available...")
                breakfast_count=int(input(f"Enter how many {Food} you want:"))
                Price=breakfast_count*vada

    elif(Time=="lunch"):
        print("")
        print("***Lunch List***")
        print("biriyani\nfullmeals\nparotta\ncurdrice")
        print("")
        Food=input("Enter your order:").lower().strip()
        if(Food in menucard_lunch):
            if(Food=="biriyani"):
                print(f"Your {Food} is available...")
                breakfast_count=int(input(f"Enter how many {Food} you want:"))
                Price=breakfast_count*biriyani
            elif(Food=="fullmeals"):
                print(f"Your {Food} is available...")
                breakfast_count=int(input(f"Enter how many {Food} you want:"))
                Price=breakfast_count*fullmeals
            elif(Food=="parotta"):
                print(f"Your {Food} is available...")
                breakfast_count=int(input(f"Enter how many {Food} you want:"))
                Price=breakfast_count*parotta
            elif(Food=="curdrice"):
                print(f"Your {Food} is available...")
                breakfast_count=int(input(f"Enter how many {Food} you want:"))
                Price=breakfast_count*curdrice

    elif(Time=="dinner"):
        print("")
        print("***Dinner List***")
        print("chapati\nnoodles\nparotta\nfriedrice")
        print("")
        Food=input("Enter your order:").lower().strip()
        if(Food in menucard_dinner):
            if(Food=="chapati"):
                print(f"Your {Food} is available...")
                breakfast_count=int(input(f"Enter how many {Food} you want:"))
                Price=breakfast_count*chapati
            elif(Food=="noodles"):
                print(f"Your {Food} is available...")
                breakfast_count=int(input(f"Enter how many {Food} you want:"))
                Price=breakfast_count*noodles
            elif(Food=="parotta"):
                print(f"Your {Food} is available...")
                breakfast_count=int(input(f"Enter how many {Food} you want:"))
                Price=breakfast_count*parotta
            elif(Food=="friedrice"):
                print(f"Your {Food} is available...")
                breakfast_count=int(input(f"Enter how many {Food} you want:"))
                Price=breakfast_count*friedrice
    else:
        print("")
        print("Enter Correctly")
        print("")
else:
    print("")
    print("Enter Start Correctly")
    print("")
            
breakfast_data(Name,Mobile_No,Time,Food,Price)
    
