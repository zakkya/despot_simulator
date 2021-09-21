from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import pyautogui

# -- FENETRES --
window = Tk()
window2 = Tk()

window.title("Despot's Mutation Simulator")
window.resizable(False, False)
window.iconbitmap("tree.ico")

window2.overrideredirect(True)
window2.attributes('-alpha',0.9)

# -- VARIABLES --
# Spended points
my_points=0
# Points in each mutation
mutation_2_1_pts = mutation_2_3_pts = mutation_2_5_pts = mutation_2_7_pts = mutation_4_1_pts = mutation_4_3_pts = mutation_4_5_pts = mutation_4_7_pts = 0
mutation_4_9_pts = mutation_6_3_pts = mutation_6_5_pts = mutation_6_7_pts = mutation_8_1_pts = mutation_8_3_pts = mutation_8_5_pts = mutation_8_7_pts = 0
# Mutation's level
mutation_2_1_lvl = mutation_2_3_lvl = mutation_2_5_lvl = mutation_2_7_lvl = mutation_4_1_lvl = mutation_4_3_lvl = mutation_4_5_lvl = mutation_4_7_lvl = 0
mutation_4_9_lvl = mutation_6_3_lvl = mutation_6_5_lvl = mutation_6_7_lvl = mutation_8_1_lvl = mutation_8_3_lvl = mutation_8_5_lvl = mutation_8_7_lvl = 0
# Mutation's name
mutation_name=["","THRILL ADDICTION","SALE!","WIDE CHOICE","MORE ALTARS","MANA REGENERATION","FAST RELOAD","MANA BONUS","MAGIC DEFENSE BONUS","TOPOCHLORIANS",
               "MGLW'NAFH","WGAH'NAGL","FHTAGN","THICK SKIN","HEALTH BONUS","ATTACK SPEED BONUS","VALOR"]
# Mutation's description
mutation_description = ""
# Labels
my_button_2_1 = my_button_2_3 = my_button_2_5 = my_button_2_7 = my_button_4_1 = my_button_4_3 = my_button_4_5 = my_button_4_7 =  Button()
my_button_4_9 = my_button_6_1 = my_button_6_3 = my_button_6_5 = my_button_8_1 = my_button_8_3 = my_button_8_5 = my_button_8_7 = Button()
# Distance between label (design)
distance_btw_labels_X=5
distance_btw_labels_Y=5

# -- ASSETS --
# Images
mutations_title = ImageTk.PhotoImage(Image.open("mutations_title.png"))
mutation_2_1 = ImageTk.PhotoImage(Image.open("mutation_2_1.png"))
mutation_2_3 = ImageTk.PhotoImage(Image.open("mutation_2_3.png"))
mutation_2_5 = ImageTk.PhotoImage(Image.open("mutation_2_5.png"))
mutation_2_7 = ImageTk.PhotoImage(Image.open("mutation_2_7.png"))
mutation_4_1 = ImageTk.PhotoImage(Image.open("mutation_4_1.png"))
mutation_4_3 = ImageTk.PhotoImage(Image.open("mutation_4_3.png"))
mutation_4_5 = ImageTk.PhotoImage(Image.open("mutation_4_5.png"))
mutation_4_7 = ImageTk.PhotoImage(Image.open("mutation_4_7.png"))
mutation_4_9 = ImageTk.PhotoImage(Image.open("mutation_4_9.png"))
mutation_6_3 = ImageTk.PhotoImage(Image.open("mutation_6_3.png"))
mutation_6_5 = ImageTk.PhotoImage(Image.open("mutation_6_5.png"))
mutation_6_7 = ImageTk.PhotoImage(Image.open("mutation_6_7.png"))
mutation_8_1 = ImageTk.PhotoImage(Image.open("mutation_8_1.png"))
mutation_8_3 = ImageTk.PhotoImage(Image.open("mutation_8_3.png"))
mutation_8_5 = ImageTk.PhotoImage(Image.open("mutation_8_5.png"))
mutation_8_7 = ImageTk.PhotoImage(Image.open("mutation_8_7.png"))
between_1and2 = ImageTk.PhotoImage(Image.open("between_1and2.png"))

# -- AUTRES --
# Infos bar (bottom)
#status_label = Label(window, text="", bd=1, relief=SUNKEN, anchor=E)
#status_label.grid(row=10,rowspan=10,column=9)

# -- FONCTIONS --
# Mouse position
def mouse_pos(event):
    x, y = pyautogui.position()
    window2.geometry("+{}+{}".format(x+30, y+30))
    #print('{}, {}'.format(x, y))
window.bind('<Motion>', mouse_pos)

# Mouse on object (mutation)
def on_enter_2_1(e):
    spell_name = mutation_name[1]
    if mutation_2_1_lvl == 0:
        spell_cost = "5"
        spell_effects = ""
        spell_next_effects = "Restocking the shop is 1 token cheaper"
    elif mutation_2_1_lvl == 1:
        spell_cost = "10"
        spell_effects = "Restocking the shop is 1 token cheaper"
        spell_next_effects = "Restocking the shop is 2 tokens cheaper"
    elif mutation_2_1_lvl == 2:
        spell_cost = "10"
        spell_effects = "Restocking the shop is 1 token cheaper"
        spell_next_effects = "Restocking the shop is 2 tokens cheaper"
    mutation_description = "Name : "+ spell_name +" \n \n Effects : " + spell_effects + "\n \n Next Effect : " + spell_next_effects + " \n \n Next Cost : " + spell_cost
    Label(window2, text=mutation_description).grid(row=0,column=0)
    window2.deiconify()
    
