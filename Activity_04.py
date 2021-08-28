x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
s=x+y
print("%d + %d = %d"%(x,y,s))
print(f'{x} + {y} = {s}')
print('{} + {} = {}'.format(x,y,s))
print(repr(x)+" + "+repr(y)+" = "+repr(s))
print(x, "+",y,"=",s)
