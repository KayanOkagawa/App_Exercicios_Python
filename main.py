from kivymd.app import MDApp
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from utilidade_app import gerador_button

# Configuração de dimensões da tela


Config.set('graphics', 'width', '1520')
Config.set('graphics', 'height', '720')
Config.write()

# Gerenciador das Screens


class Gerenciador_screen(ScreenManager):
    pass

# Screen principal


class Menu_screen(Screen):
    from utilidade_app import abrir_pagina

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def indice_ex(self, num):
        from utilidade_app import gerenciador_data
        if num == 1:
            indice = int(self.ids.label_index.name) + int(num)
            self.ids.label_index.name = str(indice)
            if indice > 120:
                indice = 1
                self.ids.label_index.name = str(indice)
        else:
            indice = int(self.ids.label_index.name) - (int(num)-1)
            self.ids.label_index.name = str(indice)
            if indice == 0:
                indice = 120
                self.ids.label_index.name = str(indice)
        conteudo = gerenciador_data(indice)
        self.ids.label_index.text = f'Exercício - {indice}'
        MDApp.get_running_app().root.get_screen('menu').ids.layout_esq.remove_widget(self.ids.logo_botao)
        MDApp.get_running_app().root.get_screen('menu').ids.layout_esq.remove_widget(self.ids.img_guana)


# Classe principal do aplicativo


class MySystem(MDApp):
    def build(self):
        return Gerenciador_screen()


MySystem().run()
