from tkinter import *
from PIL import Image, ImageTk
import pyautogui

window = Tk()
window2 = Tk()

window.title("Despot's Mutation Simulator")
window.resizable(False, False)
window.iconbitmap("tree.ico")

window2.overrideredirect(True)
window2.attributes('-alpha',0.9)

# Variables
    # Points dépensés
my_points=0
    # Points dans chaque mutation
mutation_1_pts = mutation_2_pts = mutation_3_pts = mutation_4_pts = mutation_5_pts = mutation_6_pts = mutation_7_pts = mutation_8_pts = 0
mutation_9_pts = mutation_10_pts = mutation_11_pts = mutation_12_pts = mutation_13_pts = mutation_14_pts = mutation_15_pts = mutation_16_pts = 0
    # Level de chaque mutation
mutation_1_lvl = mutation_2_lvl = mutation_3_lvl = mutation_4_lvl = mutation_5_lvl = mutation_6_lvl = mutation_7_lvl = mutation_8_lvl = 0
mutation_9_lvl = mutation_10_lvl = mutation_11_lvl = mutation_12_lvl = mutation_13_lvl = mutation_14_lvl = mutation_15_lvl = mutation_16_lvl = 0

    # Distance entre label (design)
distance_btw_labels_Y=10
distance_btw_labels_X=10

# Infos barre du bas
status_label = Label(window, text="", bd=1, relief=SUNKEN, anchor=E)
status_label.grid(row=10,rowspan=10,column=9, columnspan=10)

# Fonctions
    # Positon du curseur
def mouse_pos(event):
    x, y = pyautogui.position()
    window2.geometry("+{}+{}".format(x+30, y+30))
    #print('{}, {}'.format(x, y))
window.bind('<Motion>', mouse_pos)

    # Curseur sur objet (mutation)
def on_enter_2_1(e):
    spell_name = "blabla"
    spell_last_effects = "blabla2"
    mutation_description = "Name : "+ spell_name +" \n \n Last Effect : " + spell_last_effects +" \n \n Effects : \n \n Next Effect : \n \n Cost : \n \n Next Cost : "
    Label(window2, text=mutation_description).grid(row=0,column=0)
    status_label.config(text="You are on it")
    window.deiconify()
    window2.deiconify()

    # Curseur plus sur objet (mutation)
def on_leave_2_1(e):
    status_label.config(text="You are NOT on it")
    window.deiconify()
    window2.withdraw()

def update_my_points_2_1():
    Label(window, text="Points \n spent : " + str(my_points), justify="center").grid(row=0,column=9)

def button_lclick_2_1(event):
    global mutation_1_pts
    global mutation_1_lvl
    global my_button_2_1
    global my_points
    if (mutation_1_pts == 0):
        mutation_1_pts += 5
        my_points += 5
        mutation_1_lvl += 1
        my_button_2_1.config(text=" LVL "+ str(mutation_1_lvl))
    elif (mutation_1_lvl == 1):
        mutation_1_pts += 15
        my_points += 15
        mutation_1_lvl += 1
        my_button_2_1.config(text=" LVL "+ str(mutation_1_lvl))
    update_my_points_2_1()

def button_rclick_2_1(event):
    global mutation_1_pts
    global mutation_1_lvl
    global my_button_2_1
    global my_points
    if (mutation_1_lvl == 1):
        mutation_1_pts -= 5
        my_points -= 5
        mutation_1_lvl -= 1
        my_button_2_1.config(text=" LVL "+ str(mutation_1_lvl))
    elif (mutation_1_lvl == 2):
        mutation_1_pts -= 15
        my_points -= 15
        mutation_1_lvl -= 1
        my_button_2_1.config(text=" LVL "+ str(mutation_1_lvl))
    update_my_points_2_1()

