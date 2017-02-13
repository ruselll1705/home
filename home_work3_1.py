import sys
x=int(sys.argv[1])
y=int(sys.argv[2])
if x>y:
    s=x-y
elif x<y:
    s=x+y
else:
    s=x
print(s)