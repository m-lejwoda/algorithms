from tkinter import *
okno = Tk()
okno.title(" Algorytmy w pythonie ")
okno.geometry("550x400+500+60")

paramAlpha=20
paramLg=180

napisAlpha= Label(okno, text="Alpha=")
napisAlpha.grid(column=0, row=1, padx=5, pady=5)
editAlpha = Entry(okno,width=6)
editAlpha.insert(END, '20')
editAlpha.grid(column=1, row=1)

napis2 = Label(okno, text="lg=")
napis2.grid(column=0, row=2)
editLg = Entry(okno,width=6)
editLg.insert(END, '180')
editLg.grid(column=1, row=2, padx=5, pady=5)
plotno = Canvas(bg="white", width=300, height=300)

def clickedCzysc():
    editAlpha.delete(0, END)
    editLg.delete(0, END)
    plotno.delete("all")

przyciskCzysc = Button(okno, text=" Czyść ", command=clickedCzysc)
przyciskCzysc.grid(column=1, row=0, padx=5, pady=5)

def rysuj_spirala(paramAlpha, paramLg, x,y):
    if (paramLg > 0 and paramLg > paramAlpha):
        plotno.create_line(x, y, x + paramLg, y)
        plotno.create_line(x + paramLg, y, x + paramLg, y + paramLg)
        plotno.create_line(x + paramLg, y + paramLg, x + paramAlpha, y + paramLg)
        plotno.create_line(x + paramAlpha, y + paramLg, x + paramAlpha,
        y + paramAlpha)
        rysuj_spirala(paramAlpha, paramLg - 2 * paramAlpha, x + paramAlpha,
        y + paramAlpha)
    plotno.grid(column=2, row=2, padx=1, pady=1)

def clickedRysuj():
    plotno.delete("all")
    paramAlpha = int(editAlpha.get())
    paramLg = int(editLg.get())
    print(paramLg, paramAlpha)
    rysuj_spirala(paramAlpha, paramLg, 5,5)

przyciskRysuj = Button(okno, text="Rysuj", command=clickedRysuj)
przyciskRysuj.grid(column=0, row=0)
okno.mainloop()