# Images
mutations_title = ImageTk.PhotoImage(Image.open("mutations_title.png"))
mutation_1 = ImageTk.PhotoImage(Image.open("mutation_1.png"))
mutation_2 = ImageTk.PhotoImage(Image.open("mutation_2.png"))
mutation_3 = ImageTk.PhotoImage(Image.open("mutation_3.png"))
mutation_4 = ImageTk.PhotoImage(Image.open("mutation_4.png"))
mutation_5 = ImageTk.PhotoImage(Image.open("mutation_5.png"))
mutation_6 = ImageTk.PhotoImage(Image.open("mutation_6.png"))
mutation_7 = ImageTk.PhotoImage(Image.open("mutation_7.png"))
mutation_8 = ImageTk.PhotoImage(Image.open("mutation_8.png"))
mutation_9 = ImageTk.PhotoImage(Image.open("mutation_9.png"))
mutation_10 = ImageTk.PhotoImage(Image.open("mutation_10.png"))
mutation_11 = ImageTk.PhotoImage(Image.open("mutation_11.png"))
mutation_12 = ImageTk.PhotoImage(Image.open("mutation_12.png"))
mutation_13 = ImageTk.PhotoImage(Image.open("mutation_13.png"))
mutation_14 = ImageTk.PhotoImage(Image.open("mutation_14.png"))
mutation_15 = ImageTk.PhotoImage(Image.open("mutation_15.png"))
mutation_16 = ImageTk.PhotoImage(Image.open("mutation_16.png"))
between_1and2 = ImageTk.PhotoImage(Image.open("between_1and2.png"))

# Titre (row=0, center)
my_label_title = Label(window, image=mutations_title, justify="center").grid(row=0,column=0,columnspan=12)

# Points dépensés
my_label_points = Label(window, text="Points \n spent : " + str(my_points), justify="center").grid(row=0,column=9)

# Distance entre les labels
    # Axes verticaux
my_label_1_2 = Label(window, text="", padx=distance_btw_labels_Y).grid(row=1,column=2)
my_label_1_4 = Label(window, text="", padx=distance_btw_labels_Y).grid(row=1,column=4)
my_label_1_6 = Label(window, text="", padx=distance_btw_labels_Y).grid(row=1,column=6)
my_label_1_8 = Label(window, text="", padx=distance_btw_labels_Y).grid(row=1,column=8)
my_label_1_10 = Label(window, text="", padx=distance_btw_labels_Y).grid(row=1,column=10)
    # Axes horizontaux
my_label_1 = Label(window, text="", padx=distance_btw_labels_X).grid(row=1)
my_label_3 = Label(window, text="", padx=distance_btw_labels_X).grid(row=3)
my_label_5 = Label(window, text="", padx=distance_btw_labels_X).grid(row=5)
my_label_7 = Label(window, text="", padx=distance_btw_labels_X).grid(row=7)
my_label_9 = Label(window, text="", padx=distance_btw_labels_X).grid(row=9)

# LABELS & BOUTONS
my_button_2_1 = Button(window, text=" LVL "+ str(mutation_1_pts), image=mutation_1, compound="bottom")
my_button_2_1.grid(row=2,column=1)
my_button_2_1.bind("<Enter>", on_enter_2_1)
my_button_2_1.bind("<Leave>", on_leave_2_1)
my_button_2_1.bind("<Button-1>", button_lclick_2_1)
my_button_2_1.bind("<Button-3>", button_rclick_2_1)

my_button_2_3 = Button(window, text=" LVL "+ str(mutation_1_pts), image=mutation_2, compound="bottom")
my_button_2_3.grid(row=2,column=3)
my_button_2_3.bind("<Enter>", on_enter_2_1)
my_button_2_3.bind("<Leave>", on_leave_2_1)

my_button_2_5 = Button(window, text=" LVL "+ str(mutation_1_pts), image=mutation_3, compound="bottom")
my_button_2_5.grid(row=2,column=5)
my_button_2_5.bind("<Enter>", on_enter_2_1)
my_button_2_5.bind("<Leave>", on_leave_2_1)

