from Background_GUI_Tool import *
from tkinter import *


class mainGUI:
    def __init__(self):
        Background_GUI()
        self.main_Gui_root = Tk()
        self.main_Gui_root.title("Main screen")
        self.main_Gui_root.protocol("WM_DELETE_WINDOW",self.pressExit)

        self.main_entry = Entry(self.main_Gui_root,width=5,background='white',fg="black",borderwidth=3)
        self.main_entry.grid(row=0,column=0)

        presshow = Button(self.main_Gui_root, text="hide background",command=self.hidebackground)
        presshow.grid(row=1,column=0)

        presshow = Button(self.main_Gui_root, text="show background",command=self.showBack)
        presshow.grid(row=2,column=0)

        pressexit = Button(self.main_Gui_root, text="Exit",command=self.pressExit)
        pressexit.grid(row=3,column=0)

        #-------------------Create the export button--------------------------#
        export_button = Button(self.main_Gui_root, text="Generate Report", command=export_report)
        export_button.grid(row=4,column=0)

        

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