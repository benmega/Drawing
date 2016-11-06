def connectcircles(x0,y0,r0,x1,y1,r1):
    import turtle
    import math
    scale = 20
    #Insure x0 smaller than x1
    if x1 < x0:
        x2 = x1
        y2 = y1
        r2 = r1
        x1 = x0
        y1 = y0
        r1 = r0
        x0 = x2
        y0 = y2
        r0 = r2
        
        
    
    m = (y1-y0)/(x1-x0) #slope
    b = y0-m*x0  #y intercept
    A = pow(m,2)+1
    B0 = 2*(m*b-m*y0-x0)
    B1 = 2*(m*b-m*y1-x1)
    C0 = pow(y0,2)-pow(r0,2)+pow(x0,2)-2*b*y0+pow(b,2)
    C1 = pow(y1,2)-pow(r1,2)+pow(x1,2)-2*b*y1+pow(b,2)
    xint0 = (-1*B0 + math.sqrt(pow(B0,2) - 4*A*C0))/(2*A)
    yint0 = m*xint0 + b
    xint1 = (-1*B1 - math.sqrt(pow(B1,2) - 4*A*C1))/(2*A)
    yint1 = m*xint1 + b
    
    turtle.speed(0)
    turtle.hideturtle()    
    turtle.penup()

    turtle.goto(x0*scale,y0*scale-r0*scale)
    turtle.pendown()
    turtle.circle(r0*scale) #draw first circle
    turtle.penup()
    
    turtle.goto(xint0*scale,yint0*scale)
    turtle.pendown()
    turtle.goto(xint1*scale,yint1*scale)#draw line
    turtle.penup()
    
    turtle.goto(x1*scale,y1*scale-r1*scale)
    turtle.pendown()
    turtle.circle(r1*scale) #draw second circle
    
        
