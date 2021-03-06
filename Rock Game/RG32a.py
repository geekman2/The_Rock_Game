#-------------------------------------------------------------------------------
# Name:        Rock Game 3.1 beta
# Purpose:     A simple process of elimination game, like Deal or No Deal with characters
# Author:      Geekman2
#
# Created:     10/7/2013
# Copyright:   (c) Geekman2 2013
# Licence:     GNU Public Licence V2
#-------------------------------------------------------------------------------
from Tkinter import *
from ttk import*
import winsound
from random import*
import os
from PIL import Image,ImageTk

diomg = ['Billy','Bonnie','Ashley','Walter','Sapphira','Elam','Shiloh','Gabriel','Acacia']
diomb = ['Morgan_le__faye','Devin','Arramos']
chuckg = ['Chuck','Sarah','Awesome','Ellie','Casey','Alex','Orion','Bryce','Morgan']
chuckb = ['Rourke','Jill','Jeffster','Frost','Shaw','Tang','Emmet']
pjog = ['Percy','Annabeth','Leo','Piper','Hazel','Jason','Frank','Grover']
pjob = ['Luke','Clarisse','Octavian','Thalia']
dk = ['Kale','Bardon','Dibl','Gymn','Fenworth','Librettowit','Dar','Regidor','Gilda','Risto','Stox']
psych =['Shawn','Juliet','Lassiter','Gus','Mcnab','Henry']
RA = ['Will','Alyss','Horace','Halt','Evanlyn','Erak','Gilan','Morgarath','Oberjarl_Ragnak']
LOZ = ['Link','Zelda','Fi','Farore','Din','Nayru','Ganon','Ganondorf','Fierce_Deity','Saria','Malon','Ghirahim','Groose']
other=['Squirrels','Owls','Dantes','Guru_Guru','Gummy']

Fibonacci = [3,5,8,13,21,34]

SeriesList = [diomb,diomg,chuckg,chuckb,pjog,pjob,dk,psych,RA,LOZ,]
SeriesList2=['Dragons in Our Midst Good','Dragons in Our Midst Bad','Chuck Good','Chuck Bad','Percy Jackson Good','Percy Jackson Bad','Dragonkeeper','Psych','Rangers Apprentice','Legend Of Zelda']

Quotes = {}
Characters=[]
Characters2 = Characters[:]
alreadyDone=[]
Characters.extend(other)

buttons =[]

dirs = os.path.dirname(__file__)
#dirs = 'C:/Users/Geekman2/Dropbox/Tessa and Devon/Rock_Game/'
dirs2 = dirs+'\\Rocks\\'
rocks = ['rock2','rock3','rock4','rock5','rock6','rock7','rock8','rock9','rock10','rock11','rock12','rock13','rock14','rock15','rock16','rock17','rock18','rock19','rock20']

def CharacterWindow(Character,final=False):
    #Quote = Quotes[Character]
    picname=dirs+'\\Pictures\\'+Character+'.jpg'

    if final == True:
        subWindow=Tk()
    else:
        subWindow = Toplevel()

    subWindow.minsize(200,200)
    subWindow.title(Character)
    subWindow.geometry('+700+100')
    #says = Label(subWindow,text = Quote)
    #says.pack(side=BOTTOM)

    background = ImageTk.PhotoImage(Image.open(dirs+'\\Gui Pics\\blue gradient.jpg'))
    background_label = Label(subWindow, image=background)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    img = ImageTk.PhotoImage(Image.open(picname))
    image1 = Label(subWindow,image=img)
    image1.pack(side=TOP)

    subWindow.mainloop()

def callback(Character,window):
    global buttons
    labelFrame.destroy()
    labelFramer()
    WhosLeft()

    Cindex = Characters.index(Character)
    alreadyDone.append(Character)

    Characters2.remove(Character)

    buttons[Cindex].lower()

    if len(alreadyDone)==len(Characters):
        gameWindow.destroy()
        youAre = Tk()
        youAre.geometry('+700+300')
        Label(youAre,text="You Are...",font = ('Helvetica',74)).pack()
        youAre.after(10,lambda:winsound.PlaySound('Drumroll.wav',winsound.SND_FILENAME))
        youAre.after(5000,lambda:youAre.destroy())
        youAre.mainloop()
        CharacterWindow(Character,True)

    else:
        CharacterWindow(Character)

