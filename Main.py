import tkinter as tk
import random
from tkinter import messagebox
import winsound

# --------- MÚSICA (arquivo .wav na mesma pasta) ---------
def tocar_musica():
    try:
        winsound.PlaySound("musica.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
    except:
        pass

tocar_musica()

# --------- JANELA ---------
root = tk.Tk()
root.title('Uma pergunta importante ❤️')
root.geometry('600x600')
root.configure(bg='#8b0000')

# --------- FUNDO ---------
canvas = tk.Canvas(root, width=600, height=600, bg='#8b0000', highlightthickness=0)
canvas.place(x=0, y=0)

# corações discretos
for x in range(0, 600, 80):
    for y in range(0, 600, 80):
        canvas.create_text(x, y, text="❤️", font=("Arial", 10))

# área limpa para o título
canvas.create_rectangle(40, 50, 560, 190, fill='#a00000', outline='')

# --------- FUNÇÕES ---------

def mover_botao(e):
    x = botao_nao.winfo_x()
    y = botao_nao.winfo_y()

    if abs(e.x - x) < 80 and abs(e.y - y) < 80:
        botao_nao.place(
            x=random.randint(0, 500),
            y=random.randint(300, 550)
        )

def chuva_coracoes():
    heart = tk.Label(root, text="❤️", bg='#8b0000', font=("Arial", 14))
    heart.place(x=random.randint(0, 580), y=0)

    def cair():
        y = heart.winfo_y()
        if y < 600:
            heart.place(y=y + 5)
            root.after(30, cair)
        else:
            heart.destroy()

    cair()

def final_cinematografico():
    for widget in root.winfo_children():
        widget.destroy()

    tela_final = tk.Label(
        root,
        text="Agora é oficial ❤️\nVocê não tem mais escolha 😌",
        bg='#8b0000',
        fg='white',
        font=('Arial', 28, 'bold')
    )
    tela_final.pack(expand=True)

    for i in range(50):
        root.after(i * 100, chuva_coracoes)

def aceitou():
    messagebox.showinfo("💖", "EU SABIA 😍❤️")
    root.after(1000, final_cinematografico)

def negou():
    frases = [
        "Tem certeza? 😢",
        "Olha direito 👀",
        "Você clicou errado 😳",
        "Não vale 😭",
        "Tenta de novo..."
    ]
    messagebox.showwarning("Hmm...", random.choice(frases))

# --------- TEXTO ---------
titulo = tk.Label(
    root,
    text='Quer namorar comigo?',
    bg='#a00000',
    fg='white',
    font=('Arial', 28, 'bold')
)
titulo.place(x=90, y=90)

# --------- BOTÃO SIM ---------
botao_sim = tk.Button(
    root,
    text='SIM 😍',
    bg='#ff0000',
    fg='white',
    command=aceitou,
    font=('Arial', 16, 'bold'),
    width=10
)
botao_sim.place(x=220, y=250)

# --------- BOTÃO NÃO ---------
botao_nao = tk.Button(
    root,
    text='NÃO 😢',
    bg='#ff4d4d',
    command=negou,
    font=('Arial', 10, 'bold'),
    width=8
)
botao_nao.place(x=250, y=400)

# --------- EVENTO ---------
root.bind('<Motion>', mover_botao)

# --------- LOOP ---------
root.mainloop()
