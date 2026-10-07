# LARGEST OF THREE  

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a == b == c:
    print(f"The largest number is {a}.")
    print("All three numbers are equal.")
elif a >= b and a >= c:
    print(f"The largest number is {a}.")
    if a == b:
        print(f"{a} and {b} are equal.")
    elif a == c:
        print(f"{a} and {c} are equal.")
elif b >= a and b >= c:
    print(f"The largest number is {b}.")
    if b == a:
        print(f"{b} and {a} are equal.")
    elif b == c:
        print(f"{b} and {c} are equal.")
else:
    print(f"The largest number is {c}.")
    if c == a:
        print(f"{c} and {a} are equal.")
    elif c == b:
        print(f"{c} and {b} are equal.")
