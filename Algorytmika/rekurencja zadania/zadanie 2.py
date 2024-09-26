def binary_func(num):
    if num == 0:
        return 0
    else:
        binary_func(num // 2)
        print(num % 2, end='')

binary_func(13)
print("")
binary_func(38)