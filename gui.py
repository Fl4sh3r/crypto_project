from tkinter import *


class Gui:
    root = Tk()

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

    def create_window(self, x, y):
        self.root.geometry(str(x) + "x" + str(y))
        self.root.pack_propagate(0)
        self.root.title("Crypto stats")
        self.root.resizable(0, 1)

    def create_grid(self, text):

        head = "rank,crypto name,symbol,price(usd),total supply,total price"
        x = 0
        for j in range(self.columns):
            head2 = head.split(',')[x]
            label = Label(self.root, text=head2, borderwidth=2, relief='solid',  bg = "lawn green")
            if x == 0:
                label.config(width=3)
            elif x == 1:
                label.config(width=15)
            elif x == 2:
                label.config(width=4)
            elif x == 3:
                label.config(width=15)
            elif x == 4:
                label.config(width=14)
            elif x == 5:
                label.config(width=15)
            x += 1
            label.grid(row=0, column=j, sticky=W, ipadx=7, padx=1, pady=2, ipady=3)
        y = -1
        for i in range(self.rows):
            x = 0
            y += 1
            for j in range(self.columns):
                text1 = text[y].split('|')[x]

                if x % 2 == 0:
                    label = Label(self.root, text=text1, borderwidth=2, relief='solid', bg = "turquoise1")
                else:
                    label = Label(self.root, text=text1, borderwidth=2, relief='solid', bg='pale green')
                if x == 0:
                    label.config(width=3)
                elif x == 1:
                    label.config(width=15)
                elif x == 2:
                    label.config(width=4)
                elif x == 3:
                    label.config(width=15)
                elif x == 4:
                    label.config(width=14)
                elif x == 5:
                    label.config(width=15)

                label.grid(row=i+1, column=j, sticky=W, ipadx=7, padx=1, pady=2, ipady=3)
                x += 1