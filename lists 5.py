#listsis collection of items and is mutable allow dublecate elements  callesd list
items = ["greeps","banana","orange","apple","peralu"]
print(items[0]) # index is kehate isko  very imp concept
print(items[1])
print(items[2])
print(items[3])
print(items[4])
print(items[-2])
print(items[-1])
list = [1,2,3,4,5,"banana","apple","peralu"]
print(list[0])
print(list[1])
print(list)
print(list[2])
print(list[-3])
list = [1,2,3,4,5,[1,2,3,4,5,6,7,8,9],"banana","apple","peralu"]
print(list[0])
print(list[1])
print(list)
print(list[5])
print(list[-3])
# we want to change in the lists
list = [1,2,3,4,5,[1,2,3,4,5,6,7,8,9],"banana","apple","peralu"]
list.pop()# it is very imp for in python

print(list)
list.append("banana")
print(list)
list.pop(5)
print(list)
list.remove("banana")
print(list)
list.insert(2,"banana")
print(list)
#list.clear()
#print(list)
list[0] = "cofee powder"
print(list)
#strat stop step
items = [1,2,3,4,5,6,7,8,9]
#print(items[0:4])
print(items[0::1])
# whaen we using both "::" alret beacuse after write the "::" the how much value wegives  that much skip
print(items[1::4])
print(items[4:])
print(items[:5]) # imp point remerer because":" whre will gives it after gives the number or before the number , when we will give the afer number after numbers elements prints and wise versha
print(items[::-2])
print(len(items))
lst = [1,2,3,4,5,6,7,8,9]
#print(sum(lst))
#print(lst.index(6))
#print(lst.count(1))
lst.reverse()
print(lst)
print(sorted(lst))
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(matrix[0])
print(matrix[1][1])
print(matrix[2][2])
#home work
list1 = [1,2,3,4,5]
list1.append(7)
print(list1)
list1.insert(1,10)
print(list1)
list1.remove(3)
print(list1)
print(sorted(list1))
print(reversed(list1))




