# If we want to change tuple then first we want to convert tuple in list.

# 1. count() Method = it will count the item which we want to count.
tup = (0,1,3,4,7,8,7,9,7,3,7)
a = tup.count(7)
print("Count of '7' in tuple:",a) 

# index() Method = it will show the firstly come index of repeated item. 
b = tup.index(7)
print("Index of '7' in tuple:",b)
