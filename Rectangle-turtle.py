import turtle
tao=turtle.Pen()  #ดึงความสามารถในการใช้ปากกา
tao.shape("turtle") #แปลงร่างเป็นเต๋า

def Rectangle():
    '''ฟังก์ชั้นนี้เอาไว้วาดรูปสี่เหลี่ยม'''
    for i in range(4):
        tao.fd(100)
        tao.left(90)



def Go (x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()


Go(200,200)
Rectangle()
