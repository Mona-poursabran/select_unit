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



    def choose_lesson_to_see_student_list(self, lesson):
        """"
        check which students have chosen the same lesson 
        param : lesson
        inner def : first check this lesson if available 
        print students' names
        """  
        def check_lesson(lesson):
            read = HandleFile('lesson_info.csv').read_file()
            for row in read:
                if row['lesson_name'] == lesson:
                    return True
        if check_lesson(lesson):
            read = HandleFile('chosen_lesson.csv').read_file()
            list_students_having_same_lesson=[row['student_name'] for row in read if lesson in ast.literal_eval(row['lessons'])]
            print("  student name  ")
            print('*' * 18)
            for i in list_students_having_same_lesson:
                print(i)
        else:
            print('This lesson is not available!')


    def list_students(self):
        """
        show students' name and their ID
        """
        read = HandleFile('user_info.csv').read_file()
        list_students = [(row['username'], row['userid']) for row in read if row['usertype'] == 'student']
        mytable= PrettyTable()
        mytable.field_names =["Student name","StudentID"]
        mytable.add_rows(list_students)
        print(mytable)

    
    def search_students(self, student_name, student_id):
        """
        search students by using their fname and student id
        logging : if the student can't be found 
        show the table which includes students info 
        """        
        read = HandleFile('user_info.csv').read_file()
        list_chosen_student =[(row['fname'], row['lname'], row['userid']) for row in read if row['usertype'] == 'student' 
                                    if row['fname'] == student_name and row['userid'] == student_id]
        mytable= PrettyTable()
        mytable.field_names =["First name","Last name","Student ID"]
        if not list_chosen_student:
            print(f"{student_name} is not found!")
        else:
            mytable.add_rows(list_chosen_student)
            print(mytable)


    def choose_student_and_see_chosen_lessons(self, studentid):
        """
        choose one student and check chosen lessons
        param : studentid
        inner func : first check if this student is available
        Finally check if student has choosen any lessons
        """
        list_student_chosen_lesson=[]
        def check_student(studentid):
            read = HandleFile('user_info.csv').read_file()
            for row in read:
                if row['userid'] == studentid:
                    return True

        if check_student(studentid) :
            read = HandleFile('chosen_lesson.csv').read_file()
            for row in read :
                if ast.literal_eval(row['id']) == [studentid] :
                    units = [int(unit) for unit in ast.literal_eval(row['units'])]
                    string_lesson = ''
                    for lesson in ast.literal_eval(row['lessons']):
                        string_lesson += lesson + "  "
                    list_student_chosen_lesson .append((row['student_name'], string_lesson, sum(units)))
    
            mytable= PrettyTable()
            mytable.field_names =["student_name","lessons", "units"]
            if not list_student_chosen_lesson :
                print("This student hasn't chosen lessons yet!")
            else:
                mytable.add_rows(list_student_chosen_lesson)
                print(mytable) 
        else:
            print('This student is not available')


    def accept_reject_units(self,lname, studentid):
        """
        params: student last name and student ID
        first find the student from user info according to the lname and id
        second create an student object in order to see chosen lessons
        third edu admin chose the lesson code as accepted or rejected lessons
        fourth check if each lesson is rejected one is added to remain capacity 
        finally create a dic
        return dic 
        """
        file_chosen_lesson = HandleFile('chosen_lesson.csv').read_file()
        file_lesson_info = HandleFile('lesson_info.csv')
        accepted_lessons = []
        rejected_lessons = []
        read=HandleFile('user_info.csv').read_file()
        for row in read:
            if row['lname'] == lname and row['userid'] == studentid:
                student= Student(row['usertype'], row['username'],'abc_10', row['fname'], row['lname'])
                student.show_chosen_lesson_file()
                code=''
                while code != 'q':
                    code = input('accepted code or q: ')
                    accepted_lessons.append(code)
                code =''   
                while code != 'q':
                    code = input('rejected code or q: ')
                    rejected_lessons.append(code)
        
                break
        else :
            print("This student is not availble!") 
        read_lesson_info = file_lesson_info.read_file()
        for row in read_lesson_info:
            for code_lesson in rejected_lessons:
                if code_lesson in row['code_lesson']:
                    row['remain_cap'] = int(row['remain_cap']) + 1
            file_lesson_info.write_info(read_lesson_info)
              
        accepted_units=[code_lesson for row in file_chosen_lesson 
                                    for code_lesson in accepted_lessons if code_lesson in row['code_lesson']]
        rejected_units = [code_lesson for row in file_chosen_lesson 
                        for code_lesson in rejected_lessons if code_lesson in row['code_lesson']]
        self.dic = {'name':student.fname+" "+student.lname, 'accepted_units':accepted_units, 'rejected_units': rejected_units}  
        return self.dic


    def save_accept_reject(self):
        """ save dic which includes student name , accepted lessons and rejected ones"""
        file = HandleFile('accept_reject.csv')
        file.append_info([self.dic])

