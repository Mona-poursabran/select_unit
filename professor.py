from filehandler import HandleFile
from student import Student
from prettytable import *
import ast, logging

logging.basicConfig(filename="log.log", filemode="a",  format=" %(asctime)s : %(levelname)s: %(message)s")


class Professor(Student):
    """
    This class is inherited from student since some parts are the same
    such as init and sreach lesson 
    Other Methods : see all lesson(lessons name and units), students_list_chosen_lesson, chosen_lesson
    """
    chosen_courses = []
    total_units =0
    def __init__(self, user_type, username, password, fname, lname):
        super().__init__(user_type, username, password, fname, lname)


    def search_lesson(self, lesson):
        return super().search_lesson(lesson)
 

    def see_all_lesson(self):
        """"
        As it is written in the project 
        professor is supposed to see list of lessons
        with their units
        """ 
        with open('lesson_info.csv', 'r') as f:
            mytable = from_csv(f)
        print(mytable.get_string(fields=["lesson_name", "units"]))
