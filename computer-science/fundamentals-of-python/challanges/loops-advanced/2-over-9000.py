#Write your function here

def over_nine_thousand[a]:
  sum = 0
  for b in a:
    if sum > 9000:
      break
    sum += b
  return sum


#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))
