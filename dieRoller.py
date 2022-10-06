'''

Program: Die Roller
Language: Python using Tkinter
Author: James Eyrich at Kymo's Designs
Date: Mar 22, 2022

'''

import tkinter.constants as tc
from tkinter import Tk, Entry, Button
from random import randint
import time


# DIE ROLLER CLASS!!
class DieRoller(Tk):
    

    def __init__(self):
        super(DieRoller, self).__init__()
        

        def flipACoin():
            shake = 75
            i = 0
            while(i <= shake):
                self.num = randint(1, 2)
                entRoll.delete(0, tc.END)
                entRoll.insert(0, str(self.num))
        
                i += 1
                entRoll.update()
                time.sleep(.01)
            
                    
        def fourSidedDie():
            shake = 75
            i = 0
            while(i <= shake):
                self.num = randint(1, 4)
                entRoll.delete(0, tc.END)
                entRoll.insert(0, str(self.num))
        
                i += 1
                entRoll.update()
                time.sleep(.01)
                    
        def sixSidedDie():
            shake = 75
            i = 0
            while(i <= shake):
                self.num = randint(1, 6)
                entRoll.delete(0, tc.END)
                entRoll.insert(0, str(self.num))
        
                i += 1
                entRoll.update()
                time.sleep(.01)
            
        def eightSidedDie():
            shake = 75
            i = 0
            while(i <= shake):
                self.num = randint(1, 8)
                entRoll.delete(0, tc.END)
                entRoll.insert(0, str(self.num))
        
                i += 1
                entRoll.update()
                time.sleep(.01)
                    
        def tenSidedDie():
            shake = 75
            i = 0
            while(i <= shake):
                self.num = randint(1, 10)
                entRoll.delete(0, tc.END)
                entRoll.insert(0, str(self.num))
        
                i += 1
                entRoll.update()
                time.sleep(.01)
                    
        def twelveSidedDie():
            shake = 75
            i = 0
            while(i <= shake):
                self.num = randint(1, 12)
                entRoll.delete(0, tc.END)
                entRoll.insert(0, str(self.num))
        
                i += 1
                entRoll.update()
                time.sleep(.01)
                    
        def twentySidedDie():
            shake = 75
            i = 0
            while(i <= shake):
                self.num = randint(1, 20)
                entRoll.delete(0, tc.END)
                entRoll.insert(0, str(self.num))
        
                i += 1
                entRoll.update()
                time.sleep(.01)


        def fiftySidedDie():
            shake = 75
            i = 0
            while(i <= shake):
                self.num = randint(1, 50)
                entRoll.delete(0, tc.END)
                entRoll.insert(0, str(self.num))
        
                i += 1
                entRoll.update()
                time.sleep(.01)

        
        def oneHundredSidedDie():
            shake = 75
            i = 0
            while(i <= shake):
                self.num = randint(1, 100)
                entRoll.delete(0, tc.END)
                entRoll.insert(0, str(self.num))
        
                i += 1
                entRoll.update()
                time.sleep(.01)
        
        
        self.title("Kymo's Designs - Die Roller")
        self.config(bg = "#000000")
        #self.wm_iconbitmap("kymosdesingsicon.ico")
        
        entRoll = Entry(self, text = "", bg = "#00ff00", fg = "#000000", font = ("Arial", 50), width = 3)
        entRoll.grid(row = 0, column =0, rowspan = 7, padx = 5, pady = 5)
        
        btnCoin = Button(self, text = "Flip A Coin", bg = "#00ff00", fg = "#000000", activebackground  = "#000000", activeforeground = "#00ff00", font = ("Arial", 15), command = flipACoin)
        btnCoin.grid(row = 0, column = 1, ipadx = 9, padx = 15)
        
        btnD4 = Button(self, text = "4 Sided Die", bg = "#00ff00", fg = "#000000", activebackground  = "#000000", activeforeground = "#00ff00", font = ("Arial", 15), command = fourSidedDie)
        btnD4.grid(row = 1, column = 1, ipadx = 6)
        
        btnD6 = Button(self, text = "6 Sided Die", bg = "#00ff00", fg = "#000000", activebackground  = "#000000", activeforeground = "#00ff00", font = ("Arial", 15), command = sixSidedDie)
        btnD6.grid(row = 2, column = 1, ipadx = 6)
        
        btnD8 = Button(self, text = "8 Sided Die", bg = "#00ff00", fg = "#000000", activebackground  = "#000000", activeforeground = "#00ff00", font = ("Arial", 15), command = eightSidedDie)
        btnD8.grid(row = 3, column = 1, ipadx = 6)
        
        btnD10 = Button(self, text = "10 Sided Die", bg = "#00ff00", fg = "#000000", activebackground  = "#000000", activeforeground = "#00ff00", font = ("Arial", 15), command = tenSidedDie)
        btnD10.grid(row = 4, column = 1, padx = 5)
        
        btnD12 = Button(self, text = "12 Sided Die", bg = "#00ff00", fg = "#000000", activebackground  = "#000000", activeforeground = "#00ff00", font = ("Arial", 15), command = twelveSidedDie)
        btnD12.grid(row = 5, column = 1)
        
        btnD20 = Button(self, text = "20 Sided Die", bg = "#00ff00", fg = "#000000", activebackground  = "#000000", activeforeground = "#00ff00", font = ("Arial", 15), command = twentySidedDie)
        btnD20.grid(row = 6, column = 1)

        btnD50 = Button(self, text = "50 Sided Die", bg = "#00ff00", fg = "#000000", activebackground  = "#000000", activeforeground = "#00ff00", font = ("Arial", 15), command = fiftySidedDie)
        btnD50.grid(row = 7, column = 1)
        
        btnD100 = Button(self, text = "100 Sided Die", bg = "#00ff00", fg = "#000000", activebackground  = "#000000", activeforeground = "#00ff00", font = ("Arial", 15), command = oneHundredSidedDie)
        btnD100.grid(row = 8, column = 1)
        
        
        self.mainloop()
        
dr = DieRoller()
        
        
