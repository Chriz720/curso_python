""" import tkinter as tk 
janela = tk.Tk()
janela.title("Minha Aplicação")
janela.geometry("300x200")
janela.resizable(False, False)

texto = tk.Label(text="Hello, World!", font=("NewTimesRoman", 30), pady=30)
texto.pack()

janela.mainloop() """

""" import tkinter as tk
janela = tk.Tk()
janela.title("Contador")
janela.geometry("300x200")
janela.resizable(False, False)

clique = 0

def cont():
    global clique
    clique += 1
    subtexto.configure(text=f"Cliques: {clique}")

texto = tk.Label(text="Contador de cliques", font=("Arial", 20), pady=25)
subtexto = tk.Label(text="Cliques: 0", font=("Arial", 15), pady=20)
botao = tk.Button(text="Clique aqui", font=("Arial", 10), pady=20, command=cont)
texto.pack()
subtexto.pack()
botao.pack()

janela.mainloop() """

