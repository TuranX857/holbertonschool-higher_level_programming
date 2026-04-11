#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_sum = 0

    for num in set(my_list):
        unique_sum += num

    return unique_sum
