"""
Create a function called every_three_nums that has one parameter named start.

The function should return a list of every third number between start and 100 (inclusive). For example, every_three_nums(91) should return the list [91, 94, 97, 100]. If start is greater than 100, the function should return an empty list.
"""
#Write your function here

#Write your function here

def every_three_nums(start):
  output  = [start]
  while(output[-1] <= 100):
    output.append(output[-1]+3)
  return output

#Uncomment the line below when your function is done
print(every_three_nums(91))

"""
while my solution works, their solution was much neater:
def every_three_nums(start):
  return list(range(start, 101, 3))
"""
