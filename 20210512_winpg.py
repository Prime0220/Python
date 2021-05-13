'''
#원도우 텍스트 표시
import tkinter 


win = tkinter.Tk()

win.title("Label test")
win.geometry("640x400+100+100")
win.resizable(False, False)
label = tkinter.Label(win, text = "파이썬", width = 10, height = 5, fg = "red", relief = "solid")
label.pack()

win.mainloop()
'''

'''
# 이미지 넣기
import tkinter

win = tkinter.Tk()
win.title("Label test")
photo = tkinter.PhotoImage(file = "C:\\Users\\user\\Desktop\\test.GIF")
label = tkinter.Label(win, image = photo)
label.pack()
win.mainloop()
'''

'''
#push버튼 생성
import tkinter as tk

win = tk.Tk()
B = tk.Button(win, width = 10, height = 10, text = "push")
B.place(x = 10, y = 10)

win.mainloop()
'''

'''
#버튼 클릭시 인사해줌 
from tkinter import *
from tkinter import messagebox

def Callhello() :
    msg = messagebox.showinfo("Hello Sangil", "Welcome, please click 확인")

win = Tk()
B = Button(win, text = "클릭", command = Callhello)
B.place(x = 50, y = 50)
win.mainloop()
'''

'''
# 캔버스 크기 지정 및 색깔 지정
from tkinter import *
win = Tk()
C = Canvas(win, bg = "red", height = 150, width = 200)
C.pack()        #화면에 배치
win.mainloop()
'''

'''
# canvas
import tkinter

win = tkinter.Tk()
win.title("canvas imageloading")
C = tkinter.Canvas(win, width = 600, height = 600, bg = "white")

#문자열
#C.create_text(200, 50, text = "draw figure on canvas", fill = "black", font = ("Coming Soon", 25))

#line make : 선분 그리기 position (x1, y1, x2, y2)
#C.create_line(100, 100, 100, 200, fill ="red", width = 3)

# retangle : 사각형 그리기 position + length
#C.create_rectangle(200, 200, 300, 300, fill = "gray90", width = 3, outline = "black")

#oval 원그리기
C.create_oval(200, 200, 250, 250, fill = 'blue')

C.pack()
win.mainloop()
'''



