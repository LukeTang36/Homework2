#Luke Tang
#Python Level 0 Tuesday
    
#Week 2, Homework 1

#1. If the dot was driven at (600, 900) it would appear at the bottom right of the screen. (100, 150) would appear at top left of the screen.

#2. The first two numbers determine the x and y positions of the rectangle and the 3rd and 4th determine the length and width.

#3. The 4 numbers for ellipse determine the same things as for the rectangle.

#4

def setup():
    size(700, 400)
#To make colors in processing, one needs to input 3 numbers. The first for red, the second for green, and the third for blue.
#Each number must be <255 and >0.
#The RGB value of the color is the 3 numbers.
    background(0, 0, 0)
def draw():
    pushStyle()
    fill(255, 0, 0)
    rect(50, 50, 60, 300)
    popStyle()
    
#Rect(0, 0, 0, 0) First 2 numbers tell python the location of the top left corner of the rectangle. Next two numbers tell the length and width of the rectangle.

    pushStyle()
    fill(0, 255, 0)
    text("Hello world", 270, 50)
    textSize(30)
    popStyle()
    
    pushStyle()
    fill(0, 0, 255)
    ellipse(350, 150, 150, 150)
    popStyle()
    
    pushStyle()
    fill(255, 255, 255)
    ellipse(350, 250, 150, 150)
    popStyle()
    
    pushStyle()
    fill(255, 0, 0)
    ellipse(350, 350, 150, 150)
    popStyle()
    
    pushStyle()
    stroke(0, 255, 0)
    line(150, 100, 200, 300)
    popStyle()
    
    pushStyle()
    fill(255, 255, 0)
    rect(590, 50, 60, 300)
    popStyle()

#I tried but I wasn't able to replicate a red line to mirror the green line.
