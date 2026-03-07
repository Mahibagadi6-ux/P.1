# for loops are one of the also important concept itret of sequeance
'''for i in range(1,100):
    print(i)
for i in range(1,100,2):
    print(i,end=" ")

cities = ["mangaluru","bengaluru","dharwad"]
for city in cities:
    print(city,end=" ")
ball_in_bagg = ["blue","puple","yellow","red" ]
for ball in ball_in_bagg:
    print(ball)
name = "mahesh_bagadi"
for name in name:
    print(name*10)
name = "mahesh_bagadi"
for index, name in enumerate(name):
    print(name*(index+1))
number = ['1','2','3','4','5','6','7','8','9']
for numbers in number:
   if number == '5':
       print(f"{number} is found")
       break
   print(number)
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for index, city in enumerate(cities):
    print(f"City {index + 1}: {city}")
l = [1,2,3,4,5,6,7,8,9]
for number in l:
    print(number)
    if number==5:
        break
else:
    print("No more numbers")'''
d  = {"name":"mahesh","age":22,"salary":18}
for key,value in d.items():
    print(key,value)
for i in range(1,100):
    print(f"{2}X{i} = {2*i}")
for i in range(1,100):
    for j in range(1,11):
        print(f"{i}X{j} = {i*j}")
for i in range(1,31):
    print(f"{3}X{i} = {2*i}")
for i in range(1,11):
    print(f"{i}+1 = {i+1}")
name = input("Enter your name: ")
for names in name:
    print(names)
name = input("Enter your name: ")
count = 0
for name in name:
    if name in "aeiou":
        count += 1
        print(name)


print("number of vowels in your name:",count)
