from kivymd.uix.anchorlayout import MDAnchorLayout

from app.views.toolbar import tool_bar
from app.views.table import table
from app.views.dialog.add_student_window import add_new_student

class View:
    def __init__(self, controller, app_object,**kwargs) -> None:
        super().__init__(**kwargs)
        self.controller = controller
        self.add_dialog = add_new_student(controller)
        self.table = table(controller)
        self.tool_bar = tool_bar(controller, app_object)
        self.base_view = MDAnchorLayout(self.tool_bar,
                                     self.table)
    
    def open_add_student_window(self):
        self.add_dialog.open()
        
    def update_table(self):
        self.base_view.remove_widget(self.table)
        self.table = table(self.controller)
        self.base_view.add_widget(self.table)
        print('AAAAAAAA')