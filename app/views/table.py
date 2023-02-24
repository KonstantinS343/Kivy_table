from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.metrics import dp

def table(controller: object): 
    return MDBoxLayout(
        MDDataTable(
            size_hint=(0.9, 0.93),
            use_pagination=True,
            check=True,
            column_data=[
                ("ФИО студента", dp(90)),
                ("Курс", dp(30)),
                ("Группа", dp(30)),
                ("Общее число работ", dp(30)),
                ("Количество выполненных работ", dp(30)),
                ("Язык программирования", dp(30)),
            ],
            row_data=controller.get_student(),
            
        ))
    
    
    
    
