#This fun is Requires arguments function.

def average(*num):
    
    sum =0
    for i in num:
        sum = sum + i
    print("The avg is:", sum / len(num))

average(5,4,1,5,5)      # Here we can take values according to user.