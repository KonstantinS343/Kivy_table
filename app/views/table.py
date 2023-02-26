from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.metrics import dp

def table(controller: object): 
    return MDBoxLayout(
        MDDataTable(
            size_hint=(0.9, 0.93),
            use_pagination=True,
            elevation=2,
            check = True,
            column_data=[
                ("ФИО студента", dp(90)),
                ("Курс", dp(45)),
                ("Группа", dp(60)),
                ("Общее число работ", dp(60)),
                ("Кол-во выполненных работ", dp(60)),
                ("Язык программирования", dp(60)),
            ],
            row_data=controller.get_student(),
        
        ))
    
    
    
    
