from tkinter import *
from tkinter import ttk

cor1 = "#4f524e"  #preto
cor2 = "#feffff" #branco
cor3 = "#38576b" #azul
cor4 = "#acb0ab"  #cinza
cor5 = "#32bf9e" #laranja

janela =Tk()
janela.title('Calculadora')
janela.geometry('235x310')
janela.config(bg=cor1)

todos_valores = ''
valor_texto = StringVar()


def mostrar_valores(evento):
    global todos_valores
    todos_valores = todos_valores + str(evento)
    valor_texto.set(todos_valores)


def calcula():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))
    todos_valores = str(resultado)


def limpar_display():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')


frame_visor = Frame(janela, width=235, height=50, bg=cor1)
frame_visor.grid(row=0, column=0)

frame_botoes = Frame(janela, width=235, height=268)
frame_botoes.grid(row=1, column=0)

visor_label = Label(frame_visor, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Arial 18'), bg=cor1, fg=cor2)
visor_label.place(x=0, y=0)

tecla_c = Button(frame_botoes, command=limpar_display,  width=11, height=2, text="C", bg=cor4, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
tecla_c.place(x=0, y=0)
tecla_porcentagem = Button(frame_botoes, command=lambda: mostrar_valores('%'), width=5, height=2, text="%", bg=cor4, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
tecla_porcentagem.place(x=118, y=0)
tecla_divisao = Button(frame_botoes, command=lambda: mostrar_valores('/'), width=5, height=2, text="/", bg=cor5, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
tecla_divisao.place(x=177, y=0)

tecla_7 = Button(frame_botoes, command=lambda: mostrar_valores('7'), width=5, height=2, text="7", fg=cor2, bg=cor1, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
tecla_7.place(x=0, y=52)
tecla_8 = Button(frame_botoes, command=lambda: mostrar_valores('8'), width=5, height=2, text="8", fg=cor2, bg=cor1, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
tecla_8.place(x=59, y=52)
tecla_9 = Button(frame_botoes, command=lambda: mostrar_valores('9'), width=5, height=2, text="9", fg=cor2, bg=cor1, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
tecla_9.place(x=118, y=52)
tecla_multiplicacao = Button(frame_botoes, command=lambda: mostrar_valores('*'), width=5, height=2, text="*", bg=cor5, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
tecla_multiplicacao.place(x=177, y=52)

tecla_4 = Button(frame_botoes, command=lambda: mostrar_valores('4'), width=5, height=2, text="4", fg=cor2, bg=cor1, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
tecla_4.place(x=0, y=104)
tecla_5 = Button(frame_botoes, command=lambda: mostrar_valores('5'), width=5, height=2, text="5", fg=cor2, bg=cor1, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
tecla_5.place(x=59, y=104)
tecla_6 = Button(frame_botoes, command=lambda: mostrar_valores('6'), width=5, height=2, text="6", fg=cor2, bg=cor1, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
tecla_6.place(x=118, y=104)
tecla_subtracao = Button(frame_botoes, command=lambda: mostrar_valores('-'), width=5, height=2, text="-", bg=cor5, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
tecla_subtracao.place(x=177, y=104)

tecla_1 = Button(frame_botoes, command=lambda: mostrar_valores('1'), width=5, height=2, text="1", fg=cor2, bg=cor1, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
tecla_1.place(x=0, y=156)
tecla_2 = Button(frame_botoes, command=lambda: mostrar_valores('2'), width=5, height=2, text="2", fg=cor2, bg=cor1, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
tecla_2.place(x=59, y=156)
tecla_3 = Button(frame_botoes, command=lambda: mostrar_valores('3'), width=5, height=2, text="3", fg=cor2, bg=cor1, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
tecla_3.place(x=118, y=156)
tecla_adicao = Button(frame_botoes, command=lambda: mostrar_valores('+'), width=5, height=2, text="+", bg=cor5, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
tecla_adicao.place(x=177, y=156)

tecla_0 = Button(frame_botoes, command=lambda: mostrar_valores('0'), width=11, height=2, text="0", fg=cor2, bg=cor1, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
tecla_0.place(x=0, y=208)
tecla_virgula = Button(frame_botoes, command=lambda: mostrar_valores('.'), width=5, height=2, text=",", fg=cor2, bg=cor1, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
tecla_virgula.place(x=118, y=208)
tecla_igual = Button(frame_botoes, command=calcula, width=5, height=2, text="=", bg=cor5, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
tecla_igual.place(x=177, y=208)

janela.mainloop()