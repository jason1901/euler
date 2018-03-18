# https://projecteuler.net/problem=1

total = sum(item for item in range(1000) if item % 3 == 0 or item % 5 == 0)
print(total)