# disition making
x = 20
if x == 20:
    print(x)#indentation
else:
    print("x is not eqaul 20")
x = 10
if x % 2 == 0:
    print(" is the even number x")
else:
    print(" is not the even number x or the given number is odd")
signal = input("enter the signle colour: ")
if signal == "red":
    print(" if signal is red we wnt stop the our vehicle " )
elif signal == "yellow":
    print(" we want to ready the to bike to go ")
else:
    print(" move the bike  ")
marks = int(input("enter the marks: "))
if marks >= 75:
    print("he is able to write exam ")
elif marks > 50:
    print("he is  just alijibla to able to write exam ")
else:
    print("he is not able to write exam ")
gender = input("enter the gender: ")
if gender == "male":
    print("he is not able to travel in bus  freely the  ")
elif gender == "female":
    print("he is  able to travel in bus  freely the  ")
elif gender == "other":
    print("they also must pay the money to work ")
else:
    print("he is not able to travel in bus ")

age = int(input("enter the age: "))
if age == 10:
    print("they able to travel in bus ")
else:
    if age <= 5:
        print("ticket is free ")
    elif age >= 50:
        print("ticket is bus  ")
    elif age >= 70:
        print("ticket is half because they have  ")
    else:
        print("because the buss is pumbcture   ")
age =int(input("enter the eligible age: "))
if age <= 5:
    print("no ticket becuase he is child  ")
elif age >= 70:
    print("disscount for the senior citizen ")
elif age >= 90:
    print("disscount for the senior more  citizen  and ticket")
else:
    print("he is not able to travel in bus ")
time = int(input("enter the time: "))
if time < 8:
    print("dinner")
elif time > 8:
    print("breakfast time  ")
elif time <= 2 :
    print("lunch  ")