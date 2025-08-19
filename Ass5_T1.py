students = {"Ayaan": 54, "Suraj": 65, "Faizan": 75, "Raju": 86}
user = input("Enter name of the student: ")
if user in students:
    print(f"{user}'s marks: {students[user]}")
else:
    print("Student not found")