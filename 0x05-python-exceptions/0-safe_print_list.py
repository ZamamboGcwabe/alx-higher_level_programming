#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        num = 0
        for i in my_list:
            if num < x:
                print(i, end= ' ')
                num += 1
        print()
        return (num)
    except:
        return (num)
