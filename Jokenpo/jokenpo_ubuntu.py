# JOKENPÔ


# ---------------------------------------------------------------------------------
# Packages
from tkinter import *
import random
from tkinter import messagebox


# ---------------------------------------------------------------------------------
# Functions
def regras():
    messagebox.showinfo('Regras', 'Papel ganha de Pedra\n\nPedra ganha de Tesoura\n\nTesoura ganha de Papel')


def jogada():
    # Nova janela
    resultado = Tk()
    resultado.title('Jokenpô')
    resultado.resizable(False, False)

    # Dimensões da Janela
    largura = 300
    altura = 60

    # Resolução do nosso sistema
    largura_screen = resultado.winfo_screenwidth()
    altura_screen = resultado.winfo_screenheight()

    # Posição da janela
    posx = largura_screen / 2 - largura / 2
    posy = altura_screen / 2 - altura / 2

    # Definir a geometry
    resultado.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))

    # Lista com a jogada do computador
    lista = ['Pedra', 'Papel', 'Tesoura']
    maquina = random.choice(lista)
    jogador = jog.get()

    # Resultado do jogo
    global empate
    global derrota
    global vitoria

    if jogador == '1':
        if maquina == 'Pedra':
            final = 'Empate!\n\nAmbos escolheram Pedra'
            empate += 1
            empate_lb.config(text=empate)
        elif maquina == 'Papel':
            final = 'Você perdeu!\n\nO computador escolheu Papel'
            derrota += 1
            derrota_lb.config(text=derrota)
        else:
            final = 'Você venceu!\n\nO computador escolheu Tesoura'
            vitoria += 1
            vitoria_lb.config(text=vitoria)
    elif jogador == '2':
        if maquina == 'Papel':
            final = 'Empate!\n\nAmbos escolheram Papel'
            empate += 1
            empate_lb.config(text=empate)
        elif maquina == 'Tesoura':
            final = 'Você perdeu!\n\nO computador escolheu Tesoura'
            derrota += 1
            derrota_lb.config(text=derrota)
        else:
            final = 'Você venceu!\n\nO computador escolheu Pedra'
            vitoria += 1
            vitoria_lb.config(text=vitoria)
    elif jogador == '3':
        if maquina == 'Tesoura':
            final = 'Empate!\n\nAmbos escolheram Tesoura'
            empate += 1
            empate_lb.config(text=empate)
        elif maquina == 'Pedra':
            final = 'Você perdeu!\n\nO computador escolheu Pedra'
            derrota += 1
            derrota_lb.config(text=derrota)
        else:
            final = 'Você venceu!\n\nO computador escolheu Papel'
            vitoria += 1
            vitoria_lb.config(text=vitoria)

    # Resultado
    resultado = Label(resultado, text=final, font='Arial 11 bold')
    resultado.pack(pady=5)


# ---------------------------------------------------------------------------------
# GUI
root = Tk()
root.title('Jokenpô')
root.resizable(False, False)

# Dimensões da Janela
largura = 240
altura = 270

# Resolução do nosso sistema
largura_screen = root.winfo_screenwidth()
altura_screen = root.winfo_screenheight()

# Posição da janela
posx = largura_screen / 2 - largura / 2
posy = altura_screen / 2 - altura / 2

# Definir a geometry
root.geometry('%dx%d+%d+%d' %(largura, altura, posx, posy))


# ---------------------------------------------------------------------------------
# Widgets
# Variáveis
jog = StringVar()
jog.set('1')
vitoria = 0
empate = 0
derrota = 0

pedra = Radiobutton(root, text='Pedra', font='Arial 11', variable=jog, value='1')
papel = Radiobutton(root, text='Papel', font='Arial 11', variable=jog, value='2')
tesoura = Radiobutton(root, text='Tesoura', font='Arial 11', variable=jog, value='3')
btn_resultado = Button(root, text='Jogar', font='Arial 11', command=jogada)
btn_regras = Button(root, text='Regras', font='Arial 11', command=regras)
vitoria_res = Label(root, text='Vitórias: ', font='Arial 11 bold', fg='green')
vitoria_lb = Label(root, text=vitoria, font='Arial 11 bold', fg='green')
empate_res = Label(root, text='Empates: ', font='Arial 11 bold', fg='blue')
empate_lb = Label(root, text=empate, font='Arial 11 bold', fg='blue')
derrota_res = Label(root, text='Derrotas: ', font='Arial 11 bold', fg='red')
derrota_lb = Label(root, text=derrota, font='Arial 11 bold', fg='red')


# ---------------------------------------------------------------------------------
# Layouts
pedra.grid(row=0, column=0, columnspan=2, pady=5, padx=80)
papel.grid(row=1, column=0, columnspan=2, pady=5)
tesoura.grid(row=2, column=0, columnspan=2, pady=5)
btn_regras.grid(row=3, column=1, pady=10)
btn_resultado.grid(row=3, column=0, pady=10)
vitoria_res.grid(row=4, column=0, pady=7)
vitoria_lb.grid(row=4, column=1, pady=7)
empate_res.grid(row=5, column=0, pady=7)
empate_lb.grid(row=5, column=1, pady=7)
derrota_res.grid(row=6, column=0, pady=7)
derrota_lb.grid(row=6, column=1, pady=7)


# ---------------------------------------------------------------------------------
# Window Loop
root.mainloop()

