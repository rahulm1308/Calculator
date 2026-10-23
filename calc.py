
#!/usr/bin/env python3

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b


def main():
    while True:
        try:
            a = int(input("Enter the first argument: "))
            op = input("Enter the operation: ")
            b = int(input("Enter the second argument: "))

            if op == "+":
                print("Sum:", add(a, b))
            elif op == "-":
                print("Difference:", sub(a, b))
            elif op == "*":
                print("Product:", mult(a, b))
            elif op == "/":
                print("Quotient:", div(a, b))
            else:
                print("Invalid operation...")

        except ValueError:
            print("Invalid number argument...")
        except ZeroDivisionError:
            print("Cannot divide by zero.")

        if input("Quit? [y/n] ").lower() == "y":
            break


if __name__ == "__main__":
    main()
