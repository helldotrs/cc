"""
First, print the sum of a and b.

Second, print c minus d.

Third, print the first number printed, multiplied by the second number printed.

Finally, return the third number printed modulo a.
"""

def lots_of_math(a,b,c,d):
  e = a+b
  f = c-d
  g = e*f
  print(e)
  print(f)
  print(g)
  return g % a
  

# Write your lots_of_math function here:

# Uncomment these function calls to test your lots_of_math function:
#print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
#print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0
