import tkinter
from tkinter import *


def gui(werte):
    def testing():
        print('auf -- umgestellt')

    def kreis(x, y, r, f, c):
        c.create_oval(x - r, y - r, x + r, y + r, fill=f)

    def update(werte):
        werte.print_values()
        for i in range(5):
            x = 100 + i * 115
            kreis(x, 420, 10, werte.get_uso_color(i), canvas)
        #canvas.after(500, update)

    window = Tk()
    window.title("Bollerwagen Anzeige")
    window.geometry('1280x720')
    canvas = tkinter.Canvas(window, width=1280, height=720)
    canvas.pack()

    speed_label = Label(window, text="Geschwindigkeit")
    speed_label.place(x=280, y=60)
    canvas.create_rectangle(80, 100, 580, 150, fill="white", outline="black")

    steer_label = Label(window, text="Lenkung")
    steer_label.place(x=300, y=210)
    canvas.create_rectangle(80, 250, 580, 300, fill="white", outline="black")

    canvas.create_rectangle(80, 400, 580, 500, fill="grey", outline="black")

    for i in range(5):
        x = 100 + i * 115
        kreis(x, 420, 10, werte.get_uso_color(i), canvas)
        u_label = Label(window, text="u" + str(i + 1))
        u_label.place(x=x - 10, y=450)

    btn1 = Button(window, text="Beenden", command=update(werte))
    btn1.place(x=80, y=550)

    btn2 = Button(window, text="Neustart", command=testing)
    btn2.place(x=290, y=550)

    btn3 = Button(window, text="Kamerabild ein", command=testing)
    btn3.place(x=470, y=550)

  #  update(werte)
    window.mainloop()
