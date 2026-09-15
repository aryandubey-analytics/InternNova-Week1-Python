print("------ Numbers from 1 to 20 ------")

for number in range(1,21):
    print(number)

print("\n------ Multiplication Table ------")

table_number = int(input("Enter the number to multiply: "))

for number in range(1,11):
    print(table_number, "x", number, "=", table_number * number)

print("\n------ Even Numbers from 1 to 50 ------")

number = 2 

while number <= 50:
    print(number)
    number +=2
    