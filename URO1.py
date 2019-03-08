# -*- coding: cp1250 -*-
from tkinter import *
from math import sqrt


class myApp:

    def vymaz(self):
        self.enta.delete(0, END)
        self.enta.insert(0, '0')
        self.enta.focus_force()

        self.entb.delete(0, END)
        self.entb.insert(0, '0')

        self.entc.delete(0, END)
        self.entc.insert(0, '0')

    def obvod(self):
        return self.a + self.b + self.c

    def obsah(self):
        s = self.obvod() / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def je_trojuhelnik(self):
        if self.a + self.b > self.c and self.b + self.c > self.a and self.a + self.c > self.b:
            return True
        else:
            return False

    def je_pravouhly(self):
        if pow(self.a, 2) + pow(self.b, 2) == pow(self.c, 2) or pow(self.b, 2) + pow(self.c, 2) == pow(self.a,
                                                                                                       2) or pow(self.a,
                                                                                                                 2) + pow(
                self.c, 2) == pow(self.b, 2):
            return True
        else:
            return False

    def je_rovnostranny(self):
        if self.a == self.b == self.c:
            return True
        else:
            return False

    def vyresit(self):
        try:
            self.a = float(self.enta.get())
            self.b = float(self.entb.get())
            self.c = float(self.entc.get())

            txt = "Obecný trojúhelník"

            if self.je_trojuhelnik():
                if self.je_pravouhly(): txt = "Pravoúhlý trojúhelník"
                if self.je_rovnostranny(): txt = "Rovnostranný trojúhelník"
                self.obsah_ = self.obsah()
                self.obvod_ = self.obvod()
                text_ = "\nObvod je: " + str(self.obvod_) + "\nObsah je: " + str(self.obsah_)
                self.vysledekl_.config(text=txt + text_)
                self.vysledekl_.config(foreground='blue')
                # vypsat vysledek
            else:
                self.vysledekl_.config(text="Nejedna se o trouhelnik")
                self.vysledekl_.config(foreground="red")


        except ValueError:
            self.vysledekl_.config(text="Spatny vstup")

    def __init__(self, root):

        root.title('Triangle')

        self.top = Frame(root)
        self.top.pack(fill=BOTH)

        # top
        self.titlef = Frame(self.top, relief=GROOVE, borderwidth=2)
        self.titlef.pack(fill=X, padx=4, pady=4, ipady=4)
        self.titlel = Label(self.titlef, text="Obvod a obsah trojuhelniku")
        self.titlel.pack()

        # zadani
        self.zadanif = Frame(self.top, relief=GROOVE, borderwidth=2)
        self.zadanif.pack(fill=Y, side=LEFT, padx=4, pady=4, ipady=4)

        self.la = Label(self.zadanif, text="Strana a =")
        self.la.pack(fill=X, padx=8, pady=1)
        self.enta = Entry(self.zadanif, width=14)
        self.enta.pack(padx=8, pady=3)

        self.lb = Label(self.zadanif, text="Strana b =")
        self.lb.pack(fill=X, padx=8, pady=1)
        self.entb = Entry(self.zadanif, width=14)
        self.entb.pack(padx=8, pady=3)

        self.lc = Label(self.zadanif, text="Strana c =")
        self.lc.pack(fill=X, padx=8, pady=1)
        self.entc = Entry(self.zadanif, width=14)
        self.entc.pack(padx=8, pady=3)

        self.but = Button(self.zadanif, text='Vymazat', command=self.vymaz)
        self.but.pack(padx=4, pady=4)

        self.vymaz()
        self.enta.focus_force()

        # vysledek
        self.vysledekf = Frame(self.top, relief=GROOVE, borderwidth=2)
        self.vysledekf.pack(fill=BOTH, expand=1, padx=4, pady=4, ipady=4)

        self.vysledekl = Label(self.vysledekf, text="Vysledek")
        self.vysledekl.pack(padx=8, pady=8)

        self.vysledekl_ = Label(self.vysledekf, text="Zatim zadny vysledek", relief=SUNKEN, borderwidth=2,
                                background="gray")
        self.vysledekl_.pack(fill=BOTH, expand=1, padx=4, pady=4)
        # buttons
        self.buttonf = Frame(self.vysledekf)
        self.buttonf.pack()

        self.vyresitb = Button(self.buttonf, text="Vyresit", command=self.vyresit)
        self.vyresitb.pack(side="left", padx=4, pady=4, ipady=4, ipadx=4)

        self.konecb = Button(self.buttonf, text="Konec")
        self.konecb.pack(side="right", padx=4, pady=4, ipady=4, ipadx=4)


root = Tk()
app = myApp(root)
root.mainloop()
