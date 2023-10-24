#----------------------------------------------
# Write a program that prints the numbers from 1 to 100. But for multiples of three, print Fizz instead of the number, and multiples of five, print Buzz. For numbers that are multiples of both three and five, print FizzBuzz.
#----------------------------------------------

for i in range(100):
    if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
        print("FizzBuzz", end=" ")
    elif (i + 1) % 3 == 0:
        print("Fizz", end=" ")
    elif (i + 1) % 5 == 0:
        print("Buzz", end=" ")
    else: print(i + 1, end=" ")
