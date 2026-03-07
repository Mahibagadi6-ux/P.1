#tuples and also collection of items but it is immutable and canot the change itmes in elements tuples and lists are but the once tuple created cannot change
my_tuple = ("male","female","others")
print(my_tuple)
#print(type(my_tuple))
#my_tuple.append('dog') impotent note remeber tuple donot allows the pop sort append but allow the indexing for exmple
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[:2])
print(my_tuple[2:])
print(my_tuple[:])
# but we can the tuples
tuple = (1,2,3,3,4,5,6,7,8,9,10)
tuple1 = (9,8,7,6,5,4,3,2,1)
tuple3 = tuple + tuple1
print(tuple3)
tuple = (1,2,3,4,5,6,7,8,9,10) * 4
print(tuple)
tuple = (1,2,3,4,5,6,7,8,9,10) * 4
print(1 in tuple)
print(tuple)
tuple = (1,2,3,4,5,6,7,8,9,10) * 4
print(tuple.index(4))


# sets  is the set of uniqe items is called sets  it dont allow the doublecate elements it is unoreded and unindexed
s = {1,2,3,4,5,6,7,8,9,10}
print(s)
s = {7,6,5,3,4,6,8}
print(s)
s = {1,2,3,4,5,6,7,8,9,10}
s2 =  {11,12,3,4,5,16,17,18,19,20,21,22,23}
print(s | s2) #remeber union | and intrsection &
print(s & s2)
print(s - s2) # frist  set and second elements element takes commonn and remaining elements of fisrt ste gives the output
# in sets remove donot allow but allows the dicard for exapmle
s = {1,2,3,4,5,6,7,8,9,10}
print(s.discard(4))
print(s.intersection(s))
print(s.difference(s))
print(s.pop())# pop which does we dont thais depend upone the system
print(s.clear())
#Differences Between Lists, Tuples, and Sets

'''Feature

List

Tuple

Set

Ordering

Ordered

Ordered

Unordered

Mutability

Mutable

Immutable

Mutable

Duplicates

Allows duplicates

Allows duplicates

No duplicates

Indexing

Supports indexing

Supports indexing

No indexing

Operations

List operations

Tuple operations

Set operations

Common Uses

General collection

Fixed data

Unique items'''


my_tuple = (1,2,3,4,5,6)
print(my_tuple.index(2))
print(my_tuple.count(2))
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[1:3])







