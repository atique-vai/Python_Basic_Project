# add, sub, mul, div
# steps
# 1. print options to the user
# 2. do desired operation
# 3. print result to the user

def add():
    a = int(input("first number: "))
    b = int(input("second number: "))
    sum = a+b
    print(f"The addition of {a} and {b} is : {sum}")

def sub():
    a = int(input("first number: "))
    b = int(input("second number: "))
    ans = a-b
    print(f"The subtraction of {a} and {b} is : {ans}")

def mul():
    a = int(input("first number: "))
    b = int(input("second number: "))
    ans = a*b
    print(f"The multiplication of {a} and {b} is : {ans}")


def mod():
    a = int(input("first number: "))
    b = int(input("second number: "))
    ans = a%b
    print(f"The mod of {a} and {b} is : {ans}")


def divide():
    a = int(input("first number: "))
    b = int(input("second number: "))
    ans = a/b
    print(f"The division of {a} and {b} is : {ans}")
def main():

    option = input("Welcome to basic calculator\n" \
    "Which operation Do you want? \n" \
    "1. Add\n" \
    "2. Subtraction\n" \
    "3. Multiplication\n" \
    "4. Mod operation\n" \
    "5. Division\n")
    if option == "1":
        add()
    elif option == "2":
        sub()
    elif option == "3":
        mul()
    elif option == "4":
        mod()
    elif option == "5":
        divide()
    else:
        print("Invalid Choice\n")

main()