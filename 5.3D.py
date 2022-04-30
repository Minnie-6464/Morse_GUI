from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)
import time
import re

##hardware
led = LED(18)

##GUI Definition
win = Tk()
win.title("5.3Dtask")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

##Event Function
def dash():
    led.on();
    time.sleep(1)
    led.off()
    time.sleep(0.5)

def dot():
    led.on();
    time.sleep(0.25)
    led.off()
    time.sleep(0.5)

def enterData():
    userInput = inputtxt.get("1.0", "end-1c")
    Letter(userInput)
    
def Letter(userInput):
    for letter in userInput:
        if (letter.upper() == 'A'):
            dot()
            dash()
            
        elif (letter.upper() == 'B'):
            dash()
            dot()
            dot()
            dot()
            
        elif (letter.upper() == 'C'):
            dash()
            dot()
            dash()
            dot()
            
        elif (letter.upper() == 'D'):
            dash()
            dot()
            dot()     
        
        elif (letter.upper() == 'E'):
            dot()
            
        elif (letter.upper() == 'F'):
            dot()
            dot()
            dash()
            dot()    

        elif (letter.upper() == 'G'):
            dash()
            dash()
            dot()  
        
        elif (letter.upper() == 'H'):
            dot()
            dot()
            dot()
            dot()  
        
        elif (letter.upper() == 'I'):
            dot()
            dot()
            
        elif (letter.upper() == 'J'):
            dot()
            dash()
            dash()
            dash()
            
        elif (letter.upper() == 'K'):
            dash()
            dot()
            dash()
        
        elif (letter.upper() == 'L'):
            dot()
            dash()
            dot()
            dot()
            
        elif (letter.upper() == 'M'):
            dash()
            dash()
            
        elif (letter.upper() == 'N'):
            dash()
            dot()      
        
        elif (letter.upper() == 'O'):
            dash()
            dash()
            dash()
        
        elif (letter.upper() == 'P'):
            dot()
            dash()
            dash()
            dot()
            
        elif (letter.upper() == 'Q'):
            dash()
            dash()
            dot()
            dash()      
        
        elif (letter.upper() == 'R'):
            dot()
            dash()
            dot()
            
        elif (letter.upper() == 'S'):
            dot()
            dot()
            dot()      
        elif (letter.upper() == 'T'):
            dash()
        elif (letter.upper() == 'U'):
            dot()
            dot()
            dash()
        elif (letter.upper() == 'V'):
            dot()
            dot()
            dot()
            dash()
        elif (letter.upper() == 'W'):
            dot()
            dash()
            dash()
        elif (letter.upper() == 'X'):
            dash()
            dot()
            dot()
            dash()       
        elif (letter.upper() == 'Y'):
            dash()
            dot()
            dash()
            dash()  
        elif (letter.upper() == 'Z'):
            dash()
            dash()
            dot()
            dot()  


def close():
    RPi.GPIO.cleanup()
    win.destroy()

inputtxt = Text(win, bg = "light yellow", height = 4, width = 24)
inputtxt.grid(row=0, column=1)

Display = Button(win, text ='Convert to morse code', bg = "grey", height = 2, width = 24,  command = lambda*args:enterData())
Display.grid(row=3, column=1)

exitButton=Button(win, text='Exit', font=myFont, command=close, bg = 'darkgrey', height=2, width=24)
exitButton.grid(row=6, column=1)    

win.protocol("WM_DELETE_WINDOW", close)

win.mainloop()        
        
        
        
        
        
        
        
        
        
        