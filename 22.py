a=[]
a.append(['123','456','9000'])
a.append(['456','789','5000'])
a.append(['789','888','6000'])
a.append(['336','558','10000'])
a.append(['775','666','12000'])
a.append(['566','221','7000'])

n=int(input("輸入查詢的組數N為:"))
for i in range(n):
    sign=input("輸入帳號密碼(以空白間隔):").split()
    for j in range(len(a)):
        if sign[0]==a[j][0] and sign[1]==a[j][1]:
            print(a[j][2])
            break
        else:
            print('error')
            break