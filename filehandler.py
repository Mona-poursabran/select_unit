import csv
"""
this class just try to handle file 
such as reading and writing a file :)
"""
class HandleFile :
    def __init__ (self, file_path):
        self.file_path = file_path

    def read_file (self):
        with open (self.file_path, 'r') as read_file :
            readerdict = csv.DictReader(read_file)
            return(list(readerdict))
    
    def write_info (self, new_value):
# check this new value is dict or list of dict
        if isinstance (new_value, dict):
            field = new_value.keys()
            new_value = [new_value]
        elif isinstance(new_value, list):
            field = new_value[0].keys()

        with open (self.file_path, 'w', newline='') as f_append :  # this part helps if the file is full the info is not appened agian 
            write = csv.DictWriter(f_append, fieldnames= field)
            # check just put header top of the file 
            if f_append.tell() == 0:
                write.writeheader()
            write.writerows(new_value)

    def append_info(self, new_value):
        # check this new value is dict or list of dict
        if isinstance (new_value, dict):
            field = new_value.keys()
            new_value = [new_value]
        elif isinstance(new_value, list):
            field = new_value[0].keys()

        with open (self.file_path, 'a', newline='') as f_append :
            write = csv.DictWriter(f_append, fieldnames= field)
            # check just put header top of the file 
            if f_append.tell() == 0:
                write.writeheader()
            write.writerows(new_value)
