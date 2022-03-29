M=int(input("請輸入階乘值M:"))
N=0
t=1
while t<M:
    N+=1
    t*=N
print("超過M為1000的最小階層N值為:",N)