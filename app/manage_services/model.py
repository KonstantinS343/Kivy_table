from typing import *

class Model:
    def __init__(self) -> None:
        self.__student_list: List[List] = []
    
    def add_to_student_list(self):
        object = StudentModel()
        object.model_initiation('Свяцкий Вячеслав Александрович',
                                2,
                                121703,
                                20,
                                1,
                                'Basic')
        self.__student_list.append(object.create_data_for_table())
    
    def get_student_list(self):
        return self.__student_list

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