def on_enter_2_3(e):
    spell_name = mutation_name[2]
    if mutation_2_3_lvl == 0:
        spell_cost = "5"
        spell_effects = ""
        spell_next_effects = "A random item costs 25% cheaper in each stock"
    elif mutation_2_3_lvl == 1:
        spell_cost = "10"
        spell_effects = "A random item costs 25% cheaper in each stock"
        spell_next_effects = "A random item costs 35% cheaper in each stock"
    mutation_description = "Name : "+ spell_name +" \n \n Effects : " + spell_effects + "\n \n Next Effect : " + spell_next_effects + " \n \n Next Cost : " + spell_cost
    Label(window2, text=mutation_description).grid(row=0,column=0)
    window2.deiconify()
    
def on_enter_2_5(e):
    spell_name = mutation_name[3]
    if mutation_2_5_lvl == 0:
        spell_cost = "5"
        spell_effects = ""
        spell_next_effects = "Increase free Mutation rerool at the altar by 1"
    elif mutation_2_5_lvl == 1:
        spell_cost = "10"
        spell_effects = "Increase free Mutation rerool at the altar by 1"
        spell_next_effects = "Increase free Mutation rerool at the altar by 2"
    mutation_description = "Name : "+ spell_name +" \n \n Effects : " + spell_effects + "\n \n Next Effect : " + spell_next_effects + " \n \n Next Cost : " + spell_cost
    Label(window2, text=mutation_description).grid(row=0,column=0)
    window2.deiconify()
    
def on_enter_2_7(e):
    spell_name = mutation_name[4]
    if mutation_2_7_lvl == 0:
        spell_cost = "5"
        spell_effects = ""
        spell_next_effects = "1 more altar room per level"
    elif mutation_2_7_lvl == 1:
        spell_cost = "10"
        spell_effects = "1 more altar room per level"
        spell_next_effects = "2 more altar rooms per level"
    mutation_description = "Name : "+ spell_name +" \n \n Effects : " + spell_effects + "\n \n Next Effect : " + spell_next_effects + " \n \n Next Cost : " + spell_cost
    Label(window2, text=mutation_description).grid(row=0,column=0)
    window2.deiconify()
      
def on_enter_4_1(e):
    spell_name = mutation_name[5]
    if mutation_4_1_lvl == 0:
        spell_cost = "5"
        spell_effects = ""
        spell_next_effects = "Restore 1 mana every 0,5s"
    elif mutation_4_1_lvl == 1:
        spell_cost = "10"
        spell_effects = "Restore 1 mana every 0,5s"
        spell_next_effects = "Restore 2 mana every 0,5s"
    mutation_description = "Name : "+ spell_name +" \n \n Effects : " + spell_effects + "\n \n Next Effect : " + spell_next_effects + " \n \n Next Cost : " + spell_cost
    Label(window2, text=mutation_description).grid(row=0,column=0)
    window2.deiconify()
    
def on_enter_4_3(e):
    spell_name = mutation_name[6]
    if mutation_4_3_lvl == 0:
        spell_cost = "5"
        spell_effects = ""
        spell_next_effects = "All ability cooldowns are 1,25 times lower"
    elif mutation_4_3_lvl == 1:
        spell_cost = "10"
        spell_effects = "All ability cooldowns are 1,25 times lower"
        spell_next_effects = "All ability cooldowns are 1,35 times lower"
    mutation_description = "Name : "+ spell_name +" \n \n Effects : " + spell_effects + "\n \n Next Effect : " + spell_next_effects + " \n \n Next Cost : " + spell_cost
    Label(window2, text=mutation_description).grid(row=0,column=0)
    window2.deiconify()
    
def on_enter_4_5(e):
    spell_name = mutation_name[7]
    if mutation_4_5_lvl == 0:
        spell_cost = "5"
        spell_effects = ""
        spell_next_effects = "All units receive +30 to mana"
    elif mutation_4_5_lvl == 1:
        spell_cost = "10"
        spell_effects = "All units receive +30 to mana"
        spell_next_effects = "All units receive +50 to mana"
    mutation_description = "Name : "+ spell_name +" \n \n Effects : " + spell_effects + "\n \n Next Effect : " + spell_next_effects + " \n \n Next Cost : " + spell_cost
    Label(window2, text=mutation_description).grid(row=0,column=0)
    window2.deiconify()
    
def on_enter_4_7(e):
    spell_name = mutation_name[8]
    if mutation_4_7_lvl == 0:
        spell_cost = "5"
        spell_effects = ""
        spell_next_effects = "All units receive +20% to magic defense"
    elif mutation_4_7_lvl == 1:
        spell_cost = "10"
        spell_effects = "All units receive +20% to magic defense"
        spell_next_effects = "All units receive +30% to magic defense"
    mutation_description = "Name : "+ spell_name +" \n \n Effects : " + spell_effects + "\n \n Next Effect : " + spell_next_effects + " \n \n Next Cost : " + spell_cost
    Label(window2, text=mutation_description).grid(row=0,column=0)
    window2.deiconify()
    
