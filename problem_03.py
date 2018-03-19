# https://projecteuler.net/problem=3

import math

n = 600851475143

def is_prime(n):
    for number in range(2, n):
        if n % number == 0:
            return False
    return True

prime_factors = [number for number in range(1, math.ceil(n**0.5)) if n % number == 0 and is_prime(number)]
print(max(prime_factors))