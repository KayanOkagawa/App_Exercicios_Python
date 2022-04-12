# Função para abrir links

def gerenciador_data(id_widget):
    import pandas as pd
    data = pd.io.parsers.read_csv('_utilidade_myapp/data_link.csv')
    for c in range(0, len(data)):
        if id_widget == data.iloc[c]['Name']:
            resultado = data.iloc[c]['Link']
            return resultado


def url_open(*id_widget):
    import webbrowser
    link = gerenciador_data(id_widget[1])
    webbrowser.open(link)


def gerador_button():
    import pandas as pd
    lista_index = list()
    data = pd.io.parsers.read_csv('_utilidade_myapp/data_link.csv')
    for c in range(2, len(data)):
        lista_index.append(data.iloc[c]['Name'])
    return lista_index


gerador_button()
