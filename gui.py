import tkinter
from tkinter import *
from PIL import ImageTk, Image
import sys
from main import start
import time


class Gui():
    def __init__(self, w):
        self.werte = w
        self.start()

    def start(self):
        self.window = Tk()
        self.window.title("Bollerwagen Anzeige")
        self.window.geometry('1280x720')
        self.canvas = tkinter.Canvas(self.window, width=1280, height=720)
        self.canvas.pack()

        self.speed_label = Label(self.window, text="Geschwindigkeit max. 5km/h")
        self.speed_label.place(x=280, y=60)
        self.canvas.create_rectangle(80, 100, 580, 150, fill="white", outline="black")
        self.geschwindigkeit = self.canvas.create_rectangle(80, 100, 80, 150, fill="green")

        self.steer_label = Label(self.window, text="Lenkung")
        self.steer_label.place(x=300, y=210)
        self.canvas.create_rectangle(80, 250, 580, 300, fill="white", outline="black")
        self.auslenkung = self.canvas.create_rectangle(305, 250, 355, 300, fill="green")

        self.canvas.create_rectangle(80, 400, 580, 500, fill="grey", outline="black")

        self.canvas.create_rectangle(640, 150, 1040, 220, fill="grey", outline="black")

        self.gr = self.canvas.create_rectangle(640, 240, 1280, 720, fill="grey", outline="black")

        for i in range(5):
            x = 100 + i * 115
            self.kreis(x, 420, 10, "red", self.canvas)
            self.u_label = Label(self.window, text="u" + str(i + 1))
            self.u_label.place(x=x - 10, y=450)

        ivar = IntVar()
        ivar2 = IntVar()
        ivar.set(200)
        ivar2.set(1)
        self.editfield1 = Entry(self.window, text=ivar)
        self.editfield1.place(x=640, y=80)

        self.editfield2 = Entry(self.window, text=ivar2)
        self.editfield2.place(x=800, y=80)

        self.btn0 = Button(self.window, text="Abstand festlegen", command=self.set_distance)
        self.btn0.place(x=970, y=75)

        self.btn1 = Button(self.window, text="Beenden", command=self.shutdown)
        self.btn1.place(x=80, y=550)

        self.btn4 = Button(self.window, text="Neustart", command=self.restart)
        self.btn4.place(x=200, y=550)

        self.error_dot = self.kreis(700, 183, 20, "green", self.canvas)

        self.var = BooleanVar()
        self.var2 = BooleanVar()

        self.btn2 = Checkbutton(self.window, text="Marker suchen", variable=self.var, command=self.searchref)
        self.btn2.place(x=1050, y=172)

        self.btn3 = Checkbutton(self.window, text="Kamerabild anzeigen", variable=self.var2, command=self.button)
        self.btn3.place(x=445, y=550)

        self.error_label = Label(self.window, text="Bollerwagen wurde gestartet")
        self.error_label.place(x=800, y=172)

        self.kbild = Label(self.window, text="kein Kamerabild angezeigt")
        self.kbild.place(x=640, y=240)

        self.update()
        self.window.mainloop()

    def button(self):
        if self.var2.get():
            self.werte.showMarker = True

        else:
            self.werte.showMarker = False


    def shutdown(self):
        self.werte.stop = True
        self.window.destroy()
        raise sys.exit()

    def restart(self):
        self.werte.stop = True
        time.sleep(1)
        self.werte.stop = False
        start(self.werte)

    def showhide(self):
        if self.werte.showMarker:
            if self.werte.image is not None:
                self.kbild.imgtk = Label(self.window, text="")
                self.canvas.itemconfigure(self.gr, state='hidden')
                imgtk = ImageTk.PhotoImage(image=Image.fromarray(self.werte.image))
                self.kbild.imgtk = imgtk
                self.kbild.configure(image=imgtk)
                self.kbild.place(x=640, y=240)


        else:
            self.canvas.itemconfigure(self.gr, state='normal')
            self.kbild.imgtk = Label(self.window)
            self.kbild = Label(self.window, text="kein Kamerabild angezeigt")
            self.kbild.place(x=900, y=470)

    def set_distance(self):
        abst = float(self.editfield1.get())
        beschl = float(self.editfield2.get())
        self.werte.distance_setting = [abst, beschl]

    def searchref(self):
        if self.var.get():
            self.werte.search_for_marker = True

        else:
            self.werte.search_for_marker = False


    def kreis(self, x, y, r, f, c):
        c.create_oval(x - r, y - r, x + r, y + r, fill=f)

    def update(self):
        steer, speed, value, msg = self.werte.get_values()      #Funktion gibt Wichtige Werte zum Anzeigen zurück
                                                        #steer zwischen -50 und 50, speed zwischen 0 und 100, value gibt an ob TOF ausgerichtet ist, msg gibt Fehlertext an


        self.canvas.delete(self.geschwindigkeit)
        self.canvas.delete(self.auslenkung)

        self.showhide()

        for i in range(5):
            x = 100 + i * 115
            self.kreis(x, 420, 10, self.werte.get_uso_color(i), self.canvas)

        self.geschwindigkeit = self.canvas.create_rectangle(80, 100, 80 + 5 * speed, 150, fill="green")
        self.auslenkung = self.canvas.create_rectangle(305 + steer, 250, 355 + steer, 300, fill="green")

        self.error_label["text"] = msg

        if value:
            self.error_dot = self.kreis(700, 183, 20, "green", self.canvas)

        else:
            self.error_dot = self.kreis(700, 183, 20, "red", self.canvas)


        self.canvas.after(50, self.update)


