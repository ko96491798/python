e=int(input("輸入一個度數(正整數)"))
if e <= 120:
    print("夏月:%.2f" % (e*2.10))
    print("非夏月:%.2f" % (e*2.10))
elif 120<e<=330:
    print("夏月:%.2f" % ((e-120)*3.02+120*2.10))
    print("非夏月:%.2f" % ((e-120)*2.68+120*2.10))
elif 330<e<=500:
    print("夏月:%.2f" %((e-330)*4.39+(330-120)*3.02+120*2.10))
    print("非夏月:%.2f" %((e-330)*3.61+(330-120)*2.68+120*2.10))
elif 500<e<=700:
    print("夏月%.2f" %((e-500)*4.97+(500-330)*4.39+(330-120)*3.02+120*2.10))
    print("非夏月%.2f" %((e-500)*4.01+(500-330)*3.61+(330-120)*2.68+120*2.10))
elif e>700:
    print("夏月%.2f" %((e-700)*5.63+(700-500)*4.97+(500-330)*4.39+(330-120)*3.02+120*2.10))
    print("非夏月%.2f" %((e-700)*4.50+(700-500)*4.01+(500-330)*3.61+(330-120)*2.68+120*2.10))