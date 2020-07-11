import tkinter as tk
import calculator as calc


class ToolsWindow:
    def __init__(self):
        self.mainWindow = tk.Tk()
        self.mainWindow.title('Daily Toolkit')
        self.mainWindow.configure(bg='#222831')

        self.headdingframe = tk.Frame(self.mainWindow, borderwidth=0)
        self.headdingframe.pack(fil='x', pady=10, padx=10)
        self.headdingframe.configure(bg='#222831')

        self.mainheadding = tk.Label(self.headdingframe, text='Your Daily Tools are Here', bg='#222831', fg='white',
                                     font='5')
        self.mainheadding.pack(side=tk.LEFT)

        self.buttonframe = tk.Frame(self.mainWindow, borderwidth=0)
        self.buttonframe.pack(fil='x', pady=10, padx=10)
        self.buttonframe.configure(bg='#222831')

        self.calcbutton = tk.Button(self.buttonframe, text='Simple\nCalculator', width=10, height=5, bg='#000272', font='5',
                                    fg='white', activebackground='green', command=self.launchcalc)
        self.calcbutton.pack()

    def execute(self):
        self.mainWindow.mainloop()

    def launchcalc(self):
        calc.main()


def main():
    mainwindow = ToolsWindow()
    mainwindow.execute()


if __name__ == '__main__':
    main()
