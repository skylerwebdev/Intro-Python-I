# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard


# Print out "Even!" if the number is even. Otherwise print "Odd"
import cmd


def is_even(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd")


while True:
    num = input("Enter a number: ")
    num = int(num)
    is_even(num)

