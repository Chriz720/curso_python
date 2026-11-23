import tkinter as tk 
janela = tk.Tk()
janela.title("Texto")
janela.geometry("300x300")
janela.resizable(False, False)

texto = tk.Label(text="Hello, World!", font=("NewTimesRoman", 30), pady=30)
texto.pack()

janela.mainloop()