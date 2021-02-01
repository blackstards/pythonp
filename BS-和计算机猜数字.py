import random
print("和计算机猜数字")
print("BS出品")
print("计算机随机生成数的范围为1-10,请输入1-10间的数")
n3 = 0
while (0==0):
    n1 = random.randint(1, 10 )#在1-10之间随便取一个数
    n2 = int(input("你猜的数："))
    if (n2 < 1):
        print("请输入正确的数字（1-10），目前累计积分：" + str(n3))
        continue#跳出本次循环
    elif (n2 > 10):
        print("请输入正确的数字（1-10），目前累计积分：" + str(n3))
        continue#跳出本次循环
    elif n1 == n2:
        n3 += 1#使n3加1
        print("恭喜你，猜对了！目前累计积分：" + str(n3))
    else:
        print("猜错了，再来一次吧！目前累计积分：" + str(n3))