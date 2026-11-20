    # Lab Exercise 3: Simple calculator and area calculation

print("1. Calculator")
print("2. Area calculation")

choice = int(input("Enter your choice: "))

if choice == 1:
    a = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    b = float(input("Enter second number: "))

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = "Cannot divide by zero" if b == 0 else a / b
    else:
        result = "Invalid operator"

    print("Result:", result)

elif choice == 2:
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    shape = int(input("Choose a shape: "))

    if shape == 1:
        r = float(input("Enter radius: "))
        print("Area of circle:", 3.14159 * r * r)
    elif shape == 2:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        print("Area of rectangle:", length * width)
    elif shape == 3:
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        print("Area of triangle:", 0.5 * base * height)
    else:
        print("Invalid shape")

else:
    print("Invalid choice")