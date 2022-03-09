# Basic GUI Calculator by Bhavin Patel

from graphics import *
from math import *

class button:
    def __init__(self,win,center, width, height, label):

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('Red')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.label.setSize(12)
        self.label.setStyle('bold')

    def clicked(self, p):
        return self.xmin <= p.getX() <= self.xmax and \
               self.ymin <= p.getY() <= self.ymax


def Calculator(win):

    bd2h = button(win,Point(1.5,8.5),1.9,.9,"Dec>Hex")
    bd2b = button(win,Point(3.5,8.5),1.9,.9,"Dec>Bin")
    bPi = button(win,Point(5.5,8.5),1.9,.9,"Pi")
    bSqrt = button(win,Point(7.25,8.5),1.4,.9,"√")
    bEsc = button(win,Point(8.75,8.5),1.4,.9,"Exit")

    bsin = button(win,Point(1.5,7.4),1.9,.9,"sin")       
    bcos = button(win,Point(3.5,7.4),1.9,.9,"cos")       
    btan = button(win,Point(5.5,7.4),1.9,.9,"tan")
    bDel = button(win,Point(8.0,7.4),2.9,.9,"Del")    

    b0 = button(win,Point(1.5,0.0),1.7,1.6,"0")
    b1 = button(win,Point(1.5,2.0),1.7,1.6,"1")
    b2 = button(win,Point(3.5,2.0),1.7,1.6,"2")
    b3 = button(win,Point(5.5,2.0),1.7,1.6,"3")
    b4 = button(win,Point(1.5,4.0),1.7,1.6,"4")
    b5 = button(win,Point(3.5,4.0),1.7,1.6,"5")
    b6 = button(win,Point(5.5,4.0),1.7,1.6,"6")
    b7 = button(win,Point(1.5,6.0),1.7,1.6,"7")
    b8 = button(win,Point(3.5,6.0),1.7,1.6,"8")
    b9 = button(win,Point(5.5,6.0),1.7,1.6,"9")
    bDot = button(win,Point(3.5,0.0),1.7,1.6,".")
    bPower=button(win,Point(5.5,0.0),1.4,1.4,"^")
    bE=button(win,Point(7.1,0.0),1.4,1.4,"e")
    bEqu = button(win,Point(8.8,0.0),1.4,1.5,"=")

    bAC = button(win,Point(8.0,6.0),2.9,1.5,"AC")
    bBran1 = button(win,Point(7.25,4.4),1.4,1.0,"(")  
    bBran2 = button(win,Point(8.75,4.4),1.4,1.0,")") 
    bMul = button(win,Point(7.25,3.05),1.4,1,"*")    
    bDiv = button(win,Point(8.75,3.05),1.4,1,"/")
    bPlus = button(win,Point(7.25,1.7),1.4,1,"+")
    bMin = button(win,Point(8.75,1.7),1.4,1,"-")

    bg = Rectangle(Point(0.5,9.5), Point(9.5,11.5))
    bg.setFill('gray')
    bg.draw(win)

    show = Text(Point(5,10.5),"")
    show.draw(win)
    
    p = win.getMouse()
    while not bEsc.clicked(p):
        try:
            p = win.getMouse()

            if b0.clicked(p):
                s = show.getText()
                s = s + "0"              
                show.setText(s)
                show.setSize(25)                
                
            elif b1.clicked(p):
                s = show.getText()
                s = s + '1'
                show.setText(s)
                show.setSize(25)
                
            elif b2.clicked(p):
                s = show.getText()
                s = s + '2'
                show.setText(s)
                show.setSize(25)
                
            elif b3.clicked(p):
                s = show.getText()
                s = s + '3'
                show.setText(s)
                show.setSize(25)
            
            elif b4.clicked(p):
                s = show.getText()
                s = s + '4'
                show.setText(s)
                show.setSize(25)

            elif b5.clicked(p):
                s = show.getText()
                s = s + '5'
                show.setText(s)
                show.setSize(25)
                
            elif b6.clicked(p):
                s = show.getText()
                s = s + '6'
                show.setText(s)
                show.setSize(25)
                
            elif b7.clicked(p):
                s = show.getText()
                s = s + '7'
                show.setText(s)
                show.setSize(25)
                
            elif b8.clicked(p):
                s = show.getText()
                s = s + '8'
                show.setText(s)
                show.setSize(25)
                
            elif b9.clicked(p):
                s = show.getText()
                s = s + '9'
                show.setText(s)
                show.setSize(25)

            elif bMul.clicked(p):
                s = show.getText()
                s = s + '*'
                show.setText(s)
                show.setSize(25)        
                    
            elif bDiv.clicked(p):
                s = show.getText()
                s = s + '/'
                show.setText(s)
                show.setSize(25)
                
            elif bPlus.clicked(p):
                s = show.getText()
                s = s + '+'
                show.setText(s)
                show.setSize(25)
                
            elif bMin.clicked(p):
                s = show.getText()
                s = s + '-'
                show.setText(s)
                show.setSize(25)
                
            elif bAC.clicked(p):
                s = ""
                show.setText(s)
                show.setSize(25)

            elif bE.clicked(p):
                s = show.getText()
                s = s + 'e'
                show.setText(s)
                show.setSize(25)
                
            elif bEqu.clicked(p):
                ans = eval(show.getText())
                show.setText(str(ans))
                show.setSize(25)             

            elif bBran1.clicked(p):
                s = show.getText()
                s = s + '('
                show.setText(s)
                show.setSize(25)
                
            elif bBran2.clicked(p):
                s = show.getText()
                s = s + ')'
                show.setText(s)
                show.setSize(25)
                
            elif bPower.clicked(p):
                s = show.getText()
                s = s + '**'
                show.setText(s)
                show.setSize(25)

            elif bSqrt.clicked(p):
                s = show.getText()
                s = s + 'sqrt('
                show.setText(s)
                show.setSize(25)
                
            elif bd2h.clicked(p):
                s = show.getText()
                s = s + 'hex('
                show.setText(s)
                show.setSize(25)

            elif bd2b.clicked(p):
                s = show.getText()
                s = s + 'bin('
                show.setText(s)
                show.setSize(25)
                
            elif bPi.clicked(p):
                s = show.getText()
                s = s + 'pi'
                show.setText(s)
                show.setSize(25)

            elif bsin.clicked(p):
                s = show.getText()
                s = s + 'sin('
                show.setText(s)
                show.setSize(25)
                
            elif bcos.clicked(p):
                s = show.getText()
                s = s + 'cos('
                show.setText(s)
                show.setSize(25)

            elif btan.clicked(p):
                s = show.getText()
                s = s + 'tan('
                show.setText(s)
                show.setSize(25)

            elif bDel.clicked(p):
                s = show.getText()
                if s != "Math Error!":
                    s = s[:-1]
                    show.setText(s)
                    show.setSize(25)             

            elif bDot.clicked(p):
                s = show.getText()
                s = s + '.'
                show.setText(s)
                show.setSize(25)              
                
        except:
            show.setText("Math Error!")
            show.setSize(25)
    
    win.close()

win = GraphWin("Python Project Basic Calculator",400,450)
win.setCoords(0.0,-1.0,10,12)
Calculator(win)
