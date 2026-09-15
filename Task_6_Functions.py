def calculate_square(number):
    return number*number


def calculate_average(num1,num2,num3):
    return(num1 + num2 + num3)

print("------ Square of a Number ------")

number = float(input("Enter a number: "))
square = calculate_square(number)

print("Square:", round(square, 2))

print("------ Average of Three Numbers ------")

num1 = float(input("Enter the number: "))
num2 = float(input("Enter the number: "))
num3 = float(input("Enter the number: "))

average = calculate_average(num1, num2 , num3)

print("Average:", round(average , 2))