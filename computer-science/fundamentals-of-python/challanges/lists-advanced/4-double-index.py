"""
Create a function named double_index that has two parameters: a list named my_list and a single number named index.

The function should return a new list where all elements are the same as in my_list except for the element at index. The element at index should be double the value of the element at index of the original my_list.

If index is not a valid index, the function should return the original list.

For example, the following code should return [1,2,6,4] because the element at index 2 has been doubled:

double_index([1, 2, 3, 4], 2)

After writing your function, un-comment the call to the function that we’ve provided for you to test your results.
"""

#Write your function here
def double_index(my_list, index):
  my_list[index] = my_list[index] * 2
  return my_list
  
#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))
