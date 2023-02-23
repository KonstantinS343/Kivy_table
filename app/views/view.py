from kivymd.uix.boxlayout import MDBoxLayout

from app.views.toolbar import tool_bar

class View:
    def __init__(self, controller, app_object) -> None:
        self.tool_bar = tool_bar(controller, app_object)
        self.base_view = MDBoxLayout(self.tool_bar)