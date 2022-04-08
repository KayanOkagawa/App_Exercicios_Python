from kivymd.app import MDApp
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen

# Configuração de dimensões da tela

Config.set('graphics', 'width', '1520')
Config.set('graphics', 'height', '720')
Config.write()

# Gerenciador das Screens


class Gerenciador_screen(ScreenManager):
    pass

# Screen principal


class Menu_screen(Screen):
    from _utilidade_myapp import url_open

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


# Classe principal do aplicativo


class MyApp(MDApp):
    def build(self):
        return Gerenciador_screen()


MyApp().run()
