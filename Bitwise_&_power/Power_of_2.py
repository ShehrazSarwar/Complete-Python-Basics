def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0

num = int(input('Enter number: '))

print(is_power_of_2(num))  # Output: True
print(is_power_of_2(num)) # Output: False
