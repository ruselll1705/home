l=['dred','reds','tr','1','e','trt']
l1=[]
d=0
for i in l:
    if len(i)>=2 and (i[0]==i[-1]):
        l1.append(i)
        d+=1
print(l1,d, sep='\n')

l=['dred','reds','tr','1','e','trt']
d=0
for i in l[::-1]:
    if len(i)>=2 and (i[0]==i[-1]):
        d += 1
        continue
    l.remove(i)
print(l, d, sep='\n')






