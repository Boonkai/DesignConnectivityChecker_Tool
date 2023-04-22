from Background_GUI_Tool import *
from tkinter import *
from HtmlDataExtraction import *


class mainGUI:
    def __init__(self):
        Background_GUI()
        self.main_Gui_root = Tk()
        self.main_Gui_root.title("Main screen")
        self.ReportFile_Frame = LabelFrame(self.main_Gui_root,text="Report Files Input",labelanchor="n")
        self.ReportFile_Frame.grid(row=0,column=1,columnspan=5)
        self.main_Gui_root.protocol("WM_DELETE_WINDOW",self.pressExit)

        #--------------------NetPin tkinder GUI------------------------------------#
        # create a label for the input field
        self.NetPin_main_input_label = Label(self.ReportFile_Frame, text="Component Pin File:")
        self.NetPin_main_input_label.grid(row=0, column=0)
    
        self.NetPin_main_input_entry = Entry(self.ReportFile_Frame ,width=70,background='white',fg="black",borderwidth=3)
        self.NetPin_main_input_entry.grid(row=0,column=1)

        self.NetPin_main_browser_button = Button(self.ReportFile_Frame , text="Browse",command=self.NetPin_main_browse_file)
        self.NetPin_main_browser_button.grid(row=0, column=2)

        #-------------------Hide, Show,Exit Button-------------------------------#
        self.presshow = Button(self.main_Gui_root, text="Close Development Tool",command=self.hidebackground)
        self.presshow.grid(row=1,column=1)

        self.presshow = Button(self.main_Gui_root, text="Open Development Tool",command=self.showBack)
        self.presshow.grid(row=1,column=2)

        self.pressexit = Button(self.main_Gui_root, text="Exit",command=self.pressExit)
        self.pressexit.grid(row=1,column=4)

        #-------------------Create the export button--------------------------#
        self.export_button = Button(self.main_Gui_root, text="Generate Report", command=export_report)
        self.export_button.grid(row=1,column=3)


    # create a function to open the file browser and select a file
    def NetPin_main_browse_file(self):
        # Component Pin Report File input:
        self.NetPin_main_file_path = filedialog.askopenfilename(initialdir="/Users/yeamboonkai/Desktop/AMD_Project/Input", 
                                            title="Select a File", 
                                            filetypes=(("htm", "*.htm"), ("All files", "*.*")))
        self.NetPin_main_input_entry.delete(0, END)
        self.NetPin_main_input_entry.insert(0, self.NetPin_main_file_path)

        # NetPin_Gui_obj.NetPin_file_path = self.NetPin_main_file_path
        NetPin_Gui_obj.NetPin_input_entry.delete(0,END)
        NetPin_Gui_obj.NetPin_input_entry.insert(0,self.NetPin_main_file_path)

        # Update NetPin directory path label
        NetPin_Gui_obj.NetPin_file_path_label.config(text=self.NetPin_main_file_path)

    def pressExit(self):
        BackGui_root.destroy()
        self.main_Gui_root.destroy()

    def showBack(self):
        BackGui_root.deiconify()

    def hidebackground(self):
        BackGui_root.withdraw()

    def run_mainGUI(self):
        self.main_Gui_root.mainloop()

MainGui_Obj = mainGUI()
MainGui_Obj.run_mainGUI()