def Buttons(window):
    count = 0
    Colnum=1
    Rownum=1
    MaxColnum = 0
    Bname = 'Button'+str(count)
    global buttons
    buttons=[]
    shuffle(Characters)
    fibs = []

    for i in Characters:
        pic = ImageTk.PhotoImage(Image.open(dirs2+'\\'+choice(rocks)+'.gif'))
        button = Button(window,image=pic,command=lambda i=i:callback(i,window))
        button.image=pic
        count = count+1
        buttons.append(button)
        if i in alreadyDone:
            buttons[Characters.index(i)]=Label(window,text=i,font=('Comic Sans',12))

    for thebutton in buttons:
##        if len(Characters) < 20:
##            MaxColnum = 5
##        elif len(Characters) > 20 and len(Characters) < 40:
##            MaxColnum = 10
##        elif len(Characters) > 40:
##            MaxColnum = 20
        MaxColnum = 20

        if Colnum > MaxColnum:
            Colnum=1
            Rownum = Rownum+1
        thebutton.grid(row=Rownum,column=Colnum)
        Colnum = Colnum+1

def WhosLeft():
    count = 0
    var = StringVar()
    var.set('')
    irrelevantVariable = ''
    theText = ''

    for i in Characters2:
            var.set(var.get()+' \n '+i)
            print var.get()

    if len(Characters2)>2:
        if len(Characters2)>30:
            theText = "There are too \n many people left \n this list \n wouldn't make \n any sense"
            irrelevantVariable = Label(labelFrame,background='#236DAC',text = theText)
            irrelevantVariable.grid(column=22,row=0,sticky = N+E)

        else:
            try:
                irrelevantVariable.grid_forget()
            except AttributeError:
                pass
            theText = theText = var.get()
            charList = Label(labelFrame,background='#236DAC',text = theText)
            charList.grid(column=22,row=0,sticky = N+E)
            print type(charList)

    else:
        theText = "There's only a \n few people left \n that means you \n get to find out \n who you are the \n fun way"
        Label(labelFrame,background='#236DAC',text = theText).grid(column=22,row=0,sticky = N+E)

def pickSeries():
    pickIt = Tk()
    pickIt.geometry('+700+300')
    cheks = []
    labls = []
    count = 0
    rownum=0

    for i in SeriesList:
        chekbox = Checkbutton(pickIt,command= lambda i=i:Characters.extend(i))
        cheks.append(chekbox)

    for i in SeriesList2:
        labl = Label(pickIt,text = i)
        labls.append(labl)
    for i in cheks:
        i.grid(row=rownum)
        rownum=rownum+1
        count = count+1
    rownum=0
    for i in labls:
        i.grid(row=rownum,column=2)
        rownum=rownum+1
        count = count+1
    Button(pickIt,text = 'Let it begin',command = lambda:pickIt.destroy()).grid(row=100,column=2)
    pickIt.mainloop()
    MainPage()

def labelFramer():
    global labelFrame
    labelFrame = Frame(gameWindow)
    labelFrame.grid(column=2,row=0,sticky = N)


def MainPage():
    global Characters2
    global gameWindow
    global gameFrame

    Characters2 = Characters[:]

    gameWindow=Tk()
    gameWindow.geometry('+10+100')
    gameWindow.title('The Rock Game')
    #gameWindow.maxsize(900,506)

    gameFrame = Frame(gameWindow)
    labelFramer()


    background = ImageTk.PhotoImage(Image.open(dirs+'\\Gui Pics\\blue gradient3.jpg'))
    background_label2 = Label(gameFrame, image=background)
    background_label2.place(x=0, y=50, relwidth=1, relheight=1)

    background_label = Label(gameWindow, image=background)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)
    background_label.lower()

    gameFrame.grid(column=1,row=0,sticky = N)

    Buttons(gameFrame)

    gameWindow.mainloop()

pickSeries()
