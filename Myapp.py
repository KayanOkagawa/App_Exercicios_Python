from kivymd.app import MDApp
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

# Configuração de dimensões da tela
from _utilidade_myapp import gerador_button

Config.set('graphics', 'width', '1520')
Config.set('graphics', 'height', '720')
Config.write()

# Gerenciador das Screens


class Gerenciador_screen(ScreenManager):
    pass


# Screen principal


class Menu_screen(Screen):
    from _utilidade_myapp import url_open, gerador_button

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Box_ex(BoxLayout):
    from _utilidade_myapp import gerador_button

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        lista = gerador_button()
        for item in lista:
            self.add_widget(Button(name=item, text=f'Exercicio - {item}', size_hint_y=None, size_hint_x=0.5))


# Classe principal do aplicativo


class MyApp(MDApp):
    def build(self):
        return Gerenciador_screen()


MyApp().run()
