import tkinter as tk
#budem ho oslovovat ako tk
win = tk.Tk()





atext = tk.Label(win,text="koeficient a:")
atext.pack()
a = tk.Entry(win)
a.pack()

btext = tk.Label(win,text="koeficient b:")
btext.pack()
b = tk.Entry(win)
b.pack()

ctext = tk.Label(win,text="koeficient c:")
ctext.pack()
c = tk.Entry(win)
c.pack()

def executor():
    print(a.get(),b.get(),c.get()) #print vypise hodnoty do command line, je to string
    ka = int(a.get()) #koeficient, menime zo stringu na integer
    kb = int(b.get())
    kc = int(c.get())
    d = kb**2 - 4*ka*kc
    if d<0:
        print("Nema riesenie v R")
    elif d == 0:
        print("x:",-kb/(2*ka))
    else:
        print("x1:",-kb + d ** 0.5 / (2*ka))
        print("x2:",-kb + d ** 0.5 / (2*ka))
# a**2 + bx + c = 0



button = tk.Button(win, text = "hotovko!",command=executor)
#prvy parameter je ktoremu oknu to bude platit, 2parameter je text, 3 parameter je co ide robit
button.pack()

win.mainloop()


#du: aby sa vysledky zjavii vo win
