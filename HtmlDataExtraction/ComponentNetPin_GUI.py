# import sys
# # sys.path.append('../DesignConctChecker')
# # from DesignConctChecker.Background_Tool_GUI import *
# # from DataExtracT_Export import *
# from tkinter import *
# from tkinter import ttk
# import os
# from pathlib import Path
# test_path = Path(__file__).parent.absolute
# CurrentDir = os.path.dirname(os.path.realpath(__file__))
# path = Path(CurrentDir)
# ParentDir = path.parent

from tkinter import *
from HtmlDataExtraction import DataExtracT_Export
import Background_GUI_Tool

class NetPin_Gui:
    def __init__(self):
        #----------------------tkinder GUI: NET PIN--------------------------------#
        self.NetPin_frame = LabelFrame(Background_GUI_Tool.tab1,text= "Net Pin Report Generator ",padx=65, pady=10,labelanchor='n')
        self.NetPin_frame.grid(padx=50,pady=10,row=0,column=0)

        # create a label for the input field
        self.NetPin_input_label = Label(self.NetPin_frame, text="Component Pin File:")
        self.NetPin_input_label.grid(row=0, column=0)

        # create an entry widget for the input field
        self.NetPin_input_entry = Entry(self.NetPin_frame,width=70,background='white',fg="black",borderwidth=3)
        self.NetPin_input_entry.grid(row=0, column=1,columnspan=6)

        Label(self.NetPin_frame,text="Extract:").grid(row=1,column=0)

        # Create a list of tuples that contains the text and values of the check buttons
        self.NetPin_check_options = [("REFDES", "NetPin_option1"), 
                        ("PIN_NUMBER", "NetPin_option2"), 
                        ("COMP_DEVICE_TYPE", "NetPin_option3"),
                        ("PIN_TYPE", "NetPin_option4"),
                        ("PIN_NAME","NetPin_option5"),
                        ("NET_NAME","NetPin_option6")
                        ]

        # Create a list of IntVar variables to store the selected check button values
        self.NetPin_vars = []
        for self.option in self.NetPin_check_options:
            self.var = StringVar()
            self.NetPin_vars.append(self.var)
        # Use a for loop to create the check buttons
        for i, (text, value) in enumerate(self.NetPin_check_options):
            self.NetPin_check_button = Checkbutton(self.NetPin_frame, text=text, variable=self.NetPin_vars[i], onvalue=value, offvalue=0)
            # NetPin_check_button.grid(row=i+1, column=3,sticky="w")
            self.NetPin_check_button.grid(row=1, column=i+1,sticky="w")
            self.NetPin_check_button.deselect()

            # Set to Default when first launch the GUI
            self.NetPin_vars[0].set("NetPin_option1")
            self.NetPin_vars[1].set("NetPin_option2")
            self.NetPin_vars[5].set("NetPin_option6")
            
        self.NetPin_default_Button = Button(self.NetPin_frame, text="Default",command=self.NetPinDefault)
        self.NetPin_default_Button.grid(row=1,column=8)


    def NetPinDefault(self):

        self.NetPin_vars[0].set("NetPin_option1")
        self.NetPin_vars[1].set("NetPin_option2")
        self.NetPin_vars[2].set(0)
        self.NetPin_vars[3].set(0)
        self.NetPin_vars[4].set(0)
        self.NetPin_vars[5].set("NetPin_option6")


    def NetPinOutputData(self):
        #--------------------------NetPin Output Data--------------------------------#
        # Get NetPin input file paths
        NetPin_input_file_path = self.NetPin_input_entry.get()

        Netpin_Extract_Obj = DataExtracT_Export.DataExtraction(NetPin_input_file_path,col_select = self.NetPin_vars)
        Netpin_Extract_Obj.HTML_Data_Extract()

        NetPin_dict = {}
        NetPin_dict["NetPin_option1"] = Netpin_Extract_Obj.col_data_ComponentPin_REFDES,Background_GUI_Tool.sheet1,int(0)
        NetPin_dict["NetPin_option2"] = Netpin_Extract_Obj.col_data_ComponentPin_PinNumber,Background_GUI_Tool.sheet1,int(1)
        NetPin_dict["NetPin_option3"] = Netpin_Extract_Obj.col_data_ComponentPin_CompDeviceTyp,Background_GUI_Tool.sheet1,int(4)
        NetPin_dict["NetPin_option4"] = Netpin_Extract_Obj.col_data_ComponentPin_PinTyp,Background_GUI_Tool.sheet1,int(5)
        NetPin_dict["NetPin_option5"] = Netpin_Extract_Obj.col_data_ComponentPin_PinName,Background_GUI_Tool.sheet1,int(6)
        NetPin_dict["NetPin_option6"] = Netpin_Extract_Obj.col_data_ComponentPin_NetName,Background_GUI_Tool.sheet1,int(3)


        for key,value in NetPin_dict.items():
            for i in self.NetPin_vars:
                if key == i.get():
                    DataExtracT_Export.ExportTOexcel(value[0],value[1],column_num=value[2]).WriteTOexcel()