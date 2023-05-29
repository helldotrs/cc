"""
Create a function called middle_element that has one parameter named my_list.

If there are an odd number of elements in my_list, the function should return the middle element. If there are an even number of elements, the function should return the average of the middle two elements.
"""

#Write your function here
def middle_element(my_list):
  len_var   = len(my_list)
  len_half  = int(len(my_list)/2)
  #return len_var
  if not (len_var % 2 == 0):
    #!() to get least complex first
    return my_list[len_half]

#Uncomment the line below when your function is done
print(middle_element([10, 20, 30]))
print(middle_element([10, 20, 30, 40]))
print(middle_element([5, 2, -10, -4, 4, 5]))
