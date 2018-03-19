# https://projecteuler.net/problem=2

a, b, c, sum = 0, 1, 0, 0
while (c < 4e6):
    c = a + b
    if c % 2 == 0:
        sum += c
    a = b
    b = c
print(sum)