#Octagonal figure  八角图形绘制
import turtle  as t
t.pensize(2)
#t.colormode(255)#先使用这行代码将默认状态下turtle.colormode(1.0)切换turtle.colormode(255)
#t.pencolor((240,160,80))#然后可以对应RGB红绿蓝255以内整数随意定义颜色
t.pencolor((0.2, 0.8, 0.55))
for i in range(8):
    t.fd(150)
    t.left(135)
