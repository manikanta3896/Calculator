
a = int(input("enter a value:"))
b = int(input("enter b value:"))

while True:
    print("simple calculator")
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.exist")

    choice = input("enter a choice:")

    if choice == "5":
        print("calculator closed")
        break
    
    if choice == "1":
        print("answer=",a + b)

    elif choice == "2":
        print("answer=",a - b)

    elif choice == "3":
        print("answer=",a * b)

    elif choice == "4":
        print("answer=",a // b)

    else:
        print("invalid!!!!")
          