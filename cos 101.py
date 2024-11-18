from random import choice


def a():
    print("you are performing multiplication")
    ver1 = float(input("enter your first digit"))
    ver2 = float(input("enter your second digit"))
    print(ver1 * ver2)

def b():
    print("you are performing addition")
    ver1 = float(input("enter your first digit"))
    ver2 = float(input("enter your second digit"))
    print(ver1 + ver2)

def c():
    print("you are performing division")
    ver1 = float(input("enter your first digit"))
    ver2 = float(input("enter your second digit"))
    print(ver1 / ver2)

def d():
    print("you are performing subtraction")
    ver1 = float(input("enter your first digit"))
    ver2 = float(input("enter your second digit"))
    print(ver1 - ver2)

def e():
    print("you are performing workdone")
    ver1 = float(input("enter your first digit"))
    ver2 = float(input("enter your second digit"))
    print(ver1 / ver2)

def main():
    choice=input("choose an operation a-e")
    if choice=="a":
        a()
    elif choice == "b":
        b()
    elif choice == "c":
        c()
    elif choice == "d":
        d()
    elif choice == "e":
        e()
    else:
        print("wrong input")
if __name__ == '__main__':
    main()


