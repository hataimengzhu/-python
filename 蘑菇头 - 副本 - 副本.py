# 哈哈哈
import turtle as t
t.pensize(6)
##隐藏画笔
t.hideturtle()
t.colormode(255)
##设置主窗口大小和位置
t.setup(840,500)
##设置画笔速度
##t.speed('fastest')
t.Turtle().screen.delay(0)
#鼻子
##抬笔，可以进行位置操作，但是在画布上不会留下任何痕迹 
t.pu()
##移动画笔到绝对位置
t.goto(-100,100)
##落笔，操作时可以在画布上留下痕迹 
t.pd()
##设置海龟方向
t.seth(-90)
##设置画笔颜色以及填充颜色
t.color((0,0,0),(32,32,24))
##开始填充
t.begin_fill()
t.circle(150,-180)
a = 0
n = 80
t.lt(35) #向左转度
for i in range(n):
        a=a+0.01
        t.fd(a) #向前走a的步长
a = 0
n = 74
t.lt(145) #向左转度
for i in range(n):
        a=a+0.01
        t.fd(a) #向前走a的步长
a = 0
n = 80
t.seth(180)
for i in range(n):
        a=a+0.01
        t.fd(a) #向前走a的步长
        
a = 0
n = 110
t.seth(120)
for i in range(n):
        a=a+0.01
        t.rt(0.4)
        t.fd(a) #向前走a的步长
t.pu()
##移动画笔到绝对位置
t.goto(150,160)
##落笔，操作时可以在画布上留下痕迹 
t.pd()        
a1 = 0
n = 60
t.seth(-15)
for i in range(n):
        a1=a1+0.01
        t.rt(0.4)
        t.fd(a1) #向前走a的步长      
a = 0
n = 100
t.seth(95)
for i in range(n):
        a=a+0.01
        t.lt(0.2)
        t.fd(a) #向前走a的步长
##回走
for i in range(n):
        a=a-0.01
        t.rt(0.2)
        t.bk(a) #向前走a的步长
a1 = 0
n = 60
t.seth(-39)
for i in range(n):
        a1=a1-0.01
        t.lt(0.4)
        t.fd(a1) #向前走a的步长
a = 0
n = 255
for i in range(n):
        a=a-0.01
        t.lt(0.15)
        t.fd(a1) #向前走a的步长
a = 0
n = 45

t.seth(-100)
for i in range(n):
        a=a+0.019
##        t.rt(1.3)
        t.bk(a) #向前走a的步长        
for i in range(n):
        a=a-0.019
##        t.rt(1.3)
        t.fd(a) #向前走a的步长
n = 78
for i in range(n):
        a=a+0.019
        t.lt(0.2)
        t.fd(a) #向前走a的步长
a = 0
t.seth(185)
n = 85
for i in range(n):
        a=a+0.019
        t.lt(0.2)
        t.fd(a) #向前走a的步长
a = 0
n = 60
t.rt(115) #向左转度
for i in range(n):
        a=a+0.01
        t.fd(a) #向前走a的步长
a = 0
n = 70
t.seth(230)
for i in range(n):
        a=a+0.01
        t.fd(a) #向前走a的步长
a = 0
n = 71
for i in range(n):
        a=a+0.01
        t.rt(2)
        t.fd(a) #向前走
##移动画笔到绝对位置
t.goto(-100,100)          
##填充结束        
t.end_fill()
t.pu()
##移动画笔到绝对位置
t.goto(-40,81)
##落笔，操作时可以在画布上留下痕迹 
t.pd()
a = 0
n = 100
t.seth(-80)
for i in range(n):
        a=a+0.01
        t.lt(0.3)
        t.fd(a) #向前走a的步长
a = 0
n = 80
for i in range(n):
        a=a+0.01
        t.lt(0.4)
        t.fd(a) #向前走a的步长
a = 0
n = 50
for i in range(n):
        a=a+0.01
        t.lt(0.3)
        t.fd(a) #向前走a的步长
a = 0
n = 135
for i in range(n):
        a=a+0.01
        t.lt(0.1)
        t.fd(a) #向前走a的步长
a = 0
n = 85
for i in range(n):
        a=a+0.01
        t.lt(0.2)
        t.fd(a) #向前走a的步长
a = 0
n = 60
for i in range(n):
        a=a+0.01
        t.lt(0.6)
        t.fd(a) #向前走a的步长
