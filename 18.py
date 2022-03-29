A,J,Q,K=1,11,12,13
c=input("輸入五張牌:").split()
t=0
for i in range(len(c)):
    if c[i]=='A':
        c.remove('A')
        c.insert(i,1)
    elif c[i]=='J':
        c.remove('J')
        c.insert(i,11)
    elif c[i]=='Q':
        c.remove('Q')
        c.insert(i,12)
    elif c[i]=='K':
        c.remove('K')
        c.insert(i,13)
for i in range(len(c)):
    c[i]=int(c[i])
    t+=c[i]
print(t)