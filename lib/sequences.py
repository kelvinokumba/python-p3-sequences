#!/usr/bin/env python3

def print_fibonacci(length):
    if length<= 0:
        print("Lenght should be positive interger")
        return 
    fibonacci_sequence = [0, 1]


    while len(fibonacci_sequence) < length:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    print("Fibonacci sequence:")
    print(fibonacci_sequence[:length])


#Print the first 10 numbers in the Fibonacci sequence
print_fibonacci(10)
