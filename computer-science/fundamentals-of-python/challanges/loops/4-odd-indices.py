#Write your function here

def odd_indices(my_list):
  odd_list = [a for a in my_list id a % 2 != 0]
  return odd_list

#Uncomment the line below when your function is done
#print(odd_indices([4, 3, 7, 10, 11, -2]))