my_button_4_1 = Button(window, text=" LVL "+ str(mutation_1_pts), image=mutation_4, compound="bottom")
my_button_4_1.grid(row=4,column=1)
my_button_4_1.bind("<Enter>", on_enter_2_1)
my_button_4_1.bind("<Leave>", on_leave_2_1)

my_button_4_3 = Button(window, text=" LVL "+ str(mutation_1_pts), image=mutation_5, compound="bottom")
my_button_4_3.grid(row=4,column=3)
my_button_4_3.bind("<Enter>", on_enter_2_1)
my_button_4_3.bind("<Leave>", on_leave_2_1)

my_button_4_5 = Button(window, text=" LVL "+ str(mutation_1_pts), image=mutation_6, compound="bottom")
my_button_4_5.grid(row=4,column=5)
my_button_4_5.bind("<Enter>", on_enter_2_1)
my_button_4_5.bind("<Leave>", on_leave_2_1)

my_button_4_7 = Button(window, text=" LVL "+ str(mutation_1_pts), image=mutation_7, compound="bottom")
my_button_4_7.grid(row=4,column=7)
my_button_4_7.bind("<Enter>", on_enter_2_1)
my_button_4_7.bind("<Leave>", on_leave_2_1)

my_button_4_9 = Button(window, text=" LVL "+ str(mutation_1_pts), image=mutation_8, compound="bottom")
my_button_4_9.grid(row=4,column=9)
my_button_4_9.bind("<Enter>", on_enter_2_1)
my_button_4_9.bind("<Leave>", on_leave_2_1)

my_button_6_1 = Button(window, text=" LVL "+ str(mutation_1_pts), image=mutation_9, compound="bottom")
my_button_6_1.grid(row=6,column=1)
my_button_6_1.bind("<Enter>", on_enter_2_1)
my_button_6_1.bind("<Leave>", on_leave_2_1)

my_button_6_3 = Button(window, text=" LVL "+ str(mutation_1_pts), image=mutation_10, compound="bottom")
my_button_6_3.grid(row=6,column=3)
my_button_6_3.bind("<Enter>", on_enter_2_1)
my_button_6_3.bind("<Leave>", on_leave_2_1)

my_button_6_5 = Button(window, text=" LVL "+ str(mutation_1_pts), image=mutation_11, compound="bottom")
my_button_6_5.grid(row=6,column=5)
my_button_6_5.bind("<Enter>", on_enter_2_1)
my_button_6_5.bind("<Leave>", on_leave_2_1)

my_button_8_1 = Button(window, text=" LVL "+ str(mutation_1_pts), image=mutation_12, compound="bottom")
my_button_8_1.grid(row=8,column=1)
my_button_8_1.bind("<Enter>", on_enter_2_1)
my_button_8_1.bind("<Leave>", on_leave_2_1)

my_button_8_3 = Button(window, text=" LVL "+ str(mutation_1_pts), image=mutation_13, compound="bottom")
my_button_8_3.grid(row=8,column=3)
my_button_8_3.bind("<Enter>", on_enter_2_1)
my_button_8_3.bind("<Leave>", on_leave_2_1)

my_button_8_5 = Button(window, text=" LVL "+ str(mutation_1_pts), image=mutation_14, compound="bottom")
my_button_8_5.grid(row=8,column=5)
my_button_8_5.bind("<Enter>", on_enter_2_1)
my_button_8_5.bind("<Leave>", on_leave_2_1)

my_button_8_7 = Button(window, text=" LVL "+ str(mutation_1_pts), image=mutation_15, compound="bottom")
my_button_8_7.grid(row=8,column=7)
my_button_8_7.bind("<Enter>", on_enter_2_1)
my_button_8_7.bind("<Leave>", on_leave_2_1)

my_button_8_9 = Button(window, text=" LVL "+ str(mutation_1_pts), image=mutation_11, compound="bottom")
my_button_8_9.grid(row=8,column=9)
my_button_8_9.bind("<Enter>", on_enter_2_1)
my_button_8_9.bind("<Leave>", on_leave_2_1)

# Description des mutations

window.mainloop()