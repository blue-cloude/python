import turtle as t
import math as m

r = int(input("원의 반지름을 입력하세요: "))
# t.speed(10)
t.goto(0,-r)
t.down()

while r >= 1
    t.circle(r)

    e = 2 * r* m.sin(90/2)
    t.rt(225)
    for i in range(4) :
        t.forward(e)
        t.rt(90)

    r = e/2
    t.up()
    t.goto(0,-r)
    t.down()
