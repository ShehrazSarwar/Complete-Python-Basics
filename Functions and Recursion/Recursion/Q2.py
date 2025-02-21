def sum_n(n):
    if n == 0:
        return 0
    return sum_n(n-1) + n

sum_of_n = sum_n(5)
print(sum_of_n)