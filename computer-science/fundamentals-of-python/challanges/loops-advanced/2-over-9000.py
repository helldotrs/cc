#Write your function here

#this is a weird one because it asks me to wait until the sum is over 9000 to return it, rather than returning the sum BEFORE it becomes more than 9000. Had this been a client I would have double-checked.

def over_nine_thousand(a):
  sum = 0
  for b in a:
    if sum > 9000:
      break
    sum += b
  return sum

#their solution looks slightly different but returns the same value (9020), so guess I did not misunderstand: 
def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if (sum > 9000):
      break
  return sum


#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))