def on_enter_4_9(e):
    spell_name = mutation_name[9]
    if mutation_4_9_lvl == 0:
        spell_cost = "5"
        spell_effects = ""
        spell_next_effects = "Magic Damage increased by 40%"
    elif mutation_4_9_lvl == 1:
        spell_cost = "10"
        spell_effects = "Magic Damage increased by 40%"
        spell_next_effects = "Magic Damage increased by 60%"
    mutation_description = "Name : "+ spell_name +" \n \n Effects : " + spell_effects + "\n \n Next Effect : " + spell_next_effects + " \n \n Next Cost : " + spell_cost
    Label(window2, text=mutation_description).grid(row=0,column=0)
    window2.deiconify()
    
def on_enter_6_3(e):
    spell_name = mutation_name[10]
    if mutation_6_3_lvl == 0:
        spell_cost = "10"
        spell_effects = ""
        spell_next_effects = "Summoned creatures receive +50% to health"
    elif mutation_6_3_lvl == 1:
        spell_cost = "15"
        spell_effects = "Summoned creatures receive +50% to health"
        spell_next_effects = "Summoned creatures receive +70% to health"
    mutation_description = "Name : "+ spell_name +" \n \n Effects : " + spell_effects + "\n \n Next Effect : " + spell_next_effects + " \n \n Next Cost : " + spell_cost
    Label(window2, text=mutation_description).grid(row=0,column=0)
    window2.deiconify()
    
def on_enter_6_5(e):
    spell_name = mutation_name[11]
    if mutation_6_5_lvl == 0:
        spell_cost = "10"
        spell_effects = ""
        spell_next_effects = "Summoned creatures receive +30% Atk Spd"
    elif mutation_6_5_lvl == 1:
        spell_cost = "15"
        spell_effects = "Summoned creatures receive +30% Atk Spd"
        spell_next_effects = "Summoned creatures receive +50% Atk Spd"
    mutation_description = "Name : "+ spell_name +" \n \n Effects : " + spell_effects + "\n \n Next Effect : " + spell_next_effects + " \n \n Next Cost : " + spell_cost
    Label(window2, text=mutation_description).grid(row=0,column=0)
    window2.deiconify()
    
def on_enter_6_7(e):
    spell_name = mutation_name[12]
    if mutation_6_7_lvl == 0:
        spell_cost = "10"
        spell_effects = ""
        spell_next_effects = "Summoned creatures receive +30% Attack Power"
    elif mutation_6_7_lvl == 1:
        spell_cost = "15"
        spell_effects = "Summoned creatures receive +30% Attack Power"
        spell_next_effects = "Summoned creatures receive +50% Attack Power"
    mutation_description = "Name : "+ spell_name +" \n \n Effects : " + spell_effects + "\n \n Next Effect : " + spell_next_effects + " \n \n Next Cost : " + spell_cost
    Label(window2, text=mutation_description).grid(row=0,column=0)
    window2.deiconify()
    
def on_enter_8_1(e):
    spell_name = mutation_name[13]
    if mutation_8_1_lvl == 0:
        spell_cost = "5"
        spell_effects = ""
        spell_next_effects = "The Newbies class receives +15 to armor"
    elif mutation_8_1_lvl == 1:
        spell_cost = "15"
        spell_effects = "The Newbies class receives +15 to armor"
        spell_next_effects = "The Newbies class receives +25 to armor"
    mutation_description = "Name : "+ spell_name +" \n \n Effects : " + spell_effects + "\n \n Next Effect : " + spell_next_effects + " \n \n Next Cost : " + spell_cost
    Label(window2, text=mutation_description).grid(row=0,column=0)
    window2.deiconify()
    
def on_enter_8_3(e):
    spell_name = mutation_name[14]
    if mutation_8_3_lvl == 0:
        spell_cost = "5"
        spell_effects = ""
        spell_next_effects = "All humans receive +25% to health"
    elif mutation_8_3_lvl == 1:
        spell_cost = "15"
        spell_effects = "All humans receive +25% to health"
        spell_next_effects = "All humans receive +35% to health"
    mutation_description = "Name : "+ spell_name +" \n \n Effects : " + spell_effects + "\n \n Next Effect : " + spell_next_effects + " \n \n Next Cost : " + spell_cost
    Label(window2, text=mutation_description).grid(row=0,column=0)
    window2.deiconify()
    
def on_enter_8_5(e):
    spell_name = mutation_name[13]
    if mutation_8_1_lvl == 0:
        spell_cost = "5"
        spell_effects = ""
        spell_next_effects = "All humans receive +10% to Atk Spd"
    elif mutation_8_1_lvl == 1:
        spell_cost = "15"
        spell_effects = "All humans receive +10% to Atk Spd"
        spell_next_effects = "All humans receive +20% to Atk Spd"
    mutation_description = "Name : "+ spell_name +" \n \n Effects : " + spell_effects + "\n \n Next Effect : " + spell_next_effects + " \n \n Next Cost : " + spell_cost
    Label(window2, text=mutation_description).grid(row=0,column=0)
    window2.deiconify()
    
