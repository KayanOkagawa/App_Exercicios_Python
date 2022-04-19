def gerenciador_data(id_widget):
    import pandas as pd
    data = pd.io.parsers.read_csv('data_link.csv')
    for c in range(0, len(data)):
        if id_widget == data.iloc[c]['Name']:
            resultado = [data.iloc[c]['Link'], data.iloc[c]['Exercicios']]
            return resultado


def abrir_pagina(*id_widget):
    import webbrowser
    link = gerenciador_data(id_widget[1])
    return webbrowser.open(link)


def gerador_button():
    import pandas as pd
    lista_index = list()
    data = pd.io.parsers.read_csv('data_link.csv')
    for c in range(2, len(data)):
        lista_index.append(data.iloc[c]['Name'])
    return lista_index
