"""case(11->3)"""


# --------------------------------------------
m = int(input("enter number: "))
op = input("enter op: ")
h = int(input("enter number: "))

match op:
    case "+":
        print(m + h)
    case "-":
        print(m - h)
    case "*":
        print(m * h)
    case "/":
        print(m / h)
    case "%":
        print(m % h)
    case "**":
        print(m ** h)
    case "^":
        print(m ** h)
    case _:
        print("not op")


# --------------------------------------------




















