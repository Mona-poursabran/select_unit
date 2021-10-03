import re, csv,random
from hashlib import sha256
from filehandler import HandleFile
class User:
    """
    This is parent class 
    Attributes : username, password, fname, laname, usertype, userid(for students)
    Methods : validation_username, validation_password, confirmation,register, save_info 
    """
   
    long_in_user = []
    def __init__ (self,user_type, username, password, fname, lname) :
        self.usertype = user_type
        self.username = self.validation_username(username)
        self.password = self.validation_password(password)
        self.fname = fname
        self.lname = lname



    def validation_username(self, username):
        if len(username) >=3 :
            return username
        else :
            print('This username is invalid!')


    def validation_password(self, password) :
        # check the password to be valid:
        password= "".join(password.split())  # if there is whitespace clean it 
        regex = "^(?=.*[a-z])(?=.*\d)(?=.*[@$!%*#?&_])[A-Za-z\d@$!#%*?&_]{6,20}$"  # make a pattern    
        pattern = re.compile(regex)
        mat = re.search(pattern, password)
        if mat:
            return sha256(str(password).encode()).hexdigest()
        else:
            print("INvalid password!")


    def confirmation(self, confirm) :
        if self.password:
            while confirm ==""  or sha256(str(confirm).encode()).hexdigest() != self.password:
                print('Confirm_password is not as same as the password')
                confirm = input("confirm your password: ")   
            else: # check if there is the same username and password in the file
                return True
    

    def register(self):
        if self.username and self.password and self.confirmation:
            read_file = HandleFile('user_info.csv').read_file()
            for row in read_file:
                if row['username'] == self.username and row['password'] == self.password and row['usertype']== self.usertype: 
                    print('There is someone with this username and password')
                    break
            else: # clall save method here when there is no same user 
                print(f"User: {self.username} is registered successfully.")
                self.save_info()
                if self.usertype == 'student':
                    print(f'This is your student ID: {self.userid}')
    
                     
    def save_info (self):  
        if self.password and self.username :
            file = HandleFile('user_info.csv')
            file.append_info([self.__dict__])
     
