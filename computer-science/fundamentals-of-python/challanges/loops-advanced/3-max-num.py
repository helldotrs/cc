#Write your function here

def max_num(list):
  max = 0
  for item in list:
    if item > max:
      max = item
  return max

#I don't like CCs solution as it first sets maximum to nums[0] and then compares nums[0] to nums[0] in the first iteration. 
def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum


#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))
