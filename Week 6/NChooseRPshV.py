def factorial(x):
    if x <= 1:
        return 1

    return x * factorial(x-1)


def calculation(n, r):
    diff = factorial(n-r)
    n = factorial(n)
    r = factorial(r)
    
    return int(n/(r*diff))

while True:
    try:
        r = int(input("Amount of objects to be chosen: "))
        n = int(input("Set of: "))
        
        if n < r:
            print("The amount of objects to be chosen cannot be larger than the set.")
            continue
        elif n < 0 or r < 0:
            print("The input cannot be smaller than 0.")
            continue

    except ValueError:
        print("The input must be an integer.")

    break

print(calculation(n, r))