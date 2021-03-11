#jinglingqiu.py   宝可梦精灵球
#import turtle 
#中心园+内部白色填充+黑色外部线
#外面大园+白色线
#中间左右两个穿黑线
#上部180度扇形+红色填充
#下部180度+白色填充
from turtle import *
#外面白色的圆，改为用黄色进行填充
color("red","white")
penup()
goto(0,-200)              
pendown()
begin_fill()
setheading(0)               
circle(200)
end_fill()
#外面270度的扇形
color("red","red")
penup()
goto(0,-200)                  
pendown()
begin_fill()
setheading(0)                
circle(200,270)
left(90)
forward(200) 
end_fill()   
##外面90度的扇形
color("red","white")
penup()
goto(0,-200)                 
pendown()
begin_fill()
setheading(0)                
circle(200,90)
left(90)
forward(200)
end_fill()
##里面的小园
color("black","white")
penup()
goto(0,-100)
pendown()
begin_fill()
setheading(0)    
circle(100)
end_fill()
#中间的两条线，暂时不加
done() #加上这一个语句，代码执行完成后不会关闭画布



