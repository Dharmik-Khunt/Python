students = ["dharmik", "krish", "sunny", "Aryan", "Krunal"]

for student in students:
    if student == "sunny":
        continue;           # To skip any word use 'continue' function.
    print(student)

# To stop loop at any word then use 'break' function.
print("\n\n")
for student in students:
    if student == "Aryan":
        break;
    print(student)
