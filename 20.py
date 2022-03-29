g = int(input("組數為:"))
list1 = []
for i in range(g):
    list1.append(input("第%d組:" % (i+1)).split())
for i in range(g):
    for j in range(2):
        list1[i][j] = int(list1[i][j])
for i in range(g):
    t = 0
    t = 250*list1[i][0]+175*list1[i][1]
    print("第%d組應收費用:%d" % (i+1, t))