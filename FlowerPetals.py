import turtle

petals = int(input("number of petals: "))
angle = (((360/petals)-90)*-1)+90
leftt = 360/petals

for i in range(petals):
    for i in range(180):
        turtle.fd(1)
        turtle.lt(.0056*leftt)

    turtle.lt(angle)

    for i in range(180):
        turtle.fd(1)
        turtle.lt(.0056*leftt)



turtle.done()
