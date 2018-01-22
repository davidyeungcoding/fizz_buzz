import sys

n = 1
if len(sys.argv) > 1:
    n = sys.argv[1:]

try:
    while n <= 100:
        if n % 5 == 0 and n % 3 == 0:
            print("fizzbuzz")
        elif n % 5 == 0:
            print("buzz")
        elif n % 3 == 0:
            print("fizz")
        else:
            print(n)
        n += 1

except:
    print("Please enter a number between 1 and 100.")