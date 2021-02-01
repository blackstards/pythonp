print("打印正方形程序")
print("BS出品")
color1 = input("背景颜色？")#设定color1
color2 = input("乌龟颜色？")#设定color2
print("您选择的背景颜色为" + color1 + ",您选择的乌龟颜色为" + color2)
print("打印中......")
import turtle
turtle.screensize(None,None,color1)#设定布颜色
turtle.fillcolor(color2)#填色
turtle.shape("turtle")#设置turtle为正方形
turtle.begin_fill()#开始填充
for num in range(4):#重复执行
    turtle.forward(100)#移动100单位
    turtle.left(90)#左转90度
turtle.end_fill()#填充完毕
print("绘图完成")#完成输出
print("绘图颜色结果仅供参考")