from app.views.view import View
from app.manage_services.model import Model

class Controller:
    def __init__(self, app_object) -> None:
        self.model = Model()
        self.model.add_to_student_list()
        self.view = View(self, app_object)
    
    def get_root_view(self):
        return self.view.base_view
    
    def get_student(self):
        return self.model.get_student_list()