# -*- coding: cp1250 -*-

from tkinter import *
from math import sqrt

class myApp:

    def vymaz(self):
        self.enta.delete(0, END)

        self.enta.insert(0, '0')
        self.enta.focus_force()

    def obvod(self):
        return self.a+self.b+self.c

    def obsah(self):
        s = self.obvod() / 2
        return sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))

    def je_trojuhelnik(self):
        return True
        #return False

    def je_pravouhly(self):
        return True
        #return False

    def je_rovnostranny(self):
        return True
        #return False

    def vyresit(self):
        try:
            self.a = float(self.enta.get())
            self.b = float(self.entb.get())
            self.c = float(self.entc.get())

            txt = "Obecný trojúhelník"

            if self.je_trojuhelnik():
                if self.je_pravouhly(): txt = "Pravoúhlý trojúhelník"
                if self.je_rovnostranny(): txt = "Rovnostranný trojúhelník"
                # vypsat vysledek
            else:
               pass
               # vypsat, ze neni trojuhelnik

        except ValueError:
            # vypsat, ze strany nebyly spravne zadany
            pass

    def __init__(self, root):

        root.title('Triangle')

        self.top = Frame(root)
        self.top.pack(fill=BOTH)

        #top

        #zadani
        self.zadanif = Frame(self.top,relief=GROOVE, borderwidth=2)
        self.zadanif.pack(fill=Y, side=LEFT, padx=4, pady=4, ipady=4)

        self.la=Label(self.zadanif, text="Strana a =")
        self.la.pack(fill=X, padx=8, pady=1)
        self.enta = Entry(self.zadanif, width = 14)
        self.enta.pack(padx=8, pady=3)

        self.lb=Label(self.zadanif, text="Strana b =")
        self.lb.pack(fill=X, padx=8, pady=1)
        self.entb = Entry(self.zadanif, width = 14)
        self.entb.pack(padx=8, pady=3)

        self.lc=Label(self.zadanif, text="Strana c =")
        self.lc.pack(fill=X, padx=8, pady=1)
        self.entc = Entry(self.zadanif, width = 14)
        self.entc.pack(padx=8, pady=3)

        self.but = Button(self.zadanif, text='Vymazat', command=self.vymaz)
        self.but.pack(padx=4, pady=4)

        self.vymaz()
        self.enta.focus_force()

        #vysledek

        #buttons


root = Tk()
app = myApp(root)
root.mainloop()

