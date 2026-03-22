from functools import lru_cache

@lru_cache(maxsize=None) #this decorator stores the values in a memo so you can calculate larger numbers, without repeating the calculations all the time
def fibonacci(n):
    if n <= 2:
        return 1

    return fibonacci(n-1) + fibonacci(n-2) #recursion
    
while True:
    try:
        n = int(input("Fibonacci number: "))
        if n <= 0: 
            print("Input a number larger than 0.\n")
            continue
    except ValueError:
        print("Input a number.\n")
        continue

    break

print(fibonacci(n))