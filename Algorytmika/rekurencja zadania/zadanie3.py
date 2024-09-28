from tkinter import *
import math
okno = Tk()
okno.title(" Ozdbone ogrodzenie ")
okno.geometry("550x400+500+60")

howManyNumber=2
lengthNumber=180

howMany= Label(okno, text="How many = ")
howMany.grid(column=0, row=1, padx=5, pady=5)
editHowMany = Entry(okno,width=6)
editHowMany.insert(END, str(howManyNumber))
editHowMany.grid(column=1, row=1)

length = Label(okno, text="Side length = ")
length.grid(column=0, row=2)
editLength = Entry(okno,width=6)
editLength.insert(END, str(lengthNumber))
editLength.grid(column=1, row=2, padx=5, pady=5)
plotno = Canvas(bg="white", width=300, height=300)

def clickedClean():
    editHowMany.delete(0, END)
    editLength.delete(0, END)
    plotno.delete("all")

buttonClean = Button(okno, text=" Clean ", command=clickedClean)
buttonClean.grid(column=1, row=0, padx=5, pady=5)


def decorative_fence(number, length, x,y):
    if number == 0:
        return 0
    oval_length = length / 2
    plotno.create_line(x,y, x+ length, y)
    plotno.create_line(x + length,y, x+ length, y + length)
    plotno.create_line(x + length,y + length, x, y + length)
    plotno.create_line(x,y+length, x, y)
    plotno.create_oval(x,y, x+oval_length,y+oval_length)
    plotno.create_oval(x+length,y, x+oval_length,y+oval_length)
    plotno.create_oval(x, y+length, x+oval_length,y+oval_length)
    plotno.create_oval(x+length, y+length, x+oval_length,y+oval_length)
    decorative_fence(number-1, oval_length, x,y)
    decorative_fence(number - 1, oval_length, x +  oval_length, y)
    decorative_fence(number - 1,  oval_length, x, y +  oval_length)
    decorative_fence(number - 1,  oval_length, x + oval_length, y +  oval_length)
    # second_length = length /2
    #
    # decorative_fence(number-1,oval_r,x + f3 ,y+ f3)

    plotno.grid(column=2, row=2, padx=1, pady=1)

def clickedDraw():
    plotno.delete("all")
    howMany = int(editHowMany.get())
    length = int(editLength.get())
    decorative_fence(howMany, length, 5,5)


buttonDraw = Button(okno, text="Draw decorative fence" , command=clickedDraw)
buttonDraw.grid(column=0, row=0)
okno.mainloop()