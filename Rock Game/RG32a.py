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

SeriesList = [diomb,diomg,chuckg,chuckb,pjog,pjob,dk,psych,RA,LOZ,]
SeriesList2=['Dragons in Our Midst Good','Dragons in Our Midst Bad','Chuck Good','Chuck Bad','Percy Jackson Good','Percy Jackson Bad','Dragonkeeper','Psych','Rangers Apprentice','Legend Of Zelda']

Quotes = {}
Characters=[]
Characters2 = Characters[:]
alreadyDone=[]
Characters.extend(other)

buttons =[]

dirs = 'C:/Users/Geekman2/Dropbox/Tessa and Devon/Rock_Game/'
dirs2 = 'C:/Users/Geekman2/Dropbox/Tessa and Devon/Rock_Game/Rocks/'
rocks = ['rock2','rock3','rock4','rock5','rock6','rock7','rock8','rock9','rock10','rock11','rock12','rock13','rock14','rock15','rock16','rock17','rock18','rock19','rock20']

class RG():
    def CharacterWindow(Character,final=False):
        #Quote = Quotes[Character]
        picname=dirs+'Pictures/'+Character+'.jpg'
        if final == True:
            subWindow=Tk()
        else:
            subWindow = Toplevel()
        subWindow.minsize(200,200)
        subWindow.title(Character)
        subWindow.geometry('+700+100')
        #says = Label(subWindow,text = Quote)
        #says.pack(side=BOTTOM)
        background = ImageTk.PhotoImage(Image.open(dirs+'Gui Pics/blue gradient.jpg'))
        background_label = Label(subWindow, image=background)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        img = ImageTk.PhotoImage(Image.open(picname))
        image1 = Label(subWindow,image=img)
        image1.pack(side=TOP)
        subWindow.mainloop()

    def callback(Character,window):
        global buttons
        WhosLeft()

        Cindex = Characters.index(Character)
        alreadyDone.append(Character)

        Characters2.remove(Character)

        buttons[Cindex].lower()

        if len(alreadyDone)==len(Characters):
            window.destroy()
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
        Bname = 'Button'+str(count)
        global buttons
        buttons=[]
        shuffle(Characters)

        for i in Characters:
            pic = ImageTk.PhotoImage(Image.open(dirs2+choice(rocks)+'.gif'))
            button = Button(window,image=pic,command=lambda i=i:callback(i,window))
            button.image=pic
            count = count+1
            buttons.append(button)
            if i in alreadyDone:
                buttons[Characters.index(i)]=Label(window,text=i,font=('Comic Sans',12))

        for i in buttons:
            if Colnum > 11:
                Colnum=1
                Rownum = Rownum+1
            i.grid(row=Rownum,column=Colnum)
            Colnum = Colnum+1

    def WhosLeft():
        labels=[]
        rownum=0
        colnum=0
        whosLeft = Toplevel()
        whosLeft.after(8000,lambda:whosLeft.destroy())
        if len(Characters2) > 2:
            for i in Characters2:
                labl = Label(whosLeft,text=i)
                labels.append(labl)
            for i in labels:
                i.grid(row=rownum,column=colnum)
                rownum=rownum+1
                if rownum>20:
                    rownum=0
                    colnum=colnum+1
        else:
            Label(whosLeft,text="Oh, you're close to the end! /n You'll just have to find out /n who's left the fun way!").grid()

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

    def MainPage():
        global Characters2
        Characters2 = Characters[:]

        gameWindow=Tk()
        gameWindow.geometry('+450+100')

        background = ImageTk.PhotoImage(Image.open(dirs+'Gui Pics/blue gradient.jpg'))
        background_label = Label(gameWindow, image=background)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        Buttons(gameWindow)

        gameWindow.mainloop()
pickSeries()
