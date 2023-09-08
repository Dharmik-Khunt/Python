# Tuple is used to store the multiple items in a single variable. 
# Tuple must enclosed with "Round braces".

tup = (2,5,17,8,25)
print(type(tup),tup)

print(tup[0])           # Print item of '0' index.
print(tup[-1])          # Print item 0f last index.

print(tup[1:4])         # Print items from '1' index to '3' index.

if 25 in tup:
    print("Yes it is")