from tkinter import *

screen = Tk()
screen.title("Stopwatch")
screen.geometry("700x600")
screen.resizable(True, True)
screen.attributes("-toolwindow", True)
screen.configure(bg="lightblue", border = "10", borderwidth = 5, relief = "ridge")
running = False
hrs = StringVar(value = "00")
mins = StringVar(value = "00")
secs = StringVar(value = "00")
id = None
def start():
    global running
    if running:
        return
    running = True
    tick()
    updatebutton()

def tick():
    global id
    if not running:
        return
    second = int(secs.get())
    minute = int(mins.get())
    hour = int(hrs.get())
    second += 1
    if second == 60:
        second = 0
        minute += 1
    
    if minute == 60:
        minute = 0
        hour += 1
    hrs.set(f"{hour:02d}")
    mins.set(f"{minute:02d}")
    secs.set(f"{second:02d}")
    updatedisplay()
    id = screen.after(1000, tick)
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
Label(screen, text = "Stopwatch").grid(row = 0, column = 1)
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