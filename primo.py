#!/usr/bin/env python3

def is_prim(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

number = input("Enter a number, and I'll tell you if it's prime: ")
number = int(number)

if is_prime(number):
    print(f"\nThe number {number} is prime.")
else:
    print(f"\nThe number {number} is not prime.")
