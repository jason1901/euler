# https://projecteuler.net/problem=4

def is_palindrome(n):
    number_split = [int(i) for i in str(n)]

    if number_split == number_split[::-1]:
        return True
    
    return False
    
palindrome_list = []
for a in reversed(range(100, 1000)):
    for b in reversed(range(100, 1000)):
        if is_palindrome(a * b):
            palindrome_list.append(a * b)

print(max(palindrome_list))