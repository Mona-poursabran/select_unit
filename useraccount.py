from hashlib import sha256
import csv, logging
from filehandler import HandleFile
class UserAccount:
    log_in_user = []
    role=""
    fname= ''
    lname= ''
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = sha256(str(password).encode()).hexdigest()  # conver to hash
        
    # check that user is in the file in order let log in 
    def login(self): 
        # Return a logger with the specified name 
        logger=logging.getLogger("LogIn")
        # save each log in the file log.log with this special format
        logging.basicConfig(level=logging.INFO,filename="log.log", filemode="a",  format=" %(asctime)s : %(name)s: %(levelname)s: %(message)s")
        
        #open the file to search the username 
        file_read  =HandleFile('user_info.csv').read_file()

        for row in file_read:
            if row['username'] == self.username and row['password'] == self.password :
                self.role = row['usertype']
                self.fname = row['fname']
                self.lname = row['lname']
                self.log_in_user.append((row["username"], row['password']))
                logger.info(f"{self.username} is logging")
                print(f"Your role:{row['usertype']}")
                break
        else:
            logger.error('Username or Password is not found!')
            print('Username or Password is not found!')

    def log_out(self):
        logger=logging.getLogger("LogOut")
        print(f"Username: {self.username} : You are logged out!")
        logger.info(f"{self.username} is logging out.")
        UserAccount.log_in_user.remove((self.username,self.password))