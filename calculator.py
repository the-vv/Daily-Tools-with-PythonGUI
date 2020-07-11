from tkinter import *


class Calc:
    def __init__(self):
        self.CalcWindow = Tk()
        self.CalcWindow.title('Calculator')
        self.CalcWindow.resizable(False, False)
        self.CalcWindow.configure(bg='#222831')

        self.displayframe = Frame(self.CalcWindow, borderwidth=5, relief=SUNKEN)
        self.displayframe.pack(fil='x', pady=10, padx=10)
        self.displayframe.configure(bg='#222831')

        self.entry = Entry(self.displayframe, borderwidth=10, relief=FLAT, font='10', bg='#77abb7', fg='black')
        self.entry.pack(fill='x')

        self.buttonframe = Frame(self.CalcWindow)
        self.buttonframe.pack(fill='x', padx=30, pady=30)
        self.buttonframe.configure(bg='#222831')

        self.button8 = Button(self.buttonframe, text='8', width=5, height=2, bg='#000272', font='5', fg='white',
                              activebackground='green',
                              command=lambda: self.addchar(8))
        self.button9 = Button(self.buttonframe, text='9', width=5, height=2, bg='#000272', font='5', fg='white',
                              activebackground='green', command=lambda: self.addchar(9))
        self.button7 = Button(self.buttonframe, text='7', width=5, height=2, bg='#000272', font='5', fg='white',
                              activebackground='green',
                              command=lambda: self.addchar(7))
        self.button4 = Button(self.buttonframe, text='4', width=5, height=2, bg='#000272', font='5', fg='white',
                              activebackground='green',
                              command=lambda: self.addchar(4))
        self.button5 = Button(self.buttonframe, text='5', width=5, height=2, bg='#000272', font='5', fg='white',
                              activebackground='green',
                              command=lambda: self.addchar(5))
        self.button6 = Button(self.buttonframe, text='6', width=5, height=2, bg='#000272', font='5', fg='white',
                              activebackground='green',
                              command=lambda: self.addchar(6))
        self.button1 = Button(self.buttonframe, text='1', width=5, height=2, bg='#000272', font='5', fg='white',
                              activebackground='green',
                              command=lambda: self.addchar(1))
        self.button2 = Button(self.buttonframe, text='2', width=5, height=2, bg='#000272', font='5', fg='white',
                              activebackground='green',
                              command=lambda: self.addchar(2))
        self.button3 = Button(self.buttonframe, text='3', width=5, height=2, bg='#000272', font='5', fg='white',
                              activebackground='green',
                              command=lambda: self.addchar(3))
        self.buttondot = Button(self.buttonframe, text='.', width=5, height=2, bg='blue', font='5', fg='white',
                                activebackground='green',
                                command=lambda: self.addchar('.'))
        self.button0 = Button(self.buttonframe, text='0', width=5, height=2, bg='#000272', font='5', fg='white',
                              activebackground='green',
                              command=lambda: self.addchar(0))
        self.buttondiv = Button(self.buttonframe, text='/', width=5, height=2, bg='blue', font='5', fg='white',
                                activebackground='green',
                                command=lambda: self.addchar('/'))
        self.buttonmul = Button(self.buttonframe, text='*', width=5, height=2, bg='blue', font='5', fg='white',
                                activebackground='green',
                                command=lambda: self.addchar('*'))
        self.buttonmin = Button(self.buttonframe, text='-', width=5, height=2, bg='blue', font='5', fg='white',
                                activebackground='green',
                                command=lambda: self.addchar('-'))
        self.buttonadd = Button(self.buttonframe, text='+', width=5, height=2, bg='blue', font='5', fg='white',
                                activebackground='green',
                                command=lambda: self.addchar('+'))
        self.buttonback = Button(self.buttonframe, text='C', width=5, height=2, bg='blue', font='5', fg='white',
                                 activebackground='green',
                                 command=lambda: self.addchar(8))
        self.buttoneql = Button(self.buttonframe, text='=', width=5, height=2, bg='blue', font='5', fg='white',
                                activebackground='green',
                                command=lambda: self.addchar(8))
        self.buttondel = Button(self.buttonframe, text='CLR', width=5, height=2, bg='blue', font='5', fg='white',
                                activebackground='green', command=lambda: self.clear())
        self.buttonlb = Button(self.buttonframe, text='(', width=5, height=2, bg='blue', font='5', fg='white',
                               activebackground='green',
                               command=lambda: self.addchar(8))
        self.buttonrb = Button(self.buttonframe, text=')', width=5, height=2, bg='blue', font='5', fg='white',
                               activebackground='green',
                               command=lambda: self.addchar(8))

        self.button7.grid(row=0, column=0, padx=5, pady=5)
        self.button8.grid(row=0, column=1, padx=5, pady=5)
        self.button9.grid(row=0, column=2, padx=5, pady=5)
        self.button4.grid(row=1, column=0, padx=5, pady=5)
        self.button5.grid(row=1, column=1, padx=5, pady=5)
        self.button6.grid(row=1, column=2, padx=5, pady=5)
        self.button1.grid(row=2, column=0, padx=5, pady=5)
        self.button2.grid(row=2, column=1, padx=5, pady=5)
        self.button3.grid(row=2, column=2, padx=5, pady=5)
        self.buttondot.grid(row=3, column=0, padx=5, pady=5)
        self.button0.grid(row=3, column=1, padx=5, pady=5)
        self.buttondiv.grid(row=0, column=3, padx=5, pady=5)
        self.buttonmul.grid(row=1, column=3, padx=5, pady=5)
        self.buttonmin.grid(row=2, column=3, padx=5, pady=5)
        self.buttonadd.grid(row=3, column=3, padx=5, pady=5)
        self.buttonback.grid(row=4, column=0, padx=5, pady=5)
        self.buttoneql.grid(row=3, column=2, padx=5, pady=5)
        self.buttondel.grid(row=4, column=1, padx=5, pady=5)
        self.buttonlb.grid(row=4, column=2, padx=5, pady=5)
        self.buttonrb.grid(row=4, column=3, padx=5, pady=5)

    def addchar(self, bchar):
        self.entry.insert(END, str(bchar))

    def clear(self):
        self.entry.delete(0, END)

    def execute(self):
        self.CalcWindow.mainloop()


def main():
    print(eval('5+9-2'))
    calculator = Calc()
    calculator.execute()


if __name__ == '__main__':
    main()
