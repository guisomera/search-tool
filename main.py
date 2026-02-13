import tkinter as tk 
from tkinter import filedialog, scrolledtext
from actions import filtrar_texto
import os

estado = { 
    "loc pasta":"",
    "palavra busca": ""
}

def limpar_resultados():
    resultados.config(state="normal") #Deixa editavel
    resultados.delete("1.0", "end") #Limpa tudo
    resultados.config(state="disabled") #Tira o editavel 

def mostrar_mensagem_centro(msg):
    resultados.config(state="normal")
    resultados.delete("1.0", "end")
    resultados.insert("1.0", msg)
    resultados.tag_configure("center", justify="center")
    resultados.tag_add("center", "1.0", "end")
    resultados.config(state="disabled")

def mostrar_texto_esqueda(texto):
    resultados.config(state="normal")
    resultados.delete("1.0", "end")
    resultados.tag_remove("center", "1.0", "end") #Garante que nao fica centralizado
    resultados.insert("1.0", texto)
    resultados.config(state="disabled")


def buscar ():
    estado["palavra busca"] = entry.get().strip()
    caminho = estado["loc pasta"]
    filtro = estado["palavra busca"]

    if not caminho:
        mostrar_mensagem_centro("Selecione uma pasta primeiro")
        return
    elif not filtro:
        mostrar_mensagem_centro("Digite uma palavra para buscar")
        return

    mostrar_mensagem_centro("Buscando arquivos...")
    root.after(200, executar_busca)
    
def executar_busca():
    caminho = estado["loc pasta"]
    filtro = estado["palavra busca"]

    encontrados = filtrar_texto(caminho, filtro)
    print(f"Arquivos encontrados: {encontrados}") #Visualização no terminal

    if encontrados:
        texto = "Arquivos encontrados: \n"

        for c in encontrados:
            texto += f"- {c}\n" 
        mostrar_texto_esqueda(texto)
    else:
        mostrar_mensagem_centro("Nenhum arquivo possui essa palavra")

def diretorio():
    #Abrir diretório para escolher arquivo // Funcionalidade do botão 
    directory_path = filedialog.askdirectory(
        title="Escolha um arquivo",
        initialdir="/"
    )
    
    if directory_path:
        output_diretorio.config(text=f"Pasta selecionada:\n {directory_path}")
    else:
        output_diretorio.config(text=f"Seleção cancelada")
        

    estado["loc pasta"] = directory_path

root = tk.Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1)
root.geometry("1000x500")

root.title("Busca de arquivos")

#Frame titulo
frame_titulo = tk.Frame(root, bg="#D3D3D3")
frame_titulo.grid(row=0, column= 0, sticky="nsew")
frame_titulo.columnconfigure(0, weight=1)

titulo = tk.Label(frame_titulo, text="BUSCAR ARQUIVOS - CONTAS A PAGAR", bg="#D3D3D3", font=("Arial", 18, "bold"))
titulo.grid(row= 0, pady= 20)

#Frame controles
frame_controles = tk.Frame(root, bg="#D3D3D3")
frame_controles.grid(row=1, column=0, sticky="we")
frame_controles.columnconfigure(0, weight=1)

botao_abrir_arquivo = tk.Button(frame_controles, text="Selecionar pasta", command=diretorio) #Cria o botão com texto e funcionaliadd
botao_abrir_arquivo.grid(row= 0, column=0)#Coloca o botão na tela 

output_diretorio = tk.Label(frame_controles, text="", bg="#D3D3D3", font=("Arial", 10))
output_diretorio.grid(row=1, pady= 15)

instrucao_entry = tk.Label(frame_controles, text="Palavra para buscar", bg="#D3D3D3", font=("Arial", 10))
instrucao_entry.grid(row=2)

entry = tk.Entry(frame_controles, width= 25)
entry.grid(row=3, pady= 5)

botao_buscar = tk.Button(frame_controles, text="Buscar", command=buscar)
botao_buscar.grid(row= 4, pady=5)

#Frame resultados
frame_resultados = tk.Frame(root, bg="#D3D3D3")
frame_resultados.grid(row= 2, column=0, sticky="nsew")
frame_resultados.columnconfigure(0, weight=1)

title_resultados = tk.Label(frame_resultados, text="RESULTADOS:", bg="#D3D3D3", font=("Arial", 10, "bold"))
title_resultados.grid(row= 0, pady= 10)

resultados = scrolledtext.ScrolledText(frame_resultados,
                                       width = 70,
                                       height = 20,
                                       font=("Arial", 10),
                                       bg= "White")
resultados.grid(row= 1, column= 0)
mostrar_mensagem_centro("Selecione uma pasta e digite uma palavra para iniciar a busca")

root.mainloop()