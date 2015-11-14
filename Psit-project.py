"""the data processing project PSIT 2015"""
from tkinter import *
from matplotlib import pyplot
from numpy import arange

window = Tk()
window.geometry("400x400+900+0")
main_data = {"Resident":50 , "small company":300 , "medium company": 1000, "large company": 2345,"Government":200}
def main():
    """main of this call of all element of program"""
    menu()#call the menu of program
    main_window()

def main_window():
    label = Label(window, text = "Volt of voluminous", bg = "white")
    label.pack()

def menu():
    """create menutab on window"""
    menubar = Menu(window)
    menu_about = Menu(menubar)#Create menu tab
    menu_about.add_command(label = "Credit")#add menu to menu tab
    menubar.add_cascade(label = "Creator", menu = menu_about)#add sub menu to menu
    window.config(menu = menubar)

def bar_graph(data, value):
    """create the bar graph form data"""
    pos = arange(len(data))
    pyplot.xticks(pos+0.4,data)
    pyplot.bar(pos,value)
    pyplot.show()

main()
