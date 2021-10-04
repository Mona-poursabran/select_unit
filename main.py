from student import Student
from education_admin import EducationAdmin
from professor import Professor
from user import User
from menus import *
from useraccount import *
import os, logging


logger = logging.getLogger("Entrence")
logging.basicConfig(filename="log.log", filemode="a",  format=" %(asctime)s : %(name)s: %(levelname)s: %(message)s")


num = 0
while num != 3 :
    try:
        menu()
        num =int(input("Choose: "))
        if num == 1 :
            """ 
            Register : First choose the role 
                        Second enter the necessary inputs 
                        Then according to the role create an instance for each role to register 
            """
            try:
                user_type = int(input("as which person you want to register?\n1.Student\n2.Education Administrator\n3.Professor\n"))
            
                username = input("username: ").title().strip()
                print( "YOUR password should have at least one number.\n"
                            "It should have at least one special symbol.\n"
                            "It should be between 6 to 20 characters long.\n")
                password = input("password: ")
                confirm = input("confirm your password: ")
                fname = input("First name: ").title().strip()
                lname = input("Last name: ").title().strip()
                if user_type == 1:
                    user_type = 'student'
                    student = Student(user_type, username, password,fname, lname)
                    student.confirmation(confirm)
                    student.studen_ID()
                    student.register()
                elif user_type == 2 :
                    user_type = 'edu_admin'
                    edu_admin = EducationAdmin(user_type, username, password, fname, lname)
                    edu_admin.confirmation(confirm)
                    edu_admin.register()
                elif user_type == 3 :
                    user_type = 'professor'
                    Pro = Professor(user_type, username, password, fname, lname)
                    Pro.confirmation(confirm)
                    Pro.register()

            except Exception as e :
                print("Entrence is not valid try again")
                logger.error("Entrance Error" , exc_info=True)
        
        elif num == 2 :
            """ 
            Log in :First create an user who is found 
                    Second check the usertype
                    Then according to the usertype create an instance for each position 
                    Finally each person can access to their menu 
            """
            username= input("username: ").title().strip()
            password = input("password: ").strip()
            os.system('cls')
            user = UserAccount(username, password) 
            user.login()
            if user.role == 'student': 
                student= Student(user.role, username, password, user.fname, user.lname)
                access_student()
                choice = int(input("choose a number to access to each part: "))
                while choice != 7 :
                    if choice == 1:
                        student.see_all_lessons()

                    elif choice == 2:
                        lesson = input("which lesson are you looking for? ").title()
                        student.search_lesson(lesson) 

                    elif choice == 3:
                        student.show_total_units()

                    elif choice == 4:
                        student.see_all_lessons()
                        print("Dear student you are supposed to choose 10 to 20 units:")
                        while student.total_units < 10:
                            code_lesson = input("code: ")
                            student.chosen_lesson(code_lesson)
                            if student.total_units >=10:
                                choose_unit=  input(f"You've got {student.total_units} units.\nDo you want to add more lessons?(y/n)")
                                if choose_unit =='y':
                                   while student.total_units < 20:
                                        code_lesson = input("Enter lesson code or q: ")
                                        if code_lesson == 'q':
                                           break
                                        else:
                                            student.chosen_lesson(code_lesson)
                                elif choose_unit == 'n' :
                                    break
                        student.save_chosen_lesson()
                    elif choice == 5 :
                        student.show_chosen_lesson_file() 
                    elif choice == 6 :
                        student.see_accepted_rejected_units()
                    access_student()
                    choice = int(input("choose a number to access to each part: ")) 
                    # os.system('cls') 
                user.log_out()


            elif user.role == 'edu_admin': 
                edu_admin = EducationAdmin(user.role, username, password, user.fname, user.lname)
                access_edu_admin()
                choice = int(input("choose a number to access to each part: "))
                while choice != 10:
                    if choice == 1:
                        edu_admin.see_all_lessons()

                    elif choice == 2:
                        lesson = input("which lesson are you looking for? ").title()
                        edu_admin.search_lesson(lesson) 

                    elif choice == 3:
                        edu_admin.show_total_units()

                    elif choice == 4:
                        print("Add important info:\n")
                        lesson_name= input("lesson name: ").title().strip()
                        professor = input("Professor: ").strip().title()
                        units= input("Units: ").strip()
                        capacity = input("Capacity of this course: ").strip()
                        remain_cap = input("Remaining capacity: ").strip()
                        code_lesson = input('code lesson: ').strip()
                        edu_admin.add_new_lesson(lesson_name,units, capacity, remain_cap, code_lesson, professor)
                    elif choice == 5:
                        lesson = input("lesson: ").title().strip()
                        edu_admin.choose_lesson_to_see_student_list(lesson)
                    elif choice == 6 :
                        edu_admin.list_students()
                    elif choice == 7 :
                        firsname = input("student name: ").title().strip()
                        studentid =  input("student id: ").strip()
                        edu_admin.search_students(firsname, studentid)
                    elif choice == 8 :
                        studentid = input('studentID: ')
                        edu_admin.choose_student_and_see_chosen_lessons(studentid)
                    elif choice == 9 :
                        studnet_lastname = input("Student's last name: ").title().strip()
                        student_ID = input('StudentID: ')
                        edu_admin.accept_reject_units(studnet_lastname, student_ID)
                        edu_admin.save_accept_reject()
                    access_edu_admin()
                    choice = int(input("choose a number to access to each part: ")) 
                    # os.system('cls') 
                user.log_out()

            elif user.role == 'professor' :
                pro = Professor(user.role, username, password, user.fname, user.lname)
                access_pro()
                choice = int(input("Choose a number to access to each part: "))
                while choice != 6 :
                    if choice == 1 :
                        pro.see_all_lesson()
                    elif choice == 2:
                        lesson = input("Which lesson are you looking for? ").title().strip()
                        pro.search_lesson(lesson)
                    elif choice == 3:
                        pro.see_all_lessons()
                        print("Dear Professor,\nYou are supposed to choose 10 to 15 units:")
                        while pro.total_units < 10 :    
                            code = input("Code lesson: ").strip()
                            pro.chosen_course(code)
                            if pro.total_units >=10:
                                choose_units = input(f"You've got {pro.total_units} units.\nDo you want to add more?y/n ")
                                if choose_units == 'y':
                                    code = input("Enter lesson code or q: ")
                                    if code == 'q':
                                        break
                                    else:
                                        pro.chosen_course(code)


                                elif choose_units =='n':
                                    break
                        pro.save_chosen_course()
                    elif choice == 4 :
                        pro.show_chosen_course()
                    elif choice == 5 :
                        code_lesson = input("Enter lesson's code: ").strip()
                        pro.students_list_chosen_lesson(code_lesson)
                    access_pro()
                    choice = int(input("Choose a number to access to each part: "))
                    os.system('cls') 
                user.log_out()

        

    except Exception as e :
        print("Invalid input Try again!\nPlease choose only options!") 
        logger.error("Invalid choice" , exc_info= True)