from kivymd.app import MDApp
from kivymd.theming import ThemeManager

class ViewApp(MDApp):
    theme_cls = ThemeManager()
    title = 'Таблица'
    
    def build(self):
        return super().build()
    
ViewApp().run()