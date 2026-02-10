#Pedir palavra ao usuário
#Armazenar palavra 
#Receber pasta de arquivos 
#Abrir pasta 
#Abrir arquivo 
#Ler texto 
#Procurar palavra
#Armazenar nome do arquivo em lista, caso tenha a palavra 
#Mostrar lista de nome de arquivos

from os import listdir

def filtrar_texto(caminho, filtro):
    resultados = []
    for x in listdir(caminho):
        f = open(f'{caminho}/{x}', "r", encoding="utf-8", errors="replace")
        a = f.read()
        if filtro.upper() in a:
            resultados.append(x)
        f.close()

    return resultados