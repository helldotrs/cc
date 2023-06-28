#Write your function here

def larger_sum(a,b):
  sum_a = 0
  sum_b = 0
  for items in a:
    sum_a += a
  for items in b:
    sum_b += b
  if sum_a < sum_b:
    return sum_b
  else:
    return sum_a

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))
