c=int(input("搭了幾次電梯:"))
flist=["1"]
total=0
for i in range(c):
    flist.append(input(""))
    
flist=list(map(int,flist))
for i in range(len(flist)-1):
    if flist[i+1]>flist[i]:
        total+=20*(flist[i+1]-flist[i])
    else:
        total+=10*(flist[i]-flist[i+1])
print(total,"元")   