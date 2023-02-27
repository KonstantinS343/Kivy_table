from kivymd.uix.anchorlayout import MDAnchorLayout

from app.views.toolbar import tool_bar
from app.views.table import table
from app.views.dialog.add_student_window import add_new_student
from app.views.dialog.filter_student_window import Filter, show_result_of_filter

class View:
    def __init__(self, controller, app_object, get_all_student_function) -> None:
        self.controller = controller
        self.temp_filter_window = None
        self.add_dialog = add_new_student(controller)
        self.filter_student_dialog = Filter(controller)
        self.table = table(controller, get_all_student_function)
        self.tool_bar = tool_bar(controller, app_object)
        self.base_view = MDAnchorLayout(self.tool_bar, self.table)
    
    def open_add_student_window(self):
        self.add_dialog.open()
        
    def update_table(self):
        self.base_view.remove_widget(self.table)
        self.table = table(self.controller)
        self.base_view.add_widget(self.table)
    
    def open_filter_student_window(self):
        self.filter_student_dialog.build()
    
    def close_filter_window(self):
        self.filter_student_dialog.close()
        
    def open_filter_result_window(self, get_filter_result):
        self.temp_filter_window = show_result_of_filter(self.controller, get_filter_result)
        self.temp_filter_window.open()