#Write your function here

def odd_indices(my_list):
  return [my_list[a] for a in range(1, len(my_list), 2)] #1 to cut out the first even index (0), len() for end of range, 2 for every second (1 is default if nothing stated)

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))
