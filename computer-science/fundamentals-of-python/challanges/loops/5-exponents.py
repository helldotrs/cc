#Write your function here

def exponents(bases,powers):
  expo = []
  for a in range(0, len(bases)):
    expo.append(bases[a] ** powers[a])
  return expo
    

#Uncomment the line below when your function is done
#print(exponents([2, 3, 4], [1, 2, 3]))
