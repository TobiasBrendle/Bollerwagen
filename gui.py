import tkinter
from tkinter import *


class Gui():
    def __init__(self, werte):
        self.werte = werte
        self.start()

    def start(self):
        self.window = Tk()
        self.window.title("Bollerwagen Anzeige")
        self.window.geometry('1280x720')
        self.canvas = tkinter.Canvas(self.window, width=1280, height=720)
        self.canvas.pack()

        self.speed_label = Label(self.window, text="Geschwindigkeit")
        self.speed_label.place(x=280, y=60)
        self.canvas.create_rectangle(80, 100, 580, 150, fill="white", outline="black")

        self.steer_label = Label(self.window, text="Lenkung")
        self.steer_label.place(x=300, y=210)
        self.canvas.create_rectangle(80, 250, 580, 300, fill="white", outline="black")

        self.canvas.create_rectangle(80, 400, 580, 500, fill="grey", outline="black")

        for i in range(5):
            x = 100 + i * 115
            self.kreis(x, 420, 10, self.werte.get_uso_color(i), self.canvas)
            self.u_label = Label(self.window, text="u" + str(i + 1))
            self.u_label.place(x=x - 10, y=450)

        self.btn1 = Button(self.window, text="Beenden", command=self.testing)
        self.btn1.place(x=80, y=550)

        self.btn2 = Button(self.window, text="Neustart", command=self.testing)
        self.btn2.place(x=290, y=550)

        self.btn3 = Button(self.window, text="Kamerabild ein", command=self.testing)
        self.btn3.place(x=470, y=550)

        self.update()
        self.window.mainloop()

    def testing(self):
        print('auf -- umgestellt')

    def kreis(self, x, y, r, f, c):
        c.create_oval(x - r, y - r, x + r, y + r, fill=f)

    def update(self):
        steer, speed, value, msg = self.werte.get_values()      #Funktion gibt Wichtige Werte zum Anzeigen zurück
        #steer zwischen -50 und 50, speed zwischen 0 und 100, value gibt an ob TOF ausgerichtet ist, msg gibt Fehlertext an
        print("Lenkung = " + str(steer) + ", Geschwindigkeit = " + str(speed))

        for i in range(5):
            x = 100 + i * 115
            self.kreis(x, 420, 10, self.werte.get_uso_color(i), self.canvas)


        self.error_label = Label(self.window, text=msg)
        self.error_label.place(x=800, y=200)

        if value:
            self.kreis(800, 420, 100, "green", self.canvas)

        else:
            self.kreis(800, 420, 100, "red", self.canvas)

        self.canvas.after(50, self.update)
