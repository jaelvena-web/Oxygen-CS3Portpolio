name = input("What is your name: ")
print("Hello, " + name + "!")

number1 = int(input("Enter number: "))
if number1 > 0:
    print("The number is positive.")
elif number1 == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if num1 > num2:
        print(num1)
    elif num1 == num2:
        print("The numbers are equal.")
    else:
        print(num2)

    score = int(input("Enter your score: "))
    if score >= 75:
        print("Passed")
    else:
        print("Failed")

    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")