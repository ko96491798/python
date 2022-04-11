n=int(input("輸入比數n:"))
award=[]
for i in range(n):
    award.append(input(" ").split(" "))
for i in range(n):
    print(f"{award[i][0]}牌得到{award[i][1]}面")