def on_enter_8_7(e):
    spell_name = mutation_name[13]
    if mutation_8_1_lvl == 0:
        spell_cost = "5"
        spell_effects = ""
        spell_next_effects = "If there are more opponents than human,\neach human gets a +5 armor per extra opponent"
    elif mutation_8_1_lvl == 1:
        spell_cost = "15"
        spell_effects = "If there are more opponents than human,\neach human gets a +5 armor per extra opponent"
        spell_next_effects = "The Newbies class receives +25 to armor"
    mutation_description = "Name : "+ spell_name +" \n \n Effects : " + spell_effects + "\n \n Next Effect : " + spell_next_effects + " \n \n Next Cost : " + spell_cost
    Label(window2, text=mutation_description).grid(row=0,column=0)
    window2.deiconify()
    
# Mouse when not on object (mutation)
def on_leave(e):
    notext = ""
    window.deiconify()
    window2.withdraw()

def update_my_points():
    Label(window, text="Points \n spent : " + str(my_points), justify="center").grid(row=0,column=9)

# Left click on button (event)
def button_lclick_2_1(event):
    global my_points
    global my_button_2_1
    global mutation_2_1_pts
    global mutation_2_1_lvl   
    if (mutation_2_1_lvl == 0):
        mutation_2_1_pts += 10
        my_points += 10
        mutation_2_1_lvl += 1
    elif (mutation_2_1_lvl == 1):
        mutation_2_1_pts += 15
        my_points += 15
        mutation_2_1_lvl += 1       
    initiate_button_2_1()
    update_my_points()
    
def button_lclick_2_3(event):
    global mutation_2_3_pts
    global mutation_2_3_lvl
    global my_button_2_3
    global my_points   
    if (mutation_2_3_lvl == 0):
        mutation_2_3_pts += 5
        my_points += 5
        mutation_2_3_lvl += 1
    elif (mutation_2_3_lvl == 1):
        mutation_2_3_pts += 15
        my_points += 15
        mutation_2_3_lvl += 1
    initiate_button_2_3()
    update_my_points()
    
def button_lclick_2_5(event):
    global mutation_2_5_lvl
    global mutation_2_5_pts
    global my_button_2_5
    global my_points
    if (mutation_2_5_lvl == 0):
        mutation_2_5_pts += 5
        my_points += 5
        mutation_2_5_lvl += 1
    elif (mutation_2_5_lvl == 1):
        mutation_2_5_pts += 15
        my_points += 15
        mutation_2_5_lvl += 1
    initiate_button_2_5()
    update_my_points()
    
def button_lclick_2_7(event):
    global mutation_2_7_pts
    global mutation_2_7_lvl
    global my_button_2_7
    global my_points
    if (mutation_2_7_lvl == 0):
        mutation_2_7_pts += 5
        my_points += 5
        mutation_2_7_lvl += 1
    elif (mutation_2_7_lvl == 1):
        mutation_2_7_pts += 15
        my_points += 15
        mutation_2_7_lvl += 1
    initiate_button_2_7()
    update_my_points()
    
def button_lclick_4_1(event):      
    global mutation_4_1_lvl
    global mutation_4_1_pts
    global my_button_4_1
    global my_points
    if (mutation_4_1_lvl == 0):
        mutation_4_1_pts += 5
        my_points += 5
        mutation_4_1_lvl += 1
    elif (mutation_4_1_lvl == 1):
        mutation_4_1_pts += 15
        my_points += 15
        mutation_4_1_lvl += 1
    initiate_button_4_1()
    update_my_points()
    
def button_lclick_4_3(event):
    global mutation_4_3_pts
    global mutation_4_3_lvl
    global my_button_4_3
    global my_points
    if (mutation_4_3_lvl == 0):
        mutation_4_3_pts += 5
        my_points += 5
        mutation_4_3_lvl += 1
    elif (mutation_4_3_lvl == 1):
        mutation_4_3_pts += 15
        my_points += 15
        mutation_4_3_lvl += 1
    initiate_button_4_3()
    update_my_points()

def button_lclick_4_5(event):
    global mutation_4_5_pts
    global mutation_4_5_lvl
    global my_button_4_5
    global my_points
    if (mutation_4_5_lvl == 0):
        mutation_4_5_pts += 5
        my_points += 5
        mutation_4_5_lvl += 1
    elif (mutation_4_5_lvl == 1):
        mutation_4_5_pts += 15
        my_points += 15
        mutation_4_5_lvl += 1
    initiate_button_4_5()
    update_my_points()

def button_lclick_4_7(event):
    global mutation_4_7_pts
    global mutation_4_7_lvl
    global my_button_4_7
    global my_points
    if (mutation_4_7_lvl == 0):
        mutation_4_7_pts += 5
        my_points += 5
        mutation_4_7_lvl += 1
    elif (mutation_4_7_lvl == 1):
        mutation_4_7_pts += 15
        my_points += 15
        mutation_4_7_lvl += 1
    initiate_button_4_7()
    update_my_points()
    
def button_lclick_4_9(event):
    global mutation_4_9_pts
    global mutation_4_9_lvl
    global my_button_4_9
    global my_points
    if (mutation_4_9_lvl == 0):
        mutation_4_9_pts += 5
        my_points += 5
        mutation_4_9_lvl += 1
    elif (mutation_4_9_lvl == 1):
        mutation_4_9_pts += 15
        my_points += 15
        mutation_4_9_lvl += 1
    initiate_button_4_9()
    update_my_points()
    
