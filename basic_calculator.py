print("Operations:\n1. Multiplication (*).\n2. Division (/).\n3. Addition (+).\n4. Subtraction (-).\n5. Root (√).\n")
operation_number = int(input("Input your operation number: "))
first_number = int(input("Input your first number: "))

result = 0
if operation_number == 5:
    result = first_number ** 0.5  # Root of the first number
else:
    second_number = int(input("Input your second number: "))
    if operation_number == 1:
        result = first_number * second_number
    elif operation_number == 2:
        result = first_number / second_number
    elif operation_number == 3:
        result = first_number + second_number
    elif operation_number == 4:
        result = first_number - second_number

print("The result is:", result)
