def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    a = float(input("Enter first number: "))
    op = input("Enter operation (+, -, *, /): ")
    b = float(input("Enter second number: "))

    operations = {
        "+": add,
        "-": sub,
        "*": mult,
        "/": div,
    }

    if op not in operations:
        raise ValueError("Invalid operation")

    print("Result:", operations[op](a, b))
