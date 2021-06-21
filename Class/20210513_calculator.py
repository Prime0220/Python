from tkinter import  *

def event(btn) :
    if btn == 'C' :
        clear()
    elif btn == '=' :
        rst = eval(entdata.get())
        clear()
        insert(0, rst)
    else :
        insert(END, btn)


def insert(key, val):
    entdata.get()
    entdata.insert(key, val)

def clear() :
    entdata.get()
    entdata.delete(0, END)

win = Tk()
win.title(" 계산기 ")
win.geometry("270x125")
win.resizable(False, False)

buttons = ['7', '8', '9', '+', 'C',
           '4', '5', '6', '-', ' ',
           '1', '2', '3', '*', ' ',
           '0', '00', '.', '=', '/']
 
i = 0
x = 5

for b in buttons : 
    btn = Button(win, text = b, width = x, command = (lambda y = b : event(y)))
    btn.grid(row = i//x+1, column = i%x)
    i += 1

entdata = Entry(win, width = 33, bg = 'ivory')
entdata.grid(row = 0, column = 0, columnspan = x)


win.mainloop()

