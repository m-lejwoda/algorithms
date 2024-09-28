from tkinter import *
okno = Tk()
okno.title(" Kwadraty parzyste ")
okno.geometry("550x400+500+60")

howManyNumber=5
lengthNumber=180

howMany= Label(okno, text="Ile razy = ")
howMany.grid(column=0, row=1, padx=5, pady=5)
editHowMany = Entry(okno,width=6)
editHowMany.insert(END, str(howManyNumber))
editHowMany.grid(column=1, row=1)

length = Label(okno, text="Dlugosc boku = ")
length.grid(column=0, row=2)
editLength = Entry(okno,width=6)
editLength.insert(END, str(lengthNumber))
editLength.grid(column=1, row=2, padx=5, pady=5)
plotno = Canvas(bg="white", width=300, height=300)

def clickedCzysc():
    editHowMany.delete(0, END)
    editLength.delete(0, END)
    plotno.delete("all")

przyciskCzysc = Button(okno, text=" Czyść ", command=clickedCzysc)
przyciskCzysc.grid(column=1, row=0, padx=5, pady=5)

def kwadraty_parzyste(howMany, length, x, y):
    if howMany == 0:
        return 0

    half_length = length / 2
    second_half = half_length / 2
    plotno.create_line(x, y, x + length, y)
    plotno.create_line(x+length, y, x+length, y+length)
    plotno.create_line(x+length, y+length, x, y+length)
    plotno.create_line(x, y+length, x,y)
    plotno.create_line(x+half_length, y, x + length, y + half_length)
    plotno.create_line(x + length, y + half_length, x + half_length, y + length)
    plotno.create_line(x + half_length, y + length, x, y + half_length)
    plotno.create_line(x, y + half_length, x+half_length, y)
    kwadraty_parzyste(howMany - 1, half_length, x+second_half, y+second_half)
    plotno.grid(column=2, row=2, padx=1, pady=1)



def clickedRysuj():
    plotno.delete("all")
    howMany = int(editHowMany.get())
    length = int(editLength.get())
    kwadraty_parzyste(howMany, length, 5,5)


przyciskRysuj = Button(okno, text="Rysuj kwadraty parzyste ", command=clickedRysuj)
przyciskRysuj.grid(column=0, row=0)
okno.mainloop()