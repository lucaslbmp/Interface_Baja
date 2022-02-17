import os #usada para achar o diretorio atual
import re #usada para remover '\' do path
from tkinter import *

"""
Configurando toda a interface
"""

#Configurações iniciais da interface

inter= Tk()
inter.title("BAJA UFABC") #Título
inter.geometry("1300x650") #Tamanho
inter.configure(bg="#000") #Cor de fundo

#Variaveis apenas para plotagem/ necessario configurar com a porta

vel= 100 #Variavel do arduino / velocidade
temp= 80 #Variavel do arduino / temperatura
combus= 100 #Variavel do arduino / combustivel

#Posicionamento dos dados e seus layouts

Label(inter,text= str(vel),bg="#000",fg="#fff",font=("display - 7",70)).place(x=35,y=220)
Label(inter,text="Velocidade - KM/H",bg="#222",fg="#fff", anchor=W, font= ("display - 7",20)).place(x=30,y=330)

Label(inter,text=str(temp)+"°C",bg="#000",fg="#fff",font=("display - 7",70)).place(x=380,y=220)
Label(inter,text="Temperatura",bg="#222",fg="#fff", anchor=W, font=("display - 7",20)).place(x=400,y=330)

Label(inter,text=str(combus)+"% ",bg="#000",fg="#fff",anchor=W, font=("display - 7",20)).place(x=370,y=545)

Label(inter,text="ANÁLISE DE DADOS EM TEMPO REAL - CR 4.9", bg= "#000", fg="#090", font=("Times New Roman", 37)).place(x=240,y=45)

#Gráfico

#executa o plote dos gráficos
def grafico(): #posteriormente, colocar as funções lá em cima


    valor=parametro.get()
    if valor == "v":

        print("velocidade") #Colocar aqui o plot do grafico
        Label(graf, text="Gráfico velocidade", fg="#000").place(x=10,y=10)

    elif valor == "t":

        print("temperatura") #Colocar aqui o plot do grafico
        Label(graf, text="Gráfico temperatura", fg="#000").place(x=10,y=10)

    elif valor == "c":

        print("combustivel")#Colocar aqui o plot do grafico
        Label(graf, text="Gráfico combustivel", fg="#000").place(x=10,y=10)

    else:
        print("nenhum")


parametro= StringVar()

radvel= Radiobutton(inter,  bg="#000", fg="#fff", font=("display - 7",10), text ="Velocidade", value= "v", variable= parametro)
radvel.place(x=560,y=460)

radtemp= Radiobutton(inter, bg="#000", fg="#fff", font=("display - 7",10), text ="Temperatura", value= "t", variable= parametro)
radtemp.place(x=560,y=510)

radcombus= Radiobutton(inter, bg="#000", fg="#fff", font=("display - 7",10), text ="Combustivel", value= "c", variable= parametro)
radcombus.place(x=560,y=560)



gerar=Button(inter, text="GERAR GRÁFICO", bg="#000",fg="#fff",font=("display - 7", 12), command= grafico)
gerar.place(x=560,y=600)

#Posição do Gráfico

graf=Frame(inter, borderwidth= 1, relief= "solid")
graf.place(x= 750 ,y= 130, width= 530, height= 500)

#Inserindo as imagens

#print(os.getcwd().replace("\\","//")+"//logo.gif")
logobaja=PhotoImage(file= os.getcwd().replace("\\","//")+"//Imagens//logo.gif")
Label(inter, image=logobaja).place(x=50,y=10)

logotanque=PhotoImage(file= os.getcwd().replace("\\","//")+"//Imagens//logo tanque.gif")
Label(inter, image=logotanque).place(x=50,y=500)

#Diferentes imagens de acordo com o nivel de combustivel/ fiz só pra 100%

if combus >75:

    comb=PhotoImage(file= os.getcwd().replace("\\","//")+"//Imagens//full.gif")
    Label(inter, image=comb).place(x=155,y=540)

elif combus>50:
    print("") #Print vazio apenas para não deixar em branco

elif combus>25:
    print("") #Print vazio apenas para não deixar em branco

else:
    print("") #Print vazio apenas para não deixar em branco

inter.mainloop()