a = 0
n = 100
for i in range(n):
        a=a+0.01
        t.lt(0.7)
        t.fd(a) #向前走a的步长
t.pu()
##移动画笔到绝对位置
t.goto(15,110)
##落笔，操作时可以在画布上留下痕迹 
t.pd()
t.pensize(4)
t.seth(90)
t.circle(-20,160)
t.pu()
##移动画笔到绝对位置
t.goto(85,120)
##落笔，操作时可以在画布上留下痕迹 
t.pd()
t.seth(90)
t.circle(-20,170)
t.pu()
##移动画笔到绝对位置
t.goto(45,100)
##落笔，操作时可以在画布上留下痕迹 
t.pd()
t.pensize(6)
a = 0
n = 30
for i in range(n):
        a=a+0.01
        t.lt(3)
        t.fd(a) #向前走a的步长
t.pu()
##移动画笔到绝对位置
t.goto(100,107)
##落笔，操作时可以在画布上留下痕迹 
t.pd()
a = 0
n = 30
for i in range(n):
        a=a+0.01
        t.lt(3)
        t.fd(a) #向前走a的步长      
t.pensize(3)
t.pu()
##移动画笔到绝对位置
t.goto(30,83)
t.pd()
t.goto(50,88)
##落笔，操作时可以在画布上留下痕迹 

t.pu()
##移动画笔到绝对位置
t.goto(100,93)
t.pd()
t.goto(120,98)


t.pu()
##移动画笔到绝对位置
t.goto(52,68)
t.pd()

t.color((0,0,0),(0,0,0))
t.begin_fill()
t.seth(-100)
a = 0
n = 60
for i in range(n):
        a=a+0.01
##        t.lt(0.4)
        t.fd(a) #向前走a的步长      

a = 0
n = 100
t.seth(10)
for i in range(n):
        a=a+0.01
##        t.lt(0.4)
        t.fd(a) #向前走a的步长 
t.seth(90)
a = 0
n = 60
for i in range(n):
        a=a+0.01
##        t.lt(0.4)
        t.fd(a) #向前走a的步长
t.seth(190)
a = 0
n = 96
for i in range(n):
        a=a+0.01
##        t.lt(0.4)
        t.fd(a) #向前走a的步长
t.end_fill()

t.seth(80)
a = 0
n = 50
for i in range(n):
        a=a+0.01
##        t.rt(0.4)
        t.fd(a) #向前走a的步长
t.goto(96,88)
t.goto(100,76)    
t.pu()

t.goto(49,50)
t.pd()
t.goto(46,36)
t.goto(104,49)


a = 0
n = 50
for i in range(n):
        a=a+0.01
        t.lt(1)
        t.fd(a) #向前走a的步长

t.pu()
t.pensize(5)

t.goto(20,20)
t.pd()
t.goto(-30,-20)
t.goto(0,-15)
t.goto(0,0)

t.goto(0,-15)
t.goto(10,-12)
t.goto(11,-2)
t.goto(10,-62)
t.goto(130,-57)
t.goto(130,0)
t.goto(145,8)
t.goto(135,37)
t.goto(142,19)
t.goto(155,46)

t.pu()
t.color((0,0,0),(67,67,67))
t.begin_fill()

t.goto(35,17)
t.pd()
t.goto(35,-57)
t.goto(48,-57)
t.goto(48,17)
t.goto(35,17)
t.end_fill()
t.pu()
t.color((0,0,0),(67,67,67))
t.begin_fill()

t.pd()
t.goto(105,27)
t.goto(105,-57)
t.goto(118,-57)
t.goto(118,27)
t.goto(105,27)
t.end_fill()

t.color((0,0,0),(65,65,65))
t.begin_fill()
t.pu()

t.goto(9,-57)
t.pd()
t.goto(9,-90)
t.goto(130,-87)
t.goto(130,-57)
t.goto(9,-57)
t.end_fill()
t.pu()

t.goto(15,-87)
t.pd()
t.goto(21,-117)
t.goto(35,-87)

t.pu()

t.goto(108,-87)
t.pd()
t.goto(118,-114)
t.goto(123,-87)
t.pd()
t.pu()

t.goto(-200,-57)
t.pd()
t.write("这个人怎么这么帅", font=("微软雅黑", 14, "normal"))
import time
time.sleep(2)

