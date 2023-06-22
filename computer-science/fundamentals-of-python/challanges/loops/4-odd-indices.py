#Write your function here

def odd_indices(my_list):
  out_list = []
  for a in range (1, len(my_list), 2): #start, stop, step
    out_list.append(my_list[a])
  return out_list

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))
