# Program to find the factorial of anu number. 
# factorial(5) = 5*4*3*2*1 or we can write it as 5 * factorial(4).

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(4))