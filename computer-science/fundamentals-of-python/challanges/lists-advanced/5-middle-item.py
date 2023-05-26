"""
Create a function called middle_element that has one parameter named my_list.

If there are an odd number of elements in my_list, the function should return the middle element. If there are an even number of elements, the function should return the average of the middle two elements.
"""

#Write your function here
def middle_element(my_list):
  my_len = len(my_list)
  if my_len % 2 == 0:
    return my_list[my_len/2]
  else:
    return my_list[my_len/2]


#Uncomment the line below when your function is done
print(middle_element([10, 20, 30]))
print(middle_element([10, 20, 30, 40]))
#print(middle_element([5, 2, -10, -4, 4, 5]))
