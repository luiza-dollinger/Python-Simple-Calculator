from tkinter import *

# cor
fundo = '#0f0201'
botoes = '#473838'
botoes2 = '#261e1e'  # pressionado
letras = '#faf8f7'
botao = '#bd574f'  # =
letra = '#240a0a'  # =

calculo = ""


def b_click(simbolo):
    global calculo
    calculo += str(simbolo)
    tela.delete(1.0, "end")
    tela.insert(1.0, calculo)


def b_igual():
    global calculo
    try:
        calculo = str(eval(calculo))
        tela.delete(1.0, "end")
        tela.insert(1.0, calculo)
    except:
        b_deletar()
        tela.insert(1.0, "Error")


def b_deletar():
    global calculo
    calculo = ""
    tela.delete(1.0, "end")


root = Tk()
root.title("Calculadora")
root.geometry("292x280")

root.configure(background=fundo)

tela = Text(root, height=2, width=16, bg=fundo, fg=letras, font=("Arial", 24))
tela.grid(columnspan=5)

bt_1 = Button(root,
              text="1",
              command=lambda: b_click(1),
              width=6,
              fg=letras,
              activeforeground=letras,
              bg=botoes,
              activebackground=botoes2,
              relief=FLAT,
              font=("Arial", 14))
bt_1.grid(row=2, column=1)
bt_2 = Button(root,
              text="2",
              command=lambda: b_click(2),
              width=6,
              fg=letras,
              activeforeground=letras,
              bg=botoes,
              activebackground=botoes2,
              relief=FLAT,
              font=("Arial", 14))
bt_2.grid(row=2, column=2)
bt_3 = Button(root,
              text="3",
              command=lambda: b_click(3),
              width=6,
              fg=letras,
              activeforeground=letras,
              bg=botoes,
              activebackground=botoes2,
              relief=FLAT,
              font=("Arial", 14))
bt_3.grid(row=2, column=3)
bt_plus = Button(root,
                 text="+",
                 command=lambda: b_click("+"),
                 width=5,
                 fg=letras,
                 activeforeground=letras,
                 bg=botoes,
                 activebackground=botoes2,
                 relief=FLAT,
                 font=("Arial", 14))
bt_plus.grid(row=2, column=4)

bt_4 = Button(root,
              text="4",
              command=lambda: b_click(4),
              width=6,
              fg=letras,
              activeforeground=letras,
              bg=botoes,
              activebackground=botoes2,
              relief=FLAT,
              font=("Arial", 14))
bt_4.grid(row=3, column=1)
bt_5 = Button(root,
              text="5",
              command=lambda: b_click(5),
              width=6,
              fg=letras,
              activeforeground=letras,
              bg=botoes,
              activebackground=botoes2,
              relief=FLAT,
              font=("Arial", 14))
bt_5.grid(row=3, column=2)
bt_6 = Button(root,
              text="6",
              command=lambda: b_click(6),
              width=6,
              fg=letras,
              activeforeground=letras,
              bg=botoes,
              activebackground=botoes2,
              relief=FLAT,
              font=("Arial", 14))
bt_6.grid(row=3, column=3)
bt_minus = Button(root,
                  text="-",
                  command=lambda: b_click("-"),
                  width=5,
                  fg=letras,
                  activeforeground=letras,
                  bg=botoes,
                  activebackground=botoes2,
                  relief=FLAT,
                  font=("Arial", 14))
bt_minus.grid(row=3, column=4)

bt_7 = Button(root,
              text="7",
              command=lambda: b_click(7),
              width=6,
              fg=letras,
              activeforeground=letras,
              bg=botoes,
              activebackground=botoes2,
              relief=FLAT,
              font=("Arial", 14))
bt_7.grid(row=4, column=1)
bt_8 = Button(root,
              text="8",
              command=lambda: b_click(8),
              width=6,
              fg=letras,
              activeforeground=letras,
              bg=botoes,
              activebackground=botoes2,
              relief=FLAT,
              font=("Arial", 14))
bt_8.grid(row=4, column=2)
bt_9 = Button(root,
              text="9",
              command=lambda: b_click(9),
              width=6,
              fg=letras,
              activeforeground=letras,
              bg=botoes,
              activebackground=botoes2,
              relief=FLAT,
              font=("Arial", 14))
bt_9.grid(row=4, column=3)
bt_mul = Button(root,
                text="*",
                command=lambda: b_click("*"),
                width=5,
                fg=letras,
                activeforeground=letras,
                bg=botoes,
                activebackground=botoes2,
                relief=FLAT,
                font=("Arial", 14))
bt_mul.grid(row=4, column=4)

bt_open = Button(root,
                 text="(",
                 command=lambda: b_click("("),
                 width=6,
                 fg=letras,
                 activeforeground=letras,
                 bg=botoes,
                 activebackground=botoes2,
                 relief=FLAT,
                 font=("Arial", 14))
bt_open.grid(row=5, column=1)
bt_0 = Button(root,
              text="0",
              command=lambda: b_click(0),
              width=6,
              fg=letras,
              activeforeground=letras,
              bg=botoes,
              activebackground=botoes2,
              relief=FLAT,
              font=("Arial", 14))
bt_0.grid(row=5, column=2)
bt_close = Button(root,
                  text=")",
                  command=lambda: b_click(")"),
                  width=6,
                  fg=letras,
                  activeforeground=letras,
                  bg=botoes,
                  activebackground=botoes2,
                  relief=FLAT,
                  font=("Arial", 14))
bt_close.grid(row=5, column=3)
bt_div = Button(root,
                text="/",
                command=lambda: b_click("/"),
                width=5,
                fg=letras,
                activeforeground=letras,
                bg=botoes,
                activebackground=botoes2,
                relief=FLAT,
                font=("Arial", 14))
bt_div.grid(row=5, column=4)

bt_equals = Button(root,
                   text="=",
                   command=b_igual,
                   width=12,
                   fg=letra,
                   activebackground=botao,
                   bg=botao,
                   relief=RAISED,
                   font=("Arial", 14))
bt_equals.grid(row=6, column=3, columnspan=2)
bt_clear = Button(root,
                  text="C",
                  command=b_deletar,
                  width=12,
                  fg=letra,
                  activebackground=botao,
                  bg=botao,
                  relief=RAISED,
                  font=("Arial", 14))
bt_clear.grid(row=6, column=1, columnspan=2)

root.mainloop()
