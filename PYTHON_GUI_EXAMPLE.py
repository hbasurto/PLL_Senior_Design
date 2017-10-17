import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *

class MainGUI(Frame):
    def __init__(self, master):
        self.master = master
        Frame.__init__(self, master)
        self.grid()
        self.master.title("PLL TOOL")

        for r in range(20):
            self.master.rowconfigure(r, weight=1)    
        for c in range(20):
            self.master.columnconfigure(c, weight=1)
            
        Frame1 = Frame(master, bg="white", width=100, height=100)
        Frame1.grid(row = 0, column = 0, rowspan = 10, columnspan = 10, sticky = W+E+N+S) 
        Frame2 = Frame(master, width=100, height=100)
        Frame2.grid(row = 10, column = 0, rowspan = 10, columnspan = 10, sticky = W+E+N+S)
        Frame3 = Frame(master, bg="gray", width=100, height=10)
        Frame3.grid(row = 0, column = 10, rowspan = 10, columnspan = 10, sticky = W+E+N+S)
        Frame4 = Frame(master, bg="black", width=100, height=10)
        Frame4.grid(row = 10, column = 10, rowspan = 10, columnspan = 10, sticky = W+E+N+S)
        
        
        self.label1 = ttk.Label(Frame1, text="This is in the Frame", font="Arial 10 bold")
        self.label1.grid(in_=Frame1, row=0, column=0)        
        
        self.label2 = ttk.Label(master, text="This is not", font="Arial 10 bold")
        self.label2.grid(row=0, column=0, columnspan = 10)

        self.close_button = Button(master, text=" Close ", command=master.destroy)
        self.close_button.grid(row=2, column=2, sticky=W + E)
        
        
        self.label3 = ttk.Label(Frame4, text="Enter the Number 5", font="Arial 10 bold")
        self.label3.grid(in_=Frame4, row=0, column=0)
        
        self.enter_button = Button(Frame4, text=" Enter ", command=self.button_pressed)
        self.enter_button.grid(in_=Frame4, row=1, column=0, sticky=W + E)
        
        self.entry = Entry(Frame4, width=10)
        self.entry.grid(in_=Frame4, row=0, column=1, sticky=W + E)

        global text_value
        
        text_value= ttk.Label(Frame4, text="", font="Arial 10 bold")
        text_value.grid(in_=Frame4, row=2, column=0, columnspan = 10)
        
        self.try_button = Button(Frame3, text=" Try Clicking This Button ", command=self.new_window)
        self.try_button.grid(in_=Frame3, row=10, column=0, sticky=W + E)
        
        self.label4 = ttk.Label(Frame2, text="Multiply Two Numbers", font="Arial 10 bold")
        self.label4.grid(in_=Frame2, row=0, column=0)
        
        self.label5 = ttk.Label(Frame2, text="Enter X Value", font="Arial 10 bold")
        self.label5.grid(in_=Frame2, row=1, column=0)
        self.entry2 = Entry(Frame2, width=10)
        self.entry2.grid(in_=Frame2, row=1, column=1, sticky=W + E)
        
        self.label6 = ttk.Label(Frame2, text="Enter Y Value", font="Arial 10 bold")
        self.label6.grid(in_=Frame2, row=2, column=0)
        self.entry3 = Entry(Frame2, width=10)
        self.entry3.grid(in_=Frame2, row=2, column=1, sticky=W + E)
        
        self.enter_button2 = Button(Frame2, text=" Enter ", command=self.multiply_pressed)
        self.enter_button2.grid(in_=Frame2, row=3, column=0, sticky=W + E)  
        
        global multiply_value        
        
        self.label7 = ttk.Label(Frame2, text="Your answer is ...", font="Arial 10 bold")
        self.label7.grid(in_=Frame2, row=4, column=0)
        multiply_value= ttk.Label(Frame2, text="", font="Arial 10 bold")
        multiply_value.grid(in_=Frame2, row=4, column=1, columnspan = 10)
        
    def button_pressed(self):
        global button_input
        button_input = self.entry.get()
        global text_value
        
        if button_input == '5':
            text_value.config(text="Nice Job!")
        else:
            text_value.config(text="Try Again!!!")
            
    def multiply_pressed(self):
        global button_inputx
        global button_inputy
        button_inputx = self.entry2.get()
        button_inputy = self.entry3.get()
        global multiply_value
        output_value = float(button_inputx) * float(button_inputy)
        multiply_value.config(text=str(output_value))

    def new_window(self):
        root10 = Toplevel(self.master)
        root10.geometry("250x50")
        pls_label = Label(root10, text="You clicked the button", font=24, fg="red")
        pls_label.pack()

if __name__ == '__main__':
    root = tk.Tk()
    my_gui = MainGUI(root)
    root.geometry('750x750')
    root.mainloop()
