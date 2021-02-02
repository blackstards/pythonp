import random
print("和计算机猜数字(升级版）")
print("BS出品")
print("计算机随机生成数的范围为1-100,请输入1-100间的数")
n3=0
n4=0

while(0==0):
    n1 = random.randint(1, 100)#在1-100之间随便取一个数
    n3=n3+1
    print("现在是第%s局，目前总积分为%s，继续加油！"% (n3,n4))
    while(0==0):    
        n2 = int(input("你猜的数："))
        if (n1==n2):
            n4+=1
            print("猜对了！恭喜你！你目前的总积分为%s,加油！"% n4)
            break
        if (n1!=n2):
            if (n1>=n2):
                print("你猜的数小了哦！再试试吧！")
            if (n1<=n2):
                print("你猜的数大了哦！再试试吧！")