from turtle import *


# house

#step 1: square
width (5)
color ("blue")
forward (200)
left (90)
forward (200)
left (90)
forward (200)
left (90)
forward (200)

#step 2: door
left (90)
forward (70)
color ("red")
begin_fill ()
left (90)
forward (90)    #height of the door
right (90)
forward (60)
right (90)
forward (90)
end_fill()

#step 3: roof
penup()
goto (200, 200)
pendown()
color ("green")
begin_fill ()
right (150)
forward (200)
left (120)         
forward (200)      
end_fill()    #end of the roof

#step 4: windows
penup()
goto (0,0)
pendown()
color ("blue")
right(90)
right(90)
left(30)
forward (130)    #height until the window
left (90)
right(180)
forward (70)   #size of the window
left (90)
forward (70)
penup ()
goto (200,200)
pendown ()
left (90)
forward (70)
left(90)
forward(70)
left (90)
forward (70)
left(90)
forward(70)
left (90)
forward(35)
left (90)
forward (70)
right(90)
forward(35)
right(90)
forward(35)
right(90)
forward(70)
left(90)
forward(35)
left(90)
forward(200)
left(90)
forward(35)
left(90)
forward(70)
left(90)
forward(35)
left(90)
forward (35)
left(90)
forward(70)
#end of the house

exitonclick ()

