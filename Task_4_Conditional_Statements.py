marks = int(input("Enter your marks: "))

print("\n------Students Academic Result------")

if marks >= 90:
    print("Grade: A")
elif marks > 75:
    print("Grade: B ")
elif marks >= 60:
    print("Grade: C")
else:
    print("Result: Fail")
