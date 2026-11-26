import tkinter as tk

janela = tk.Tk()
janela.title("SocorrOS Assistência Técnica")
janela.geometry("560x430")
janela.configure(padx=15, pady=15)

janela.grid_columnconfigure(1, weight=1)

lbl_titulo = tk.Label(
    janela,
    text="SOCORROS INFORMATICA - GERENCIAMENTO DE ORDENS DE SERVICO",
    font=("Arial", 10, "bold"),
    relief="solid",
    bd=1,
    pady=8,
    anchor="w",
    padx=10
)
lbl_titulo.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 10))

frame_form = tk.Frame(janela, relief="solid", bd=1, padx=12, pady=12)
frame_form.grid(row=1, column=0, columnspan=2, sticky="nsew")
frame_form.grid_columnconfigure(1, weight=1)

lbl_subtitulo = tk.Label(frame_form, text="NOVA ORDEM DE SERVICO", font=("Arial", 10, "bold"))
lbl_subtitulo.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

campos = [
    ("Cliente:", 1),
    ("Telefone:", 2),
    ("Equipamento:", 3),
    ("Marca/modelo:", 4),
    ("Valor:", 5),
]

entradas = {}
for texto, linha in campos:
    lbl = tk.Label(frame_form, text=texto)
    lbl.grid(row=linha, column=0, sticky="w", pady=4, padx=(0, 15))

    ent = tk.Entry(frame_form)
    ent.grid(row=linha, column=1, sticky="ew", pady=4)
    entradas[texto] = ent

lbl_problema = tk.Label(frame_form, text="Problema:")
lbl_problema.grid(row=6, column=0, sticky="nw", pady=4, padx=(0, 15))

txt_problema = tk.Text(frame_form, height=2, width=30)
txt_problema.grid(row=6, column=1, sticky="ew", pady=4)

lbl_situacao = tk.Label(frame_form, text="Situacao inicial: Pendente")
lbl_situacao.grid(row=7, column=0, columnspan=2, sticky="w", pady=(8, 12))

frame_botoes = tk.Frame(frame_form)
frame_botoes.grid(row=8, column=0, columnspan=2, pady=(5, 0))

def limpar_campos():
    for ent in entradas.values():
        ent.delete(0, tk.END)
    txt_problema.delete("1.0", tk.END)

btn_cadastrar = tk.Button(frame_botoes, text="Cadastrar OS", width=15)
btn_cadastrar.grid(row=0, column=0, padx=8)

btn_limpar = tk.Button(frame_botoes, text="Limpar campos", width=15, command=limpar_campos)
btn_limpar.grid(row=0, column=1, padx=8)

janela.mainloop()