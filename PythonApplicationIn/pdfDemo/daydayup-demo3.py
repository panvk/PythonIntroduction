# pthony 3.2 实例3-天天向上的力量 .createtime 2020-11-09
#qustion 1 1‰的力量
# - 一天365天，每天进步1‰，累计进步多少？ -1.001的365次方，
# - 一天365天，每天退步1‰，累计退步多少？ -0.999的365次方
#1.001的365次方，
####  文字部分，尽量不作记录，可以复制，但是需要思考
#需求分析
#需求分析
#天天向上的力量
#- 数学公式可以求解，似乎没必要用程序
#- 如果是"三天打鱼两天晒网"呢？
#- 如果是"双休日又不退步"呢？

#DayDayUPQ1.py
##dayup = pow (1.001, 365)
##daydown =pow (0.999, 365)
##print("向上:{:.2f},向下:{:.2f}".format(dayup, daydown))
#
#问题2： 5‰和1%的力量
#- 一年365天，每天进步5‰或1%，累计进步多少呢？
#- 一年365天，每天退步5‰或1%，累计剩下多少呢？
#1.005的365次方
#0.995的365次方
#1.01的365次方
#0.99的365次方

#DayDayupQ2.py
##dayfactor = 0.005 # 使用变量,便于修改
##dayup = pow(1+dayfactor, 365)
##daydown=pow(1-dayfactor, 356)
##print("向上:{:.2f}, 向下:{:.2f}".format(dayup, daydown))

#问题3： 工作日的力量
#- 一年365天，一周5个工作日，每天进步1%
#- 一年365天，一周2个休息日，每天退步1%
#- 这种工作日的力量，如何呢？
#1.01365 (数学思维) for..in..  (计算思维)

#DayDayupQ3.py
##dayup = 1.0
##dayfactor = 0.01
##for i in range(365):
##    if i % 7 in [6,0]:
##        dayup = dayup * (1 -dayfactor)
##    else:
##        dayup = dayup * (1+ dayfactor)
##print("工作日的力量:{:.2f}".format(dayup))

#问题4： 工作日的努力
#B君(工作日, x%) A君(365, 1%)
#比较一下
#把x再加点儿
#比不过
#比上了
#输出x
#def..while..
#("笨办法"试错)

#DayDayupQ4.py
##def dayUP(df):
##    dayup = 1
##    for i in range(365):
##        if i % 7 in [6,0]:
##            dayup = dayup * (1 - 0.01)
##        else:
##            dayup = dayup * (1 + df)
##    return dayup
##dayfactor = 0.01
##while dayUP(dayfactor) < 37.78:
##    dayfactor += 0.001
##print("工作日的努力参数是: {:.3f}".format(dayfactor))
##

#pythonDraw.py
##import turtle
##turtle.setup(650,350,200,200)
##turtle.penup()
##turtle.fd(-250)
##turtle.down()
##turtle.pensize(25)
##turtle.pencolor("purple")
##turtle.seth(-40)
##for  i in range(4):
##    turtle.circle(40,80)
##    turtle.circle(-40,80)
##turtle.circle(40,80/40)
##turtle.fd(40)
##turtle.circle(16,180)
##turtle.fd(40 * 2/3)
##turtle.done()

#绘制一个正方形
#import turtle 
#turtle.setup(650,350,200,200)   #设定起点
#turtle.penup()  #画笔抬起
#turtle.fd(200)  #前进
#turtle.down()   #画笔落下
#turtle.pensize(25)
#turtle.pencolor("purple")
#turtle.seth(-40)
#turtle.right(90)   # 先右选择画第二个边
#turtle.penup()  #画笔抬起
#turtle.fd(200)  #前进
#turtle.down()   #画笔落下
#turtle.done()

#import turtle         #导入
#turtle.title("画正方形")
#turtle.pensize(5)      #画笔大小为5
#turtle.pencolor("black") #画笔颜色为红
#for i in range(4):       #循环四次
#    turtle.forward(200)   #前进200
#    turtle.left(90)      #左转90度
#turtle.done()           #导入结束

#正六边形
#import turtle
#turtle.pensize(5)
#turtle.pencolor("black")
#for i in range(6):
#    turtle.fd(200)
#    turtle.left(60)

#正三角行
#import turtle
#turtle.pensize(5)
#turtle.pencolor("black")
#for i in range(3):
#    turtle.fd(200)
#    turtle.left(120)

#正五边形
#import turtle
#turtle.pensize(5)
#turtle.pencolor("black")
#for i in range(5):
#    turtle.fd(200)
#    turtle.left(72)

#TwoRoundDraw.py 一共9条边，共2圈，每次左转角度为80度（720/9）。
import turtle as t
t.pensize(2)
for i in range(9):
    t.fd(150)
    t.left(80)  #720/9


# Yes ,I can do it



#国际、国内\BMI