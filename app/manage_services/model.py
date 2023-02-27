from typing import *
import json

class Model:
    def __init__(self) -> None:
        self.__student_list: List[List] = []
        with open('data.json', 'r') as file:
             self.__student_list = json.load(file)
    
    def add_to_student_list(self, student_data):
        object = StudentModel()
        object.model_initiation(student_data['name'],
                                student_data['course'],
                                student_data['group'],
                                student_data['all_work'],
                                student_data['do_work'],
                                student_data['lang'])
        self.__student_list.append(object.create_data_for_table())
        self.save()
        self.view.update_table()
        
    @property
    def student_list(self):
        return self.__student_list
    
    def save(self):
        with open('data.json', 'w') as file:
            json.dump(self.__student_list,file,ensure_ascii=False)
    
    def delete(self, delete_template):
        self.__student_list[:] = [i for i in self.__student_list if i not in delete_template]
        self.view.update_table()
        with open('data.json', 'w') as file:
           json.dump(self.__student_list,file,ensure_ascii=False)
        
    def init_view(self, view):
        self.view = view

class StudentModel:
    def __init__(self) -> None:
        self.student_name: str = None
        self.student_course: int = None
        self.student_group: int = None
        self.amount_all_student_work: int = None
        self.amount_do_student_work: int = None
        self.programming_lang: str = None
        
    def model_initiation(self,
                          name: str,
                          course: int,
                          group: int,
                          amount_all_work: int,
                          amout_do_work: int,
                          programming_lang: str
                          ):
        self.student_name = name
        self.student_course = course
        self.student_group = group
        self.amount_all_student_work = amount_all_work
        self.amount_do_student_work = amout_do_work
        self.programming_lang = programming_lang
    
    def create_data_for_table(self):
        return [
            self.student_name,
            self.student_course,
            self.student_group,
            self.amount_all_student_work,
            self.amount_do_student_work,
            self.programming_lang,
        ]