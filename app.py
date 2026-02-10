import tkinter as tk 
from tkinter import filedialog
from actions import filtrar_texto

estado = { 
    "loc pasta":"",
    "palavra busca": ""
}

def buscar ():
    estado["palavra busca"] = entry.get()
    caminho = estado["loc pasta"]
    filtro = estado["palavra busca"]

    if not caminho:
        resultados.config(text="Selecione um caminho primeiro")
        return
    elif not filtro:
        resultados.config(text="Escolha uma palavra para buscar")
        return

    encontrados = filtrar_texto(caminho, filtro)
    print(f"Arquivos encontrados: {encontrados}")

    if encontrados != []:
        texto = "Arquivos encontrados: \n"
        nomes_arquivos = ""

        for c in encontrados:
            nomes_arquivos += f"- {c}\n" 
        texto += nomes_arquivos
        resultados.config(text=texto)
    else:
        resultados.config(text="Nenhum arquivo possui essa palavra")

def diretorio():
    #Abrir diretório para escolher arquivo // Funcionalidade do botão 
    directory_path = filedialog.askdirectory(
        title="Escolha um arquivo",
        initialdir="/"
    )
    
    if directory_path:
        output_diretorio.config(text=f"O caminho selecionado foi: {directory_path}")
    else:
        output_diretorio.config(text=f"Seleção cancelada")
        

    estado["loc pasta"] = directory_path

root = tk.Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1)

root.title("Busca de arquivos!")

#Frame titulo
frame_titulo = tk.Frame(root, bg="#D3D3D3")
frame_titulo.grid(row=0, column= 0, sticky="nsew")
frame_titulo.columnconfigure(0, weight=1)

titulo = tk.Label(frame_titulo, text="BUSCAR ARQUIVOS - CONTAS A PAGAR", bg="#D3D3D3"  )
titulo.grid()

#Frame controles
frame_controles = tk.Frame(root, bg="#D3D3D3")
frame_controles.grid(row=1, column=0, sticky="we")
frame_controles.columnconfigure(0, weight=1)

botao_abrir_arquivo = tk.Button(frame_controles, text="Selecionar arquivos", command=diretorio) #Cria o botão com texto e funcionaliadd
botao_abrir_arquivo.grid(row= 0, column=0, pady= 15) #Coloca o botão na tela 

output_diretorio = tk.Label(frame_controles, text="", bg="#D3D3D3")
output_diretorio.grid(row=1)

entry = tk.Entry(frame_controles)
entry.grid(row=2, pady= 15)

botao_buscar = tk.Button(frame_controles, text="Buscar", command=buscar)
botao_buscar.grid(row= 3, pady=5)

#Frame resultados
frame_resultados = tk.Frame(root, bg="#D3D3D3")
frame_resultados.grid(row= 2, column=0, sticky="nsew")
frame_resultados.columnconfigure(0, weight=1)

resultados = tk.Label(frame_resultados, text="", bg="#D3D3D3")
resultados.grid(row= 0, column= 0, sticky="we")

root.mainloop()