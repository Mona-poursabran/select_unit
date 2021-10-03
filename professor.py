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


    def students_list_chosen_lesson(self, code_lesson):
        """"
        check which students have chosen the same lesson 
        param : code_lesson
        inner func : first check if this lesson code is available
        print students' names
        """  
        def check_code(code_lesson):
            read = HandleFile('lesson_info.csv').read_file()
            for row in read:
                if row['code_lesson'] == code_lesson:
                    return True 
        if check_code(code_lesson):     
            read_file = HandleFile("chosen_lesson.csv").read_file()
            list_students_having_same_lesson = [row['student_name'] for row in read_file 
                                                if code_lesson in ast.literal_eval(row['code_lesson'])]
            print("  student name  ")
            print('*' * 18)
            for i in list_students_having_same_lesson:
                print(i)
        else :
            logging.warning('lesson code is not available!')
            print('This lesson code is not available!')


    def chosen_course(self, code_lesson):
        def check(code_lesson):
            read = HandleFile('lesson_info.csv').read_file()
            for row in read:
                if row['code_lesson'] == code_lesson and row['Professor'] == "":
                    return True 

        if check(code_lesson) :
            read_file = HandleFile('lesson_info.csv')
            read = read_file.read_file()
            for row in read :
                if row['code_lesson'] == code_lesson:
                    self.total_units += int(row['units'])
                    row['Professor'] = self.lname
                    self.chosen_courses.append(row)
        
            read_file.write_info(read) 
            return self.chosen_courses             
        else :
            print('Perhapse this lesson code is not available\nor has been chosen by another professor')


    def save_chosen_course(self):
        read = HandleFile('chosen_course_pro.csv')
        read.append_info(self.chosen_courses)

