import tkinter as tk
import random
from tkinter import messagebox

root = tk.Tk()
root.title('Uma pergunta importante ❤️')
root.geometry('600x600')
root.configure(background='#ffc8dd')

# ---------- FUNÇÕES ----------

def move_button_1(e):
    x = button_nao.winfo_x()
    y = button_nao.winfo_y()

    # distância do mouse
    if abs(e.x - x) < 80 and abs(e.y - y) < 80:
        new_x = random.randint(0, 500)
        new_y = random.randint(200, 500)
        button_nao.place(x=new_x, y=new_y)

def accepted():
    for i in range(10):
        root.after(i * 100, lambda: show_heart())

    messagebox.showinfo(
        '💖',
        'EU SABIA 😍\nAgora você oficialmente não tem mais escolha kkkkk ❤️'
    )

def denied():
    frases = [
        "Tem certeza? 😢",
        "Olha direito...",
        "Você clicou errado 😳",
        "Tenta de novo...",
        "Não vale esse botão 😭"
    ]
    messagebox.showwarning("Hmm...", random.choice(frases))

def show_heart():
    heart = tk.Label(root, text="❤️", bg='#ffc8dd', font=("Arial", 20))
    heart.place(x=random.randint(0, 550), y=random.randint(0, 550))

# ---------- INTERFACE ----------

titulo = tk.Label(
    root,
    text='Quer namorar comigo?',
    bg='#ffc8dd',
    fg='#590d22',
    font=('Arial', 26, 'bold')
)
titulo.pack(pady=50)

button_sim = tk.Button(
    root,
    text='SIM 😍',
    bg='#ff8fab',
    fg='white',
    command=accepted,
    font=('Arial', 16, 'bold'),
    width=10
)
button_sim.pack(pady=20)

button_nao = tk.Button(
    root,
    text='NÃO 😢',
    bg='#ffb3c1',
    command=denied,
    font=('Arial', 10, 'bold'),
    width=8
)
button_nao.place(x=250, y=350)

# detectar movimento do mouse
root.bind('<Motion>', move_button_1)

root.mainloop()
