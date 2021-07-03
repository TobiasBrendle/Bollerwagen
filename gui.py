from tkinter import *
import time
#from wholethreads import dip


def gui(werte):
    while True:
        time.sleep(0.4)
   #     werte.print_values()
        
    window = Tk()
    window.title("Bollerwagen Anzeige")
    window.geometry('512x256')



    sek_lbl = Label(window, text="überschrift oder so")
    sek_lbl.grid(column=0, row=1)

    sek_lbl = Label(window, text="tof:")
    sek_lbl.grid(column=0, row=3)
    sek = Entry(window,width=10)
    sek.grid(column=1, row=3)

    min_lbl = Label(window, text="ultrschall:")
    min_lbl.grid(column=0, row=4)
    m = Entry(window,width=10)
    m.grid(column=1, row=4)

    h_lbl = Label(window, text="camera:")
    h_lbl.grid(column=0, row=5)
    h = Entry(window,width=10)
    h.grid(column=1, row=5)



    def testing():
         print('auf -- umgestellt')


    btn = Button(window, text="Ausgabe", command=testing)
    btn.grid(column=0, row=2)

    window.mainloop()


#gui()


