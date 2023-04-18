def add(a, b):
    return a + b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b
def div(a,b):
    return a/b
<<<<<<< Updated upstream
def hello():
=======
def print1():
>>>>>>> Stashed changes
    pass
def main():
    a = int(input("ENTER NUMBER 1: "))
    b = int(input("ENTER NUMBER 2: "))

    sum = add(a, b)

    sub = subtraction(a,b)
    mul = multiplication(a,b)

    print("Addition is ->", sum)
    print("subtraction is ->", sub)
    print("multiplication : ",mul)

main()