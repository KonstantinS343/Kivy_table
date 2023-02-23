from kivy.config import Config
Config.set("graphics", "resizable", 0)
Config.set("graphics", "width", 950)
Config.set("graphics", "height", 600)

from kivymd.app import MDApp
from kivymd.theming import ThemeManager

from app.manage_services.controller import Contorller

class App(MDApp):
    theme_cls = ThemeManager()
    title = 'Таблица'
    
    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.8
        controller = Contorller(self)
        return controller.get_root_view()
    
    def switch_theme_style(self, *args):
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )