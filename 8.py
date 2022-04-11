num=input("輸入第一行正整數為:")
row=input("第二行中數列的數字為:").split(" ")
rowlist=[]
for i in range(len(row)):
    rowlist.append(row[i])
maxcount=0
max=0
for j in range(len(rowlist)):
    if rowlist.count(rowlist[j])>maxcount:
        maxcount=rowlist.count(rowlist[j])
        max=rowlist[j]
if maxcount==1:
    print("每個數字剛好只出現一次")
else:
    print(f"最大出現次數的數字為{max}")
    print(f"出現次數為:{maxcount}")