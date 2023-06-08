#Write your function here

def delete_starting_evens(my_list):
  if len(my_list):
    for a in my_list:
      if my_list[0] % 2 == 0:
        my_list = my_list[1:]
      else:
        break
    return my_list

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
