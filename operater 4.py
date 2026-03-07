#''' assinment operata = 10
'''a = a + 10
print(a)
b = 30000
b *= 100000
print(b)
a = 100
b = 20
print(a==b)
print(a<b)
print(a>b)
print(a!=b)
print(a>=b)
print(a<=b0'''

#logical operrater
# 'and' use as the both are corect or not and 'or'
a = 5
print(a<10 and a>10)
print(a<10 or a>10)
print(not(a<10))
print(a>10)
#membership operater
string = "mahesh"
print("m" in string)
print("hesh" in string)
my_list = [10 , 20 , 30 , 40 , 50 , 60 ]
print(10 in my_list)
print(60 in my_list)
print("z" in my_list)
# both are using at atime in in one print fution
print(("c" in string) and (10 in my_list))  # if the in "and" funtion gives the out both must be true  while it gives the good output  othewise it gives false )
# but the or is not like that if one must be correct if the one correct both this while gives out put true )
print(("c" in string) or (10 in my_list))
print(not("c" in string) and (90 in my_list))

# bitwise operater
#1 bit is eqau to the 8bytes
#home work
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > 10 and num2 > 10:
    print("both numbers positive and greter than the 10")
else:
    print("both numbers negative and greter than the 10")
if num1 < 5 or num2 < 5:
    print("both numbers less than or equal to 5")
else:
    print("both numbers greater than or equal to 5")
if not(num1<num2):
    print("num1 is not greater than num2")
else:
    print("num1 is greater than num2")
# Take two numbers as input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# 1. Both numbers are greater than 10 (using and)
if num1 > 10 and num2 > 10:
    print("Both numbers are greater than 10.")
else:
    print("Both numbers are NOT greater than 10.")

# 2. At least one number is less than 5 (using or)
if num1 < 5 or num2 < 5:
    print("At least one number is less than 5.")
else:
    print("Neither number is less than 5.")

# 3. First number is NOT greater than second (using not)
if not (num1 > num2):
    print("The first number is NOT greater than the second number.")
else:
    print("The first number is greater than the second number.")
#home work 2
age = int(input("Enter your age: "))
if age<18:
    print("Your age is less than to 18.")
else:
    print("Your age is greter  than 18.")
age1 = int(input("Enter your age: "))
if age1<=18:
    print("Your age is greater than or equal to 18.")
else:
    print("Your are the not the adult thika muchkond odu chennagi.")
# Take input from user
text = input("Enter a string: ")

# Check if letter 'a' is in the string
if 'a' in text:
    print("The letter 'a' is present in the string.")
else:
    print("The letter 'a' is NOT present in the string.")

# Check if the word "Python" is NOT in the string
if "Python" not in text:
    print("The word 'Python' is NOT present in the string.")
else:
    print("The word 'Python' is present in the string.")
my_list = [10, 20, 30, 40, 50]
if 10 in my_list:
    print("10 in my_list")
else:
    print("10 not in my_list")
if 10 not in my_list:
    print("10 not in my_list")
else:
    print("10 in my_list")
 # home wokr 3
a = 10
b = 20
print(a & b)
print(a | b)
print(a ^ b)
print(a << 2)
print(a >> 2)
print(b >> 1)
print(a & a)
print(a | a)