def button_lclick_6_3(event):
    global mutation_6_3_pts
    global mutation_6_3_lvl
    global my_button_6_3
    global my_points
    if (mutation_6_3_lvl == 0):
        mutation_6_3_pts += 10
        my_points += 10
        mutation_6_3_lvl += 1
    elif (mutation_6_3_lvl == 1):
        mutation_6_3_pts += 15
        my_points += 15
        mutation_6_3_lvl += 1
    initiate_button_6_3()
    update_my_points()
    
def button_lclick_6_5(event):
    global mutation_6_5_pts
    global mutation_6_5_lvl
    global my_button_6_5
    global my_points
    if (mutation_6_5_lvl == 0):
        mutation_6_5_pts += 5
        my_points += 5
        mutation_6_5_lvl += 1
    elif (mutation_6_5_lvl == 1):
        mutation_6_5_pts += 15
        my_points += 15
        mutation_6_5_lvl += 1
    initiate_button_6_5()
    update_my_points()
    
def button_lclick_6_7(event):
    global mutation_6_7_pts
    global mutation_6_7_lvl
    global my_button_6_7
    global my_points
    if (mutation_6_7_lvl == 0):
        mutation_6_7_pts += 5
        my_points += 5
        mutation_6_7_lvl += 1
    elif (mutation_6_7_lvl == 1):
        mutation_6_7_pts += 15
        my_points += 15
        mutation_6_7_lvl += 1
    initiate_button_6_7()
    update_my_points()
    
def button_lclick_8_1(event):
    global mutation_8_1_pts
    global mutation_8_1_lvl
    global my_button_8_1
    global my_points
    if (mutation_8_1_lvl == 0):
        mutation_8_1_pts += 5
        my_points += 5
        mutation_8_1_lvl += 1
    elif (mutation_8_1_lvl == 1):
        mutation_8_1_pts += 15
        my_points += 15
        mutation_8_1_lvl += 1
    initiate_button_8_1()
    update_my_points()
  
def button_lclick_8_3(event):
    global mutation_8_3_pts
    global mutation_8_3_lvl
    global my_button_8_3
    global my_points
    if (mutation_8_3_lvl == 0):
        mutation_8_3_pts += 5
        my_points += 5
        mutation_8_3_lvl += 1
    elif (mutation_8_3_lvl == 1):
        mutation_8_3_pts += 15
        my_points += 15
        mutation_8_3_lvl += 1
    initiate_button_8_3()
    update_my_points()
        
def button_lclick_8_5(event):
    global mutation_8_5_pts
    global mutation_8_5_lvl
    global my_button_8_5
    global my_points
    if (mutation_8_5_lvl == 0):
        mutation_8_5_pts += 5
        my_points += 5
        mutation_8_5_lvl += 1
    elif (mutation_8_5_lvl == 1):
        mutation_8_5_pts += 15
        my_points += 15
        mutation_8_5_lvl += 1
    initiate_button_8_5()
    update_my_points()
        
def button_lclick_8_7(event):
    global mutation_8_7_pts
    global mutation_8_7_lvl
    global my_button_8_7
    global my_points
    if (mutation_8_7_lvl == 0):
        mutation_8_7_pts += 5
        my_points += 5
        mutation_8_7_lvl += 1
    elif (mutation_8_7_lvl == 1):
        mutation_8_7_pts += 15
        my_points += 15
        mutation_8_7_lvl += 1
    initiate_button_8_7()
    update_my_points()


# Right click on button (event)
def button_rclick_2_1(event):
    global mutation_2_1_pts
    global mutation_2_1_lvl
    global my_button_2_1
    global my_points
    if (mutation_2_1_lvl == 1):
        mutation_2_1_pts -= 5
        my_points -= 5
        mutation_2_1_lvl -= 1
    elif (mutation_2_1_lvl == 2):
        mutation_2_1_pts -= 15
        my_points -= 15
        mutation_2_1_lvl -= 1
    initiate_button_2_1()
    update_my_points()
    
def button_rclick_2_3(event):
    global mutation_2_3_pts
    global mutation_2_3_lvl
    global my_button_2_3
    global my_points
    if (mutation_2_3_lvl == 1):
        mutation_2_3_pts -= 5
        my_points -= 5
        mutation_2_3_lvl -= 1
    elif (mutation_2_3_lvl == 2):
        mutation_2_3_pts -= 15
        my_points -= 15
        mutation_2_3_lvl -= 1
    initiate_button_2_3()
    update_my_points()
    
def button_rclick_2_5(event):
    global mutation_2_5_pts
    global mutation_2_5_lvl
    global my_button_2_5
    global my_points
    if (mutation_2_5_lvl == 1):
        mutation_2_5_pts -= 5
        my_points -= 5
        mutation_2_5_lvl -= 1
    elif (mutation_2_5_lvl == 2):
        mutation_2_5_pts -= 15
        my_points -= 15
        mutation_2_5_lvl -= 1
    initiate_button_2_5()
    update_my_points()
    
def button_rclick_2_7(event):
    global mutation_2_7_pts
    global mutation_2_7_lvl
    global my_button_2_7
    global my_points
    if (mutation_2_7_lvl == 1):
        mutation_2_7_pts -= 5
        my_points -= 5
        mutation_2_7_lvl -= 1
    elif (mutation_2_7_lvl == 2):
        mutation_2_7_pts -= 15
        my_points -= 15
        mutation_2_7_lvl -= 1
    initiate_button_2_7()
    update_my_points()
    
