# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/

import matplotlib

#matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg as FigureCanvas, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from tkinter import ttk

import time
import serial
from threading import Thread
from multiprocessing import Process
import sys
import itertools
import os

LARGE_FONT = ("Verdana", 12)
style.use("ggplot")

f = Figure(figsize=(5, 5), dpi=100)
a = f.add_subplot(111)

root = tk.Tk()
root.wm_title("Embedding in Tk")

def store_data():
    comport.write(PARAM_CARACTER.encode('utf-8'))
    linha = comport.readline().decode('utf-8')
    linha = ''.join(e for e in linha if e.isalnum() or e==',')
    with open("dados.txt", "a") as dados:
        dados.write(linha+'\n')
    #with open('dados.txt', 'rb') as file:
     #   file.seek(-2, os.SEEK_END)
    #print(linha)
    #sys.stdout.flush()
    #comport.close()

def animate(i):
    #store_data()
    background_thread = Thread(target=store_data, args=())
    background_thread.start()
    tempo=[]
    vel=[]
    comb=[]
    variaveis = {'t':tempo,'v':vel,'c':comb}
    #pullData = open("dados.txt", "r").read()
    offset = 20
    n = 30
    with open("dados.txt") as data:
        n_last_lines = list(reversed([x for x in itertools.islice(data, None)][-(offset+1):-(offset+n+1):-1]))
    dataList = reversed(n_last_lines)
    #dataList = pullData.split("\n")
    for eachLine in dataList:
        if len(eachLine) > 1:
            campos = eachLine.split(",")
            for campo in campos:
                var = campo[0]
                if var in variaveis.keys() and len(tempo)>=len(variaveis[var]):
                    variaveis[var].append(int(campo[1:])) # atribuindo o valor à variável correpondente a 'var'
    #print(tempo,'|',vel,'\n')

    a.clear()
    a.plot(tempo, vel)

class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self)
        tk.Tk.wm_title(self, "Sea of BTC client")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = ttk.Button(
            self, text="Visit Page 1", command=lambda: controller.show_frame(PageOne)
        )
        button.pack()

        button2 = ttk.Button(
            self, text="Visit Page 2", command=lambda: controller.show_frame(PageTwo)
        )
        button2.pack()

        button3 = ttk.Button(
            self, text="Graph Page", command=lambda: controller.show_frame(PageThree)
        )
        button3.pack()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(
            self, text="Back to Home", command=lambda: controller.show_frame(StartPage)
        )
        button1.pack()

        button2 = ttk.Button(
            self, text="Page Two", command=lambda: controller.show_frame(PageTwo)
        )
        button2.pack()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(
            self, text="Back to Home", command=lambda: controller.show_frame(StartPage)
        )
        button1.pack()

        button2 = ttk.Button(
            self, text="Page One", command=lambda: controller.show_frame(PageOne)
        )
        button2.pack()


class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(
            self, text="Back to Home", command=lambda: controller.show_frame(StartPage)
        )
        button1.pack()

        canvas = FigureCanvas(f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

comport = serial.Serial('COM5', 38400,timeout=0.3)
PARAM_CARACTER='t'
time.sleep(1.5) # Time entre a conexao serial e o tempo para enviar algo (Entre 1.5s a 2s)
#comport = serial.Serial('COM5', 38400)
#p = Process(target=store_data)
#p.start()  # start execution of myFunc() asychronously
app = SeaofBTCapp()
ani = animation.FuncAnimation(f, animate, interval=200)
app.mainloop()
#background_thread = Thread(target=store_data, args=())
#background_thread.start()
#comport.close()


