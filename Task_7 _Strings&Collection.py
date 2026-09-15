print("------ Strings Operation ------")

text = "Welcome to Python"

print("Original Text:", text)
print("Upper Text:", text.upper())
print("Lower Text:", text.lower())
print("Replace:", text.replace("Python","java"))
print("Find 'Python':", text.find("Python"))

print("\n------ List Operations ------")

students = ["Aryan", "Rahul", "Sobhit"]

print("Original List:", students)

students.append("Rohit")
print("After Append:", students)

students.remove("Rahul")
print("After Remove:",students)

students.sort()
print("After Sort:", students)

print("\n------ Tuple Creation and Indexing ------")

courses = ("Python", "SQL", "Power BI")

print("Tuple:", courses)
print("First Elememt:", courses[0])
print("Second Elememt:", courses[1])
print("Third Elememt:", courses[2])

print("\n ------ Dictionary ------")

student = {
    "Name": "Aryan Dubey",
    "Age": "19",
    "Course": "BCA"
}

print("Student Information:", student)

print("Name:", student["Name"])
print("Age:", student["Age"])
print("Course:", student["Course"])

print("\n------ Set Operations ------")

skills = {"Python", "SQL", "Excel"}

print("Original Set:", skills)

skills.add("Power BI")
print("After Add:", skills)

skills.remove("SQL")
print("After Remove:", skills)
