from tkinter import *
from HtmlDataExtraction import DataExtracT_Export
import Background_GUI_Tool

class BOM_Gui:
    def __init__(self):
        #----------------------tkinder GUI: BOM--------------------------------#
        self.BOM_frame = LabelFrame(Background_GUI_Tool.tab1,text= "BOM Report Generator",padx=83, pady=10,labelanchor='n')
        self.BOM_frame.grid(padx=30,pady=10,row=2,column=0)

        # create a label for the input field
        self.BOM_input_label = Label(self.BOM_frame, text="BOM FIle:")
        self.BOM_input_label.grid(row=0, column=0)

        # create an entry widget for the input field
        self.BOM_input_entry = Entry(self.BOM_frame,width=70,background='white',fg="black",borderwidth=3)
        self.BOM_input_entry.grid(row=0, column=1,columnspan=6)

        self.BOM_Extractlable = Label(self.BOM_frame,text="Extract:").grid(row=2,column=0)

        # Create a list of tuples that contains the text and values of the check buttons
        self.BOM_check_options = [("SYM Name", "BOM_option1"), 
                            ("COMP_DEVICE_TYPE", "BOM_option2"),
                            ("COMP_VALUE", "BOM_option3"),
                            ("COMP_TOL", "BOM_option4"),
                            ("COMP_CLASS", "BOM_option5"),
                            ("REFDES", "BOM_option6")]

        # Create a list of IntVar variables to store the selected check button values
        self.BOM_vars = []
        for self.option in self.BOM_check_options:
            self.var = StringVar()
            self.BOM_vars.append(self.var)

        # Use a for loop to create the check buttons
        for i, (text, value) in enumerate(self.BOM_check_options):
            BOM_check_button = Checkbutton(self.BOM_frame, text=text, variable=self.BOM_vars[i], onvalue=value, offvalue=0)
            BOM_check_button.grid(row=2, column=i+1,sticky="w")
            BOM_check_button.deselect()

            # Set to Default when first launch the GUI
            self.BOM_vars[0].set("BOM_option1")
            self.BOM_vars[1].set("BOM_option2")
            self.BOM_vars[2].set("BOM_option3")
            self.BOM_vars[3].set("BOM_option4")
            self.BOM_vars[4].set("BOM_option5")
            self.BOM_vars[5].set("BOM_option6")
    
        BOM_default_Button = Button(self.BOM_frame, text="Default",command=self.BomDefault)
        BOM_default_Button.grid(row=2,column=8)

    def BomDefault(self):
        self.BOM_vars[0].set("BOM_option1")
        self.BOM_vars[1].set("BOM_option2")
        self.BOM_vars[2].set("BOM_option3")
        self.BOM_vars[3].set("BOM_option4")
        self.BOM_vars[4].set("BOM_option5")
        self.BOM_vars[5].set("BOM_option6")

    def BomOutputData(self):
        #-------------------------BOM Output Data------------------------------#
        # Get NetPin input file paths
        self.BOM_input_file_path = self.BOM_input_entry.get()

        self.BOM_Extract_Obj = DataExtracT_Export.DataExtraction(self.BOM_input_file_path,col_select = self.BOM_vars)
        self.BOM_Extract_Obj.HTML_Data_Extract()

        BOM_dict = {}
        BOM_dict["BOM_option1"] = self.BOM_Extract_Obj.col_data_BOM_SymName,Background_GUI_Tool.sheet3,int(0)
        BOM_dict["BOM_option2"] = self.BOM_Extract_Obj.col_data_BOM_CompDeviceTyp,Background_GUI_Tool.sheet3,int(1)
        BOM_dict["BOM_option3"] = self.BOM_Extract_Obj.col_data_BOM_CompValue,Background_GUI_Tool.sheet3,int(2)
        BOM_dict["BOM_option4"] = self.BOM_Extract_Obj.col_data_BOM_CompTol,Background_GUI_Tool.sheet3,int(3)
        BOM_dict["BOM_option5"] = self.BOM_Extract_Obj.col_data_BOM_CompClass,Background_GUI_Tool.sheet3,int(4)
        BOM_dict["BOM_option6"] = self.BOM_Extract_Obj.col_data_BOM_REFDES,Background_GUI_Tool.sheet3,int(5)


        for key,value in BOM_dict.items():
            for i in self.BOM_vars:
                if key == i.get():
                    DataExtracT_Export.ExportTOexcel(value[0],value[1],column_num=value[2]).WriteTOexcel()