from tkinter import *
root = Tk()
root.title('Segmented Line')
cw=300
ch=200
canvas_1 = Canvas(root, width=cw, height=ch, background="white")
canvas_1.grid(row=0,column=1)

x1 = 50
y1 = 10

x2 = 50
y2 = 180

x3 = 180
y3 = 180
lines = [x1,y1,x2,y2,x3,y3]
canvas_1.create_line(lines)

root.mainloop()