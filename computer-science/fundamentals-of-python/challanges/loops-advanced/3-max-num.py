#Write your function here

def max_num(list):
  max = 0;
  for item in list:
    if item > max:
      max = item
  return max


#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))
