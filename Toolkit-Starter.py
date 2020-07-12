import tkinter as tk
import calculator as calc


class ToolsWindow:
    def __init__(self):
        self.mainWindow = tk.Tk()
        self.mainWindow.title('Daily Toolkit')
        self.mainWindow.configure(bg='#222831')
        self.mainWindow.resizable(False, False)

        self.headdingframe = tk.Frame(self.mainWindow, borderwidth=0)
        self.headdingframe.pack(fil='x', pady=10, padx=10)
        self.headdingframe.configure(bg='#222831')

        self.mainheadding = tk.Label(self.headdingframe, text='Your Daily Tools are Here', bg='#222831', fg='white',
                                     font='5').pack()

        self.buttonframe = tk.Frame(self.mainWindow, borderwidth=0)
        self.buttonframe.pack(fil='x', pady=10, padx=10)
        self.buttonframe.configure(bg='#222831')

        self.calcbutton = tk.Button(self.buttonframe, text='Calculator', width=10, height=5, bg='#000272',
                                    font='5', fg='white', activebackground='green',
                                    command=self.launchcalc).pack(padx='10', pady='10')

        self.mainheadding = tk.Label(self.buttonframe, text='More tools are coming soon!', bg='#222831',
                                     fg='white').pack(pady='10')

    def execute(self):
        self.mainWindow.mainloop()

    def launchcalc(self):
        self.mainWindow.quit()
        calculator = calc.Calc()
        calculator.execute()
        del calculator


def main():
    mainwindow = ToolsWindow()
    mainwindow.execute()


if __name__ == '__main__':
    main()
