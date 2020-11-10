 OctagonProw.py  八边形绘制
import   turtle as t  # 对turtle库进行命名 ，别名 t
t.pensize(2)          # 声明画笔大小 2     
for i in range(8):    # 进行循环 八次
    t.fd(100)         #画笔向前画  100 ，海龟向前进 100 forward() | fd()前进
    t.left(45)        #画笔左转45度