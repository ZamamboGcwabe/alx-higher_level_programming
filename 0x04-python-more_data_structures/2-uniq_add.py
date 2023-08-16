#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = []

    for element in my_list:
        unique_set.add(element)
    sum_unique = sum(unique_set)

    return(sum_unique)
