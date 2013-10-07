#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Geekman2
#
# Created:     21/10/2012
# Copyright:   (c) Geekman2 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from Tkinter import*
from rox import*
from Makefile import*
from random import*
from PIL import*
Characters=[Percy,Annabeth]
shuffle(Characters)
count=0
def callback():
    #try:
    count=count+1
    C = Characters.pop(0)
    #except ValueError:
    #   return None
    return C()

game = Tk()
game.geometry('50x50+700+100')
Button1 = Button(game,text = '1',command =callback )
Button1.pack(side=LEFT)


game.mainloop()
Annabeth()
