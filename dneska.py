import tkinter as tk
win = tk.Tk()

def drticka(e):
    print("Vykonala som sa")
    print(e.x,e.y) #suradnice po kliknuti do canvasu
    zozob = canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1) #na myske sa mi vytvori maly stvorcek 1,1 a ked kliknem na objekt r1 alebo o1 tak mi vypise ci sa spolu prekryvali
    print(zozob) #tiez = r1 je 1 a o1 je 2
    if 1 in zozob:
        print("Klikla som na stvorec") #r1
    elif 2 in zozob:
        print("Klikla som na oval") #o1
    # elif zozob == 1 and zozob == 2:  #nefunguje
    #     print("Klikla som na aj aj")
    else:
        print("Klikla som mimo")

    # klik = canvas.create_oval(e.x+1,e.y+1)
    # print(klik)
    # if 1 in klik:
    #     r2 =  canvas.create_rectangle(150,150,350,350,fill="random")
    # if 1 in zozob:
    #     r2 = canvas.create_rectangle(150,150,350,350,fill="pink")
    if 1 in zozob:
        canvas.move(r1,10,10) #posuva mi r1 doprava o 10
        if canvas.itemcget(r1,"fill") == "black": #itemcget zistuje napr tu fill akej je farby
            canvas.itemconfig(r1, fill="turquoise")  #itemconfig meni danemu tvaru vlastnosti a
        else:
            canvas.itemconfig(r1, fill="black")


def drticka2(e):  #drticka2 mam aby mi mi posuvalo do minusu cize dolava
    zozob = canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if 1 in zozob:
        canvas.move(r1,-10,-10)
        if canvas.itemcget(r1,"fill") == "black":
            canvas.itemconfig(r1, fill="turquoise")
        else:
            canvas.itemconfig(r1, fill="black")

def mover():
    canvas.move(r1,5,0)
    canvas.after(1000,mover) #kazdu 1000 milisek mi posunie stvorec o 5 doprava
def movero():
    canvas.move(o1,-10,0)
    canvas.after(500,movero) #kazdu 500 milisek mi posunie oval o 10 dolava


canvas = tk.Canvas(win,width=500,height=500,bg="red") #canvas bude vo win preto je v () win
r1 = canvas.create_rectangle(150,150,350,350,fill="black")
o1 = canvas.create_oval(250,250,500,500,fill="brown")

mover()
movero()
canvas.bind("<Button-1>",drticka) #ked kliknem hocikde do canvasu, tak sa mi vykona drticka
canvas.bind("<Button-3>",drticka2)


canvas.pack()
win.mainloop()


#canvas.itemcget(r1,"fill") zistuje mi vlastnosti daneho objektu
#canvas.itemconfig(r1, fill="turquoise")  meni vlastnosti objektu
#canvas.move(r1,-10,-10) posuva objekt o dany vektor
#canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1) zistuje ci tam nieco lezi
#canvas.bind("<Button-3>",drticka2) k pozadovanej funkcii pripne funkciu, cize button-1 je pravy klik a button-3 je pravy
