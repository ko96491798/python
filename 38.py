n = int(input())
point =[]
a = 0
b = 0
for i in range(1,n+1):
    k = int(input())
    point.append(k)
for i in point:
    a = a+1  
    if i%9 == 0 or i%11 == 0:
        print("第" , a , "個點" , i)
    else :
        b=b+1
if b==n :
    print("0")