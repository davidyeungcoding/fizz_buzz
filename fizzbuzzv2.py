import sys

while True:
    try:
        if len(sys.argv) > 1:
            k = int(sys.argv[1])
        else:
            k = int(input("Please enter the upper limit: "))
        break
    except:
        print("Please enter a number between 1 and 100.")
n = 1

while n <= k:
    if n % 5 == 0 and n % 3 == 0:
        print("fizzbuzz")
    elif n % 5 == 0:
        print("buzz")
    elif n % 3 == 0:
        print("fizz")
    else:
        print(n)
    n += 1