from tkinter import *
tk=Tk()
canvas=Canvas(tk, width=875, height=490)
canvas.pack()
balon=PhotoImage(file="ball.gif")
cancha=PhotoImage(file="image.gif")
canvas.create_image(0, 0, ancho=NW, image=cancha)
canvas.create_image(421.5, 229, ancho=NW, image=balon)

gol=0
x,y=421.5,229

def moveball(event):
    global x,y
    if event.keysym=="Up":
        canvas.move(2,0,-5)
        y=y-5
    elif event.keysym=="Down":
        canvas.move(2,0,5)
        y=y+5
    elif event.keysym=="Left":
    	canvas.move(2,-5,0)
    	x=x-5
    else:
        canvas.move(2,5,0)
        x=x+5

    if (x>850 and 184<y<276):
        msg=canvas.create_text(421.5,100,text="Goooool!!",font=("times",40),fill="blue")

    elif (x<-7 and 184<y<276):
        msg=canvas.create_text(421.5,100,text="Goooool!!",font=("times",40),fill="red")
        
canvas.bind_all('<KeyPress-Up>', moveball)
canvas.bind_all('<KeyPress-Down>', moveball)
canvas.bind_all('<KeyPress-Left>', moveball)
canvas.bind_all('<KeyPress-Right>', moveball)

tk.mainloop()
