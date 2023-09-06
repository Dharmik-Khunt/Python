first = input("Enter first num:")
operator = input("Enter operator(+,-,*,/,%)=")
second = input("Enter second num:")

if operator == '+':
    print(int(first) + int(second))
elif operator == '-':
    print(int(first) - int(second))
elif operator == '*':
    print(int(first) * int(second))
elif operator == '/':
    print(int(first) / int(second))
elif operator == '%':
    print(int(first) % int(second))
else:
    print("invalid operator")