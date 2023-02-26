from app.views.view import View
from app.manage_services.model import Model
from app.manage_services.validator import Validator

class Controller:
    def __init__(self, app_object) -> None:
        self.model = Model()
        self.view = View(self, app_object)
    
    def get_root_view(self):
        return self.view.base_view
    
    def get_student(self):
        return self.model.get_student_list()
    
    def open_add_window(self):
        self.view.open_add_student_window()
        
    def add_student_in_table(self):
        
        def create_student_data():
            return {
                'name':data_from_add_dialog_window.name.text,
                'course':data_from_add_dialog_window.course.text,
                'group':data_from_add_dialog_window.group.text,
                'all_work':data_from_add_dialog_window.all_work.text,
                'do_work':data_from_add_dialog_window.do_work.text,
                'lang':data_from_add_dialog_window.lang.text,
            }
        
        self.close_add_window()
        data_from_add_dialog_window = self.view.add_dialog.content_cls.ids
        validation = Validator(data=data_from_add_dialog_window)
        validation.validate()
        
        self.model.add_to_student_list(student_data=create_student_data())
        self.view.update_table()
    
    def close_add_window(self):
        self.view.add_dialog.dismiss()
        