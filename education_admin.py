from filehandler import HandleFile
from student import Student
import logging, ast
from prettytable import *

class EducationAdmin(Student):
    """
    This class is inherited from student since some parts are the same
    such as init and sreach lesson , see all lessons, show_total_units
    Other Methods : add_new_lessons, 
    """
    def __init__(self,user_type, username, password, fname, lname):
        super().__init__(user_type,username, password, fname, lname)


    def see_all_lessons(self):
        return super().see_all_lessons()


    def search_lesson(self, lesson):
        return super().search_lesson(lesson)


    def show_total_units(self):
        return super().show_total_units()


    def add_new_lesson(self, lesson_name,units, capacity, remain_cap, code_lesson,professor=''):
        """ 
        Logging : Missing argument or orgument is not ok
        Logging : if there is repeated lesson code
        if everything is ok add new lesson to file
        return nothing 
        """
        logger=logging.getLogger("Add new lesson")
        logging.basicConfig(filename="log.log", filemode="a",  format=" %(asctime)s : %(name)s: %(levelname)s: %(message)s")
        
        if lesson_name.isalnum()  and units.isnumeric() and capacity.isnumeric() and remain_cap.isnumeric() and code_lesson.isalnum():

            list_dic = {"lesson_name":lesson_name, "Professor": professor, "units":units, "capacity":capacity, 
                        "remain_cap":remain_cap, "code_lesson":code_lesson}

            read_file = HandleFile('lesson_info.csv')
            read = read_file.read_file()
            for row in read:
                if row['code_lesson'] == code_lesson:
                    logger.error('Using repeated lesson code')
                    print(f'{code_lesson}: This lesson code has already used!')
                    break
            else:
                read_file.append_info([list_dic])
        else :
            logger.error("You have faced an error!\nMissign argument or Invalid input")
            print("You have faced an error!\nMissign argument or Invalid input")