def button_rclick_4_1(event):
    global mutation_4_1_pts
    global mutation_4_1_lvl
    global my_button_4_1
    global my_points
    if (mutation_4_1_lvl == 1):
        mutation_4_1_pts -= 5
        my_points -= 5
        mutation_4_1_lvl -= 1
    elif (mutation_4_1_lvl == 2):
        mutation_4_1_pts -= 15
        my_points -= 15
        mutation_4_1_lvl -= 1
    initiate_button_4_1()
    update_my_points()

def button_rclick_4_3(event):
    global mutation_4_3_pts
    global mutation_4_3_lvl
    global my_button_4_3
    global my_points
    if (mutation_4_3_lvl == 1):
        mutation_4_3_pts -= 5
        my_points -= 5
        mutation_4_3_lvl -= 1
    elif (mutation_4_3_lvl == 2):
        mutation_4_3_pts -= 15
        my_points -= 15
        mutation_4_3_lvl -= 1
    initiate_button_4_3()
    update_my_points()

def button_rclick_4_5(event):
    global mutation_4_5_pts
    global mutation_4_5_lvl
    global my_button_4_5
    global my_points
    if (mutation_4_5_lvl == 1):
        mutation_4_5_pts -= 5
        my_points -= 5
        mutation_4_5_lvl -= 1
    elif (mutation_4_5_lvl == 2):
        mutation_4_5_pts -= 15
        my_points -= 15
        mutation_4_5_lvl -= 1
    initiate_button_4_5()
    update_my_points()
    
def button_rclick_4_7(event):
    global mutation_4_7_pts
    global mutation_4_7_lvl
    global my_button_4_7
    global my_points
    if (mutation_4_7_lvl == 1):
        mutation_4_7_pts -= 5
        my_points -= 5
        mutation_4_7_lvl -= 1
    elif (mutation_4_7_lvl == 2):
        mutation_4_7_pts -= 15
        my_points -= 15
        mutation_4_7_lvl -= 1
    initiate_button_4_7()
    update_my_points()
    
def button_rclick_4_9(event):
    global mutation_4_9_pts
    global mutation_4_9_lvl
    global my_button_4_9
    global my_points
    if (mutation_4_9_lvl == 1):
        mutation_4_9_pts -= 5
        my_points -= 5
        mutation_4_9_lvl -= 1
    elif (mutation_4_9_lvl == 2):
        mutation_4_9_pts -= 15
        my_points -= 15
        mutation_4_9_lvl -= 1
    initiate_button_4_9()
    update_my_points()
        
def button_rclick_6_3(event):
    global mutation_6_3_pts
    global mutation_6_3_lvl
    global my_button_6_3
    global my_points
    if (mutation_6_3_lvl == 1):
        mutation_6_3_pts -= 5
        my_points -= 5
        mutation_6_3_lvl -= 1
    elif (mutation_6_3_lvl == 2):
        mutation_6_3_pts -= 15
        my_points -= 15
        mutation_6_3_lvl -= 1
    initiate_button_6_3()
    update_my_points()
    
def button_rclick_6_5(event):
    global mutation_6_5_pts
    global mutation_6_5_lvl
    global my_button_6_5
    global my_points
    if (mutation_6_5_lvl == 1):
        mutation_6_5_pts -= 5
        my_points -= 5
        mutation_6_5_lvl -= 1
    elif (mutation_6_5_lvl == 2):
        mutation_6_5_pts -= 15
        my_points -= 15
        mutation_6_5_lvl -= 1
    initiate_button_6_5()
    update_my_points()
    
def button_rclick_6_7(event):
    global mutation_6_7_pts
    global mutation_6_7_lvl
    global my_button_6_7
    global my_points
    if (mutation_6_7_lvl == 1):
        mutation_6_7_pts -= 5
        my_points -= 5
        mutation_6_7_lvl -= 1
    elif (mutation_6_7_lvl == 2):
        mutation_6_7_pts -= 15
        my_points -= 15
        mutation_6_7_lvl -= 1
    initiate_button_6_7()
    update_my_points()
    
def button_rclick_8_1(event):
    global mutation_8_1_pts
    global mutation_8_1_lvl
    global my_button_8_1
    global my_points
    if (mutation_8_1_lvl == 1):
        mutation_8_1_pts -= 5
        my_points -= 5
        mutation_8_1_lvl -= 1
    elif (mutation_8_1_lvl == 2):
        mutation_8_1_pts -= 15
        my_points -= 15
        mutation_8_1_lvl -= 1
    initiate_button_8_1()
    update_my_points()
    
def button_rclick_8_3(event):
    global mutation_8_3_pts
    global mutation_8_3_lvl
    global my_button_8_3
    global my_points
    if (mutation_8_3_lvl == 1):
        mutation_8_3_pts -= 5
        my_points -= 5
        mutation_8_3_lvl -= 1
    elif (mutation_8_3_lvl == 2):
        mutation_8_3_pts -= 15
        my_points -= 15
        mutation_8_3_lvl -= 1
    initiate_button_8_3()
    update_my_points()
    
