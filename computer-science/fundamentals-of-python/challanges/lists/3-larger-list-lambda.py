a = [1,2]
b = [3,4]

print( (lambda a,b:  a[-1] if len(a) >= len(b) else b[-1])(a,b) )
