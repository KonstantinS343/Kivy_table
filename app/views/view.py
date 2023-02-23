from kivymd.uix.anchorlayout import MDAnchorLayout

from app.views.toolbar import tool_bar
from app.views.table import table

class View:
    def __init__(self, controller, app_object) -> None:
        self.table = table()
        self.tool_bar = tool_bar(controller, app_object)
        self.base_view = MDAnchorLayout(self.tool_bar,
                                     self.table)