def button_rclick_8_5(event):
    global mutation_8_5_pts
    global mutation_8_5_lvl
    global my_button_8_5
    global my_points
    if (mutation_8_5_lvl == 1):
        mutation_8_5_pts -= 5
        my_points -= 5
        mutation_8_5_lvl -= 1
    elif (mutation_8_5_lvl == 2):
        mutation_8_5_pts -= 15
        my_points -= 15
        mutation_8_5_lvl -= 1
    initiate_button_8_5()
    update_my_points()
    
def button_rclick_8_7(event):
    global mutation_8_7_pts
    global mutation_8_7_lvl
    global my_button_8_7
    global my_points
    if (mutation_8_7_lvl == 1):
        mutation_8_7_pts -= 5
        my_points -= 5
        mutation_8_7_lvl -= 1
    elif (mutation_8_7_lvl == 2):
        mutation_8_7_pts -= 15
        my_points -= 15
        mutation_8_7_lvl -= 1
    initiate_button_8_7()
    update_my_points()
       
# Images
def initiate_image():
    global mutations_title
    mutations_title = ImageTk.PhotoImage(Image.open("mutations_title.png"))
    Label(window, image=mutations_title, justify="center").grid(row=0,column=0,columnspan=12)
initiate_image()

# Spended points
def initiate_label():
    my_label_points = Label(window, text="Points \n spent : " + str(my_points), justify="center").grid(row=0,column=9)
initiate_label()

# LABELS BTW BUTTONS (design)
# Vertical axes
def initiation_ver_label():
    for i in range (2, 11, 2):
        cmd = "my_label_1_" + str(i) + " = Label(window, padx=distance_btw_labels_Y).grid(row=1,column=" + str(i) + ")"
        exec(cmd)
initiation_ver_label()

# Horizontal axes  
def initiation_hor_label():
    for i in range (1, 11, 2):
        cmd = "my_label_" + str(i) + " = Label(window, padx=distance_btw_labels_X).grid(row=" + str(i) + ")"
        exec(cmd)        
initiation_hor_label()

# Buttons initiate
def initiate_buttons():
    initiate_button_2_1()
    initiate_button_2_3()
    initiate_button_2_5()
    initiate_button_2_7()
    initiate_button_4_1()
    initiate_button_4_3()
    initiate_button_4_5()
    initiate_button_4_7()
    initiate_button_4_9()
    initiate_button_6_3()
    initiate_button_6_5()
    initiate_button_6_7()
    initiate_button_8_1()
    initiate_button_8_3()
    initiate_button_8_5()
    initiate_button_8_7()
    
def initiate_button_2_1():
    my_button_2_1 = Button(window, text=" LVL "+ str(mutation_2_1_lvl), image=mutation_2_1, compound="bottom")
    my_button_2_1.grid(row=2,column=1)
    my_button_2_1.bind("<Enter>", on_enter_2_1)
    my_button_2_1.bind("<Leave>", on_leave)
    my_button_2_1.bind("<Button-1>", button_lclick_2_1)
    my_button_2_1.bind("<Button-3>", button_rclick_2_1)

def initiate_button_2_3():
    my_button_2_3 = Button(window, text=" LVL "+ str(mutation_2_3_lvl), image=mutation_2_3, compound="bottom")
    my_button_2_3.grid(row=2,column=3)
    my_button_2_3.bind("<Enter>", on_enter_2_3)
    my_button_2_3.bind("<Leave>", on_leave)
    my_button_2_3.bind("<Button-1>", button_lclick_2_3)
    my_button_2_3.bind("<Button-3>", button_rclick_2_3)

def initiate_button_2_5():
    my_button_2_5 = Button(window, text=" LVL "+ str(mutation_2_5_lvl), image=mutation_2_5, compound="bottom")
    my_button_2_5.grid(row=2,column=5)
    my_button_2_5.bind("<Enter>", on_enter_2_5)
    my_button_2_5.bind("<Leave>", on_leave)
    my_button_2_5.bind("<Button-1>", button_lclick_2_5)
    my_button_2_5.bind("<Button-3>", button_rclick_2_5)
    
def initiate_button_2_7():
    my_button_2_7 = Button(window, text=" LVL "+ str(mutation_2_7_lvl), image=mutation_2_7, compound="bottom")
    my_button_2_7.grid(row=2,column=7)
    my_button_2_7.bind("<Enter>", on_enter_2_7)
    my_button_2_7.bind("<Leave>", on_leave)
    my_button_2_7.bind("<Button-1>", button_lclick_2_7)
    my_button_2_7.bind("<Button-3>", button_rclick_2_7)

def initiate_button_4_1():
    my_button_4_1 = Button(window, text=" LVL "+ str(mutation_4_1_lvl), image=mutation_4_1, compound="bottom")
    my_button_4_1.grid(row=4,column=1)
    my_button_4_1.bind("<Enter>", on_enter_4_1)
    my_button_4_1.bind("<Leave>", on_leave)
    my_button_4_1.bind("<Button-1>", button_lclick_4_1)
    my_button_4_1.bind("<Button-3>", button_rclick_4_1)

def initiate_button_4_3():
    my_button_4_3 = Button(window, text=" LVL "+ str(mutation_4_3_lvl), image=mutation_4_3, compound="bottom")
    my_button_4_3.grid(row=4,column=3)
    my_button_4_3.bind("<Enter>", on_enter_4_3)
    my_button_4_3.bind("<Leave>", on_leave)
    my_button_4_3.bind("<Button-1>", button_lclick_4_3)
    my_button_4_3.bind("<Button-3>", button_rclick_4_3)

