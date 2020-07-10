from tkinter import *

CalcWindow = Tk()
CalcWindow.title('Calculator')
CalcWindow.resizable(False, False)
CalcWindow.configure(bg='#222831')

displayframe = Frame(CalcWindow, borderwidth=5, relief=SUNKEN)
displayframe.pack(fil='x', pady=10, padx=10)
displayframe.configure(bg='#222831')

entry = Entry(displayframe, borderwidth=10, relief=FLAT, font='10', bg='#77abb7', fg='black')
entry.pack(fill='x')

buttonframe = Frame(CalcWindow)
buttonframe.pack(fill='x', padx=30, pady=30)
buttonframe.configure(bg='#222831')

button8 = Button(buttonframe, text='8', width=5, height=2, bg='#000272', font='5', fg='white', activebackground='green')
button9 = Button(buttonframe, text='9', width=5, height=2, bg='#000272', font='5', fg='white', activebackground='green')
button7 = Button(buttonframe, text='7', width=5, height=2, bg='#000272', font='5', fg='white', activebackground='green')
button4 = Button(buttonframe, text='4', width=5, height=2, bg='#000272', font='5', fg='white', activebackground='green')
button5 = Button(buttonframe, text='5', width=5, height=2, bg='#000272', font='5', fg='white', activebackground='green')
button6 = Button(buttonframe, text='6', width=5, height=2, bg='#000272', font='5', fg='white', activebackground='green')
button1 = Button(buttonframe, text='1', width=5, height=2, bg='#000272', font='5', fg='white', activebackground='green')
button2 = Button(buttonframe, text='2', width=5, height=2, bg='#000272', font='5', fg='white', activebackground='green')
button3 = Button(buttonframe, text='3', width=5, height=2, bg='#000272', font='5', fg='white', activebackground='green')
buttondot = Button(buttonframe, text='.', width=5, height=2, bg='blue', font='5', fg='white', activebackground='green')
button0 = Button(buttonframe, text='0', width=5, height=2, bg='#000272', font='5', fg='white', activebackground='green')
buttondiv = Button(buttonframe, text='/', width=5, height=2, bg='blue', font='5', fg='white', activebackground='green')
buttonmul = Button(buttonframe, text='*', width=5, height=2, bg='blue', font='5', fg='white', activebackground='green')
buttonmin = Button(buttonframe, text='-', width=5, height=2, bg='blue', font='5', fg='white', activebackground='green')
buttonadd = Button(buttonframe, text='+', width=5, height=2, bg='blue', font='5', fg='white', activebackground='green')
buttonback = Button(buttonframe, text='C', width=5, height=2, bg='blue', font='5', fg='white', activebackground='green')
buttoneql = Button(buttonframe, text='=', width=5, height=2, bg='blue', font='5', fg='white', activebackground='green')
buttondel = Button(buttonframe, text='CLR', width=5, height=2, bg='blue', font='5', fg='white', activebackground='green')
buttonlb = Button(buttonframe, text='(', width=5, height=2, bg='blue', font='5', fg='white', activebackground='green')
buttonrb = Button(buttonframe, text=')', width=5, height=2, bg='blue', font='5', fg='white', activebackground='green')

button7.grid(row=0, column=0, padx=5, pady=5)
button8.grid(row=0, column=1, padx=5, pady=5)
button9.grid(row=0, column=2, padx=5, pady=5)
button4.grid(row=1, column=0, padx=5, pady=5)
button5.grid(row=1, column=1, padx=5, pady=5)
button6.grid(row=1, column=2, padx=5, pady=5)
button1.grid(row=2, column=0, padx=5, pady=5)
button2.grid(row=2, column=1, padx=5, pady=5)
button3.grid(row=2, column=2, padx=5, pady=5)
buttondot.grid(row=3, column=0, padx=5, pady=5)
button0.grid(row=3, column=1, padx=5, pady=5)
buttondiv.grid(row=0, column=3, padx=5, pady=5)
buttonmul.grid(row=1, column=3, padx=5, pady=5)
buttonmin.grid(row=2, column=3, padx=5, pady=5)
buttonadd.grid(row=3, column=3, padx=5, pady=5)
buttonback.grid(row=4, column=0, padx=5, pady=5)
buttoneql.grid(row=3, column=2, padx=5, pady=5)
buttondel.grid(row=4, column=1, padx=5, pady=5)
buttonlb.grid(row=4, column=2, padx=5, pady=5)
buttonrb.grid(row=4, column=3, padx=5, pady=5)

CalcWindow.mainloop()
