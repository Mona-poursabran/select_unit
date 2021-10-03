import csv, random
from prettytable import PrettyTable, from_csv
import logging,os, ast
from filehandler import HandleFile
from user import User
from datetime import datetime

class Student (User):
    """
    Student class is a child class of User class to check some validation
    Attributes : usertype, username, password, fname, lname, chosen_lesson and total_units
    Methods : see_all_lessons, search lesson, show_total_units , chosen_lessons
    """
    chosen_lessons = []
    total_units = 0

    def __init__ (self,  user_type,username, password, fname, lname) :
        super().__init__(user_type, username, password, fname, lname)


    def see_all_lessons(self):
        """
        in this method student is able to see all info about lessons
        such as lesson names, units, capacity, remain capacity , lesson code and even professor 
        """
        with open('lesson_info.csv', 'r') as f:
            mytable = from_csv(f)
        print(mytable)
   
   
    def search_lesson(self, lesson):
        """
        in this method student is able to look for a lesson
        """
        logger=logging.getLogger("Search the lesson")
        logging.basicConfig(filename="log.log", filemode="a",  format=" %(asctime)s : %(name)s: %(levelname)s: %(message)s")

        read = HandleFile('lesson_info.csv').read_file()
        lst_lesson=[row for row in read if row['lesson_name'] == lesson]
        table = PrettyTable()
        table.field_names = ['lesson_name','professor', 'units', 'capacity', 'remain_cap', 'code_lesson']
        if not lst_lesson:
            logger.warning("This lesson is not found!")
            print("This lesson is not found!")
        else:
            lst_lesson = lst_lesson[0].values()
            table.add_rows([lst_lesson])
            print(table)


    def show_total_units(self):
        read = HandleFile('lesson_info.csv').read_file()
        list_units=[int(row['units']) for row in read]        
        print("Total Units: ",sum(list_units))


    def studen_ID(self): 
        self.userid = str(f'{datetime.now().year}{random.randint(1, 100)}{datetime.now().second}{self.fname[2]}')
        return self.userid




