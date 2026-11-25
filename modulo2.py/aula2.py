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

""" import tkinter as tk
janela = tk.Tk()
janela.title("Cadastro")
janela.geometry("500x500")
janela.resizable(False, False)

lblNome = tk.Label(janela, text="Nome:", font=("Arial", 10))
nome = tk.Entry(janela, width=30)

lblIdade = tk.Label(janela, text="Idade:")
idade = tk.Entry(janela, width=30)

lblEmail = tk.Label(janela, text="Email:")
email = tk.Entry(janela, width=30)

resultado = tk.Label(janela, text="clique em cadastrar", font=("Arial", 12))

def cadastrar():
    if nome.get().strip() == "" or email.get().strip() == "":
        resultado.config(text="Todos os campos são obrigatórios!", fg="red")
    elif not idade.get().isdigit() or int(idade.get()) <= 0:
        resultado.config(text="Idade inválida!", fg="red")
    else:
        resultado.config(text="Cadastro com sucesso!", fg="green")

btmConfirmar = tk.Button(janela, text="Confirmar", command=cadastrar)

lblNome.grid(row=0, column=0)
nome.grid(row=0, column=1)
lblIdade.grid(row=1, column=0)
idade.grid(row=1, column=1)
lblEmail.grid(row=2, column=0)
email.grid(row=2, column=1)
btmConfirmar.grid(row=3, column=0, columnspan=2)
resultado.grid(row=4, column=0, columnspan=2)

janela.mainloop() """

