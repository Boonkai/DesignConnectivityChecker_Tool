from tkinter import filedialog
from tkinter import *

#---------------------NetPin File Browser-----------------------------------
# create a function to open the file browser and select a file
class browser:
    def __init__(self) -> None:
        pass

    def browse_file(self):
        self.file_path =  filedialog.askopenfilename(initialdir="/Users/yeamboonkai/Desktop/AMD_Project/Input", 
                                            title="Select a File", 
                                            filetypes=(("htm", "*.htm"), ("All files", "*.*")))
        return self.file_path
