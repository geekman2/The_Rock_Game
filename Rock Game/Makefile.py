#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Geekman2
#
# Created:     20/10/2012
# Copyright:   (c) Geekman2 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
##from Tkinter import*
##from rox import*
trqut='"""'
def makewindow(character,quote):

    rox = open('E:/Users/Chuckles/Dropbox/Tessa and Devon/Rock_Game/rox2.py',"a",)
    rox.write("""def """+ character +"""():
    picname=dirs+'"""+character+""".jpg'
    """+ character +"""= Toplevel()"""+"""
    """+ character +""".geometry('450x450+700+100')
    """+    """says = Label("""+ character +""",text ="""+trqut+quote+trqut+""")
    says.pack(side=BOTTOM)
    img = ImageTk.PhotoImage(Image.open(picname))
    image1 = Label("""+character+""",image=img)
    image1.pack(side=TOP)
    """+ character +""".mainloop()

""")
def makebutton():
    Bnum = 1
    Colnum = 1
    Rownum=1
    count=0
    while Bnum < 107:
        coms = open('C:/Users/Geekman2/Desktop/Rock_Game/buttons.txt',"w",)
        Bname = 'Button'+str(Bnum)
        if Colnum > 7:
            Colnum=1
        if count == 7:
            Rownum=Rownum+1
            count = 0
        coms.write(Bname+"""=Button(master,text='click me',command=lambda:callback("""+Bname+"""))
        """+Bname+""".grid(row="""+str(Rownum)+""",column="""+str(Colnum)+""")
        """)
        Bnum=Bnum+1
        Colnum=Colnum+1
        count=count+1
        print count
def makemore():
    again = 'y'
    while again == 'y':
        makewindow(raw_input('Character:'),raw_input('Quote:'))
        again = raw_input('again?y/n:')



def maketrait():
    coms = open('C:/Users/Geekman2/Desktop/Rock_Game/traits.py',"a",)
    char=raw_input('Character (lower case only please')
    trait1=raw_input('Trait 1 (lower case)')
    trait2=raw_input('Trait 2(lower case)')
    trait3=raw_input('Trait 3 (lower case)')
    coms.write(char+'=["'+trait1+'","'+trait2+'","'+trait3+""""]
    """)


#makemore()
#makebutton()
maketrait()