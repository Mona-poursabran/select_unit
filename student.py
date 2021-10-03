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
        

    def chosen_lesson(self,code_lesson):
        """
        param: code_lesson
        in this method student can chose a lesson 
        first add chosen lessons in self.chosen_lesson
        then return one dictionary in order to save in a file 
        """
        
        read_file = HandleFile('lesson_info.csv')
        read = read_file.read_file()
        for row in read:
            if row['code_lesson'] == code_lesson and int(row['remain_cap']) > 0 :
                self.chosen_lessons.append(row)
                self.total_units += int(row['units'])
                row['remain_cap'] = int(row['remain_cap']) - 1
            
            read_file.write_info(read)

        read_user_info = HandleFile('user_info.csv').read_file()
        self.chosen_lesson_info= {'student_name':self.fname+" "+self.lname, 'lessons':[dic['lesson_name'] for dic in self.chosen_lessons],
                                'professor':[row['Professor'] for row in self.chosen_lessons],'units':[row['units'] for row in self.chosen_lessons],
                                'id':[row['userid'] for row in read_user_info if row['lname'] == self.lname],'code_lesson':[dic['code_lesson'] for dic in self.chosen_lessons]}
        return self.chosen_lesson_info

    def show_chosen_lesson_file(self):
        """
        if the student chose lessons before   
        """
        read = HandleFile('chosen_lesson.csv').read_file()
        for row in read :
            if row['student_name'] == self.fname + " " + self.lname :
                t = PrettyTable(['lesson', 'pro','unit', 'code'])
                lessons = [ast.literal_eval(row['lessons'])]
                professor= [ast.literal_eval(row['professor'])]
                unit = [ast.literal_eval(row['units'])]
                code = [ast.literal_eval(row['code_lesson'])]
                for i in range(len(lessons[0])):
                    t.add_row([lessons[0][i], professor[0][i], unit[0][i], code[0][i]])
                print(t) 
                break    
        else :
            print('No lessons have been chosen yet!')
        

    def save_chosen_lesson(self):
        save = HandleFile('chosen_lesson.csv')
        save.append_info(self.chosen_lesson_info)


