#Write your function here

def larger_sum(a,b):
  sum_a = 0
  sum_b = 0
  for item in a:
    sum_a += item
  for item in b:
    sum_b += item
  if sum_a < sum_b:
    return sum_b
  else:
    return sum_a

# exact same solution as CC but with different names lmao

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))
