name = input("Enter your name:")
country = input("Enter country:")
print(f"My name is {name} and I am living in {country}")

# Lengthy way
letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Dharmik"
print(letter.format(name,country))