#!/usr/bin/env python3

def print_fibonacci(length):
    i = 0
    fibonacci_list = []
    while i < length:
        if i == 0 or i == 1:
            fibonacci_list.append(i)
            i += 1
        else:
            j = i - 2
            k = i - 1
            new_number = fibonacci_list[j] + fibonacci_list[k]
            fibonacci_list.append(new_number)
            i += 1
    print(fibonacci_list)
