print("------ Basic File Handling ------")

introduction = """My name is Aryan Dubey.
I am a BCA students.
I am currently pursuing BCA and learning Python Analyst througm my Internova Internship programme.
"""
with open("introduction.txt","w") as file:
    file.write(introduction)

print("Introduction written succesfully to introduction.txt")

with open("introduction.txt","r") as file:
    content = file.read()

print("\n------ File Contents ------")
print(content)