def initiate_button_4_5():
    my_button_4_5 = Button(window, text=" LVL "+ str(mutation_4_5_lvl), image=mutation_4_5, compound="bottom")
    my_button_4_5.grid(row=4,column=5)
    my_button_4_5.bind("<Enter>", on_enter_4_5)
    my_button_4_5.bind("<Leave>", on_leave)
    my_button_4_5.bind("<Button-1>", button_lclick_4_5)
    my_button_4_5.bind("<Button-3>", button_rclick_4_5)

def initiate_button_4_7():
    my_button_4_7 = Button(window, text=" LVL "+ str(mutation_4_7_lvl), image=mutation_4_7, compound="bottom")
    my_button_4_7.grid(row=4,column=7)
    my_button_4_7.bind("<Enter>", on_enter_4_7)
    my_button_4_7.bind("<Leave>", on_leave)
    my_button_4_7.bind("<Button-1>", button_lclick_4_7)
    my_button_4_7.bind("<Button-3>", button_rclick_4_7)

def initiate_button_4_9():
    my_button_4_9 = Button(window, text=" LVL "+ str(mutation_4_9_lvl), image=mutation_4_9, compound="bottom")
    my_button_4_9.grid(row=4,column=9)
    my_button_4_9.bind("<Enter>", on_enter_4_9)
    my_button_4_9.bind("<Leave>", on_leave)
    my_button_4_9.bind("<Button-1>", button_lclick_4_9)
    my_button_4_9.bind("<Button-3>", button_rclick_4_9)

def initiate_button_6_3():
    my_button_6_3 = Button(window, text=" LVL "+ str(mutation_6_3_lvl), image=mutation_6_3, compound="bottom")
    my_button_6_3.grid(row=6,column=3)
    my_button_6_3.bind("<Enter>", on_enter_6_3)
    my_button_6_3.bind("<Leave>", on_leave)
    my_button_6_3.bind("<Button-1>", button_lclick_6_3)
    my_button_6_3.bind("<Button-3>", button_rclick_6_3)    

def initiate_button_6_5():
    my_button_6_5 = Button(window, text=" LVL "+ str(mutation_6_5_lvl), image=mutation_6_5, compound="bottom")
    my_button_6_5.grid(row=6,column=5)
    my_button_6_5.bind("<Enter>", on_enter_6_5)
    my_button_6_5.bind("<Leave>", on_leave)
    my_button_6_5.bind("<Button-1>", button_lclick_6_5)
    my_button_6_5.bind("<Button-3>", button_rclick_6_5)

def initiate_button_6_7():
    my_button_6_7 = Button(window, text=" LVL "+ str(mutation_6_7_lvl), image=mutation_6_7, compound="bottom")
    my_button_6_7.grid(row=6,column=7)
    my_button_6_7.bind("<Enter>", on_enter_6_7)
    my_button_6_7.bind("<Leave>", on_leave)
    my_button_6_7.bind("<Button-1>", button_lclick_6_7)
    my_button_6_7.bind("<Button-3>", button_rclick_6_7)

def initiate_button_8_1():
    my_button_8_1 = Button(window, text=" LVL "+ str(mutation_8_1_lvl), image=mutation_8_1, compound="bottom")
    my_button_8_1.grid(row=8,column=1)
    my_button_8_1.bind("<Enter>", on_enter_8_1)
    my_button_8_1.bind("<Leave>", on_leave)
    my_button_8_1.bind("<Button-1>", button_lclick_8_1)
    my_button_8_1.bind("<Button-3>", button_rclick_8_1)

def initiate_button_8_3():
    my_button_8_3 = Button(window, text=" LVL "+ str(mutation_8_3_lvl), image=mutation_8_3, compound="bottom")
    my_button_8_3.grid(row=8,column=3)
    my_button_8_3.bind("<Enter>", on_enter_8_3)
    my_button_8_3.bind("<Leave>", on_leave)
    my_button_8_3.bind("<Button-1>", button_lclick_8_3)
    my_button_8_3.bind("<Button-3>", button_rclick_8_3)

def initiate_button_8_5():
    my_button_8_5 = Button(window, text=" LVL "+ str(mutation_8_5_lvl), image=mutation_8_5, compound="bottom")
    my_button_8_5.grid(row=8,column=5)
    my_button_8_5.bind("<Enter>", on_enter_8_5)
    my_button_8_5.bind("<Leave>", on_leave)
    my_button_8_5.bind("<Button-1>", button_lclick_8_5)
    my_button_8_5.bind("<Button-3>", button_rclick_8_5)

def initiate_button_8_7():
    my_button_8_7 = Button(window, text=" LVL "+ str(mutation_8_7_lvl), image=mutation_8_7, compound="bottom")
    my_button_8_7.grid(row=8,column=7)
    my_button_8_7.bind("<Enter>", on_enter_8_7)
    my_button_8_7.bind("<Leave>", on_leave)
    my_button_8_7.bind("<Button-1>", button_lclick_8_7)
    my_button_8_7.bind("<Button-3>", button_rclick_8_7)
    
initiate_buttons()

window.mainloop()