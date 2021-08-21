from tkinter import *
root = Tk()

root.title("Despot's Mutation Simulator")
root.iconbitmap("tree.ico")
root.geometry("500x300")

my_entry1 = Entry(root, width=25, fg='red')
my_entry1.grid(row=3,column=4)

def my_click1():
    Label(root, text="you click on it", fg='white', bg='red').grid(row=6,column=1)

def my_click2():
    string_1=my_entry1.get()
    Label(root, text="your name is "+ string_1).grid(row=5,column=4)
    my_entry1.delete(0,END)
    

my_label1 = Label(root, text="hello").grid(row=0,column=1)
my_label2 = Label(root, text="how are you ?").grid(row=2,column=2)
my_label3 = Label(root, text="enter you name").grid(row=2,column=4)
my_button1 = Button(root, text="LVL 1", command=my_click1, padx=25, pady=25).grid(row=3,column=2)
my_button2 = Button(root, text="execute", command=my_click2, padx=25, pady=25).grid(row=4,column=4)
my_radiobutton1 = Radiobutton(root, text="Option 1", variable="", value=1).grid(row=6,column=6)

root.mainloop()