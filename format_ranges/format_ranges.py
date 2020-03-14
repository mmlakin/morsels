#!/usr/bin/env python3
"""
 format_ranges.py

Takes a list of numbers and returns a string that groups ranges of consecutive numbers together.

e.g
> format_ranges([1, 2, 3, 4, 5, 6, 7, 8])
'1-8'
> format_ranges([1, 2, 3, 5, 6, 7, 8, 10, 11])
'1-3,5-8,10-11'

Bonus 1: Handle single numbers
Bonus 2: Handle unordered numbers
Bonus 3: Handle duplicate numbers; produce separate ranges
"""


def format_ranges(numlist: list) -> str:
    numlist = list(numlist)
    numlist.sort()
    lists = []
    num_index = 0
    cur_num = numlist[num_index]
    new_list = [cur_num]
    numlist.remove(cur_num)
    hit_last = False
    while numlist:
        if num_index > len(numlist) - 1:
            num_index = 0
            hit_last = True
        cur_num = numlist[num_index]
        cur_list_num = new_list[-1]
        if cur_num == cur_list_num:
            if hit_last is True:
                lists.append(new_list)
                numlist.remove(cur_num)
            num_index += 1
        elif cur_num == cur_list_num + 1:
            new_list += [cur_num]
            numlist.remove(cur_num)
        else:
            lists.append(new_list)
            num_index = 0
            cur_num = numlist[num_index]
            new_list = [cur_num]
            numlist.remove(cur_num)
    if len(new_list):
        lists.append(new_list)
    lists.sort()
    return_string = ""
    for group in lists:
        if len(group) is 1:
            return_string += str(group[0]) + ","
        else:
            return_string += str(group[0]) + "-" + str(group[-1]) + ","
    return return_string.strip(",")
