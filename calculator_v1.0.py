#updated on 13102021

print("Welcome to my calculator v1.0!")

num1 = float(input("Enter your first number: "))
op = input("operator: ")
num2 = float(input("Enter your second number: "))

if op == "+": 
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator!")