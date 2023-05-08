
"""
Write a function named append_sum that has one parameter — a list named named my_list.

The function should add the last two elements of my_list together and append the result to my_list. It should do this process three times and then return my_list.

For example, if my_list started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8]. 
"""

#Write your function here

def append_sum(a):
    a.append(a[-2] + a[-1])
    return a

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))
