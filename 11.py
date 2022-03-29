mt = input('請輸入月及日(用空格分開)')
bir= mt.split(' ')
m=int(bir[0])
d=int(bir[1])
if (m == 1) and (d>=1) and (d<=20):
    a='魔羯座'
elif (m == 12) and (d>=22) and (d<=31):
    a='魔羯座'
elif (m == 1) and (d>=21) and (d<=31):
    a='水瓶座'
elif (m == 2) and (d>=1) and (d<=18):
    a='水瓶座'
elif (m == 2) and (d>=19) and (d<=29):
    a='雙魚座'
elif (m == 3) and (d>=1) and (d<=20):
    a='雙魚座'
elif (m == 3) and (d>=21) and (d<=31):
    a='牡羊座'
elif (m == 4) and (d>=1) and (d<=20):
    a='牡羊座'
elif (m == 4) and (d>=21) and (d<=30):
    a='金牛座'
elif (m == 5) and (d>=1) and (d<=21):
    a='金牛座'
elif (m == 5) and (d>=22) and (d<=31):
    a='雙子座'
elif (m == 6) and (d>=1) and (d<=21):
    a='雙子座'
elif (m == 6) and (d>=22) and (d<=30):
    a='巨蟹座'
elif (m == 7) and (d>=1) and (d<=22):
    a='巨蟹座'
elif (m == 7) and (d>=23) and (d<=31):
    a='獅子座'
elif (m == 8) and (d>=1) and (d<=23):
    a='獅子座'
elif (m == 8) and (d>=24) and (d<=31):
    a='處女座'
elif (m == 9) and (d>=1) and (d<=23):
    a='處女座'
elif (m == 9) and (d>=24) and (d<=30):
    a='天秤座'
elif (m == 10) and (d>=1) and (d<=23):
    a='天秤座'
elif (m == 10) and (d>=24) and (d<=30):
    a='天蠍座'
elif (m == 11) and (d>=1) and (d<=22):
    a='天蠍座'
elif (m == 11) and (d>=21) and (d<=31):
    a='射手座'
elif (m == 12) and (d>=1) and (d<=23):
    a='射手座'
else:
    print('輸入錯誤')
print('星座為:',a)