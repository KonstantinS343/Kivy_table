

from app.views.view import View

class Contorller:
    def __init__(self, app_object) -> None:
        self.view = View(self, app_object)
    
    def get_root_view(self):
        return self.view.base_view