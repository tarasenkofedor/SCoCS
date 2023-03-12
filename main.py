# Prints "Hello, World!"
def print_hello_world():
    print("Hello, World!")


# Gets two numbers and operation to apply to those numbers,
# then does that operation and returns the result
def calculate(first_number, second_number, operation):

    if operation == "add":
        return first_number + second_number
    elif operation == "sub":
        return first_number - second_number
    elif operation == "mult":
        return first_number * second_number
    else:
        return first_number / second_number


# Runs the program
if __name__ == '__main__':
    print_hello_world()
    calculate(1, 2, "sum")
