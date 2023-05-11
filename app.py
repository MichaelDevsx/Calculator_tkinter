#run the calculator app
import tkinter as tk
from tkinter import ttk
import tkinter.font as font




class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.resizable(False, False)

        self.number = []

        ttk.Label(
            self,
            text="Calculator"
        ).grid()


        self.display = tk.Entry(
            self,
            width=30,
            borderwidth=5
        )
        self.display.configure(state="normal")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.error = tk.StringVar()
        ttk.Label(
            self,
            textvariable=self.error
        ).grid(row=99, column=0, columnspan=4)

        #buttons
        self.button_1 = tk.Button(self, text="1", padx=40, pady=20, command= lambda: self.button_click(1))
        self.button_2 = tk.Button(self, text="2", padx=40, pady=20, command= lambda: self.button_click(2))
        self.button_3 = tk.Button(self, text="3", padx=40, pady=20, command= lambda: self.button_click(3))
        self.button_4 = tk.Button(self, text="4", padx=40, pady=20, command= lambda: self.button_click(4))
        self.button_5 = tk.Button(self, text="5", padx=40, pady=20, command= lambda: self.button_click(5))
        self.button_6 = tk.Button(self, text="6", padx=40, pady=20, command= lambda: self.button_click(6))
        self.button_7 = tk.Button(self, text="7", padx=40, pady=20, command= lambda: self.button_click(7))
        self.button_8 = tk.Button(self, text="8", padx=40, pady=20, command= lambda: self.button_click(8))
        self.button_9 = tk.Button(self, text="9", padx=40, pady=20, command= lambda: self.button_click(9))
        self.button_0 = tk.Button(self, text="0", padx=40, pady=20, command= lambda: self.button_click(0))

        # operations
        self.button_add = tk.Button(self, text="+", padx=39, pady=20, command= self.button_add)
        self.button_subtrack = tk.Button(self, text="-", padx=41, pady=20, command= self.button_subtrack)
        self.button_multiply = tk.Button(self, text="x", padx=40, pady=20, command= self.button_multiply)
        self.button_divide = tk.Button(self, text="/", padx=41, pady=20, command= self.button_divide)
        self.button_clear = tk.Button(self, text="C", padx=39, pady=20, command= self.button_clear)
        self.button_equal = tk.Button(self, text="=", padx=39, pady=20, command= self.button_equal)

        #Position of the buttons
        self.button_1.grid(row=1, column=0)
        self.button_2.grid(row=1, column=1)
        self.button_3.grid(row=1, column=2)
        self.button_4.grid(row=2, column=0)
        self.button_5.grid(row=2, column=1)
        self.button_6.grid(row=2, column=2)
        self.button_7.grid(row=3, column=0)
        self.button_8.grid(row=3, column=1)
        self.button_9.grid(row=3, column=2)
        self.button_0.grid(row=4, column=0)


        self.button_clear.grid(row=4, column=1)
        self.button_equal.grid(row=4, column=2)

        self.button_add.grid(row=1, column=3)
        self.button_subtrack.grid(row=2, column=3)
        self.button_multiply.grid(row=3 , column=3)
        self.button_divide.grid(row=4, column=3)

    def button_click(self, number):
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, str(current) + str(number))
        self.number.append(int(number))
        self.is_summing = True
        self.is_subtrackting = True
        self.is_multiplying = True
        self.is_diveding = True

    def button_add(self):
        if self.is_summing:
            current = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(0, str(current) + "+")
            self.number.append("+")
        self.is_summing = False


    def button_subtrack(self):
        if self.is_subtrackting:
            current = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(0, str(current) + "-")
            self.number.append("-")
            self.is_subtrackting = False

    def button_multiply(self):
        if self.is_multiplying:
            current = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(0, str(current) + "*")
            self.number.append("*")
            self.is_multiplying = False

    def button_divide(self):
        if self.is_diveding:
            current = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(0, str(current) + "*")
            self.number.append("*")
            self.is_diveding = False

    def button_clear(self):
        self.display.delete(0, tk.END)

    def button_equal(self):
        try:
            if self.is_summing:
                current = self.display.get()
                self.display.delete(0, tk.END)
                self.display.insert(0, eval(current))
                self.is_summing = False

            elif self.is_subtrackting:
                current = self.display.get()
                self.display.delete(0, tk.END)
                self.display.insert(0, eval(current))
                self.is_subtrackting = False

            elif self.is_multiplying:
                current = self.display.get()
                self.display.delete(0, tk.END)
                self.display.insert(0, eval(current))
                self.is_multiplying = False

            elif self.is_diveding:
                current = self.display.get()
                self.display.delete(0, tk.END)
                self.display.insert(0, eval(current))
                self.is_diveding = False
        except SyntaxError as error:
            return f"{self.error.set(error)}"
            
            
            

        

root = Application()
font.nametofont("TkDefaultFont").configure(size=14)

root.mainloop()