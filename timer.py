from tkinter import *
import time
screen = Tk()
screen.title("Timer")
screen.geometry("700x600")
screen.resizable(True, True)
screen.attributes("-toolwindow", True)
screen.configure(bg="lightblue", border = "10", borderwidth = 5, relief = "ridge")
running = False
hrs = IntVar(value = 0)
mins = IntVar(value = 0)
secs = IntVar(value = 0)
def start():
    global running
    if running:
        return
    running = True
    tick()
    updatebutton()

def tick():
    if not running:
        return
    second = secs.get()
    minute = mins.get()
    hour = hrs.get()
    totalsecs = (hour * 3600) + (minute * 60) + second
    print(totalsecs)
    h,m,s = 0,0,0
    while totalsecs > 0:
        print(h,m,s)
        m,s = divmod(totalsecs, 60)
        if m > 60:
            h,m = divmod(m, 60)

        hrs.set(h)
        secs.set(s)
        mins.set(m)
        #screen.after(1000, tick)
        screen.update()
        time.sleep(1)
        totalsecs -= 1

def updatedisplay():
    pass
def pause():
    global running, id
    running = False
    if id:
        screen.after_cancel(id)
        id = None
    updatebutton()

def stop():
    global id, running
    running = False
    if id:
        screen.after_cancel(id)
        id = None
    hrs.set(0)
    mins.set(0)
    secs.set(0)
    updatebutton()

def updatebutton():
    if running:
        begin.config(state = DISABLED)
        b.config(state = NORMAL)
    else:
        begin.config(state = NORMAL)
        b.config(state = DISABLED)
Label(screen, text = "Timer").grid(row = 0, column = 1)
h = Entry(screen, textvariable= hrs, width = 30)
h.grid(pady = 20, row = 1, column = 0)

m = Entry(screen, textvariable = mins, width = 30)
m.grid(pady = 20, row = 1, column = 1)

s = Entry(screen, textvariable=secs, width = 30)
s.grid(pady = 20, row = 1, column = 2)

begin = Button(screen, text = "Start", command = start)
begin.grid(row = 2, column = 0)

b = Button(screen, text = "Pause", command = pause)
b.grid(row = 2, column = 1)

stop = Button(screen, text = "Stop", command = stop)
stop.grid(row = 2, column = 2)

screen.mainloop()