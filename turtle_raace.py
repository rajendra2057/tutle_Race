from turtle import Turtle,Screen
import random
WIDTH =400
HEIGHT = 400
color_list=["red", "orange", "green", "cyan", "blue", "purple", "yellow", "pink","black","brown"]
def no_of_turtles():
    while True:
        n=int(input("Enter the number of turtles you want to participate in race (2-10):"))
        if 2<=n<=10:
            return n
        else:
            print("Invalid Input! please enter the valid input: ")
number= no_of_turtles()
print(number) 
s1=Screen()
s1.setup(400,400)

x_spacing= WIDTH//(number+1) # to make the turtles equidistant from each other:

turtle_list=[]

for i in range(1,number+1): # to create multiple turtles:
    new_turtle=Turtle()
    new_turtle.shape("turtle")
    new_turtle.left(90)
    new_turtle.color(color_list[i-1])
    new_turtle.penup()
    new_turtle.goto(-WIDTH//2+(i*x_spacing),-HEIGHT//2+20)
    # +20 is in y coordinte so that full turlte is visible
    turtle_list.append(new_turtle)
    
def race():
    is_race_on= True
    while is_race_on:
        
        for turtle in turtle_list:
            distance=random.randrange(2,20)
            turtle.fd(distance)
            
            x, y=turtle.position()
            
            if y>=HEIGHT//2:
                
                print(f"the winner is {turtle.pencolor()} turtle")
                is_race_on=False

race()
s1.mainloop()