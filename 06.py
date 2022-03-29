value=input("輸入值為:").split(",")
min=''
max=''
value_int=list(map(int,value))
value_int.sort()
value_int=list(map(str,value_int))
for i in range(len(value)):
    min+=value_int[i]

value_int=list(map(int,value_int))
value_int.reverse()
value_int=list(map(str,value_int))
for i in range(len(value)):
    max+=value_int[i]

print("最大值數列與最小值數列差值為:%d" %(int(max)-int(min)))