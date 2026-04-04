#!/usr/bin/python3
def print_last_digit(number):
    last = abs(number) % 10  # Son rəqəm, həmişə müsbət
    print(last, end="")
    return last
