#Write your function here

def reversed_list(a,b):
  for i in range(len(a)):
    if a(i) != b((len(a)-i)):
    return False
  return True
    
  

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
