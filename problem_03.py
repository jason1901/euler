# https://projecteuler.net/problem=3

import math

n = 600851475143

def is_prime(n):
    if n == 1:
        return False
    for number in range(2, math.ceil(n**0.5)):
        if n % number == 0:
            return False
    return True

prime_factors = [number for number in range(1, math.ceil(n**0.5)) if n % number == 0 and is_prime(number)]

print(prime_factors)
