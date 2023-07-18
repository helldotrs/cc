# Write your tip function here:

def total(a,b):
  return a + (a * (b/100))

def tip(a,b):
  return a * (b/100)
  
# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0
