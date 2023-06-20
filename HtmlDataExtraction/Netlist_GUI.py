from tkinter import *
from HtmlDataExtraction import DataExtracT_Export

class Netlist_Gui:
    def __init__(self,rootframe,sheet):
        self.rootframe = rootframe
        self.sheet = sheet
        self.Netlist_frame = LabelFrame(self.rootframe,text= "Netlist Report Generator",padx=88, pady=10,labelanchor='n')
        self.Netlist_frame.grid(padx=50,pady=10,row=1,column=0)

        # create a label for the input field
        self.Netlist_input_label = Label(self.Netlist_frame, text="NetList File:")
        self.Netlist_input_label.grid(row=0, column=0)

        # create an entry widget for the input field
        self.Netlist_input_entry = Entry(self.Netlist_frame,width=70,background='white',fg="black",borderwidth=3)
        self.Netlist_input_entry.grid(row=0, column=1,columnspan=6)


        self.Netlist_Extractlable = Label(self.Netlist_frame,text="Extract:").grid(row=1,column=0)

        # Create a list of tuples that contains the text and values of the check buttons
        self.Netlist_check_options = [("Net Name", "Netlist_option1"), 
                                ("Net Pins", "Netlist_option2")]

        # Create a list of IntVar variables to store the selected check button values
        self.Netlist_vars = []
        for self.option in self.Netlist_check_options:
            var = StringVar()
            self.Netlist_vars.append(var)

        # Use a for loop to create the check buttons
        for i, (text, value) in enumerate(self.Netlist_check_options):
            self.Netlist_check_button = Checkbutton(self.Netlist_frame, text=text, variable=self.Netlist_vars[i], onvalue=value, offvalue=0)
            self.Netlist_check_button.grid(row=1, column=i+1,sticky="w")
            self.Netlist_check_button.deselect()

            # Set to Default when first launch the GUI
            self.Netlist_vars[0].set("Netlist_option1")
            self.Netlist_vars[1].set("Netlist_option2")

        self.Netlist_default_Button = Button(self.Netlist_frame, text="Default",command=self.NetlistDefault)
        self.Netlist_default_Button.grid(row=1,column=8)

    def NetlistDefault(self):
        self.Netlist_vars[0].set("Netlist_option1")
        self.Netlist_vars[1].set("Netlist_option2")

    def NetlistOutputData(self):
        #-------------------------Netlist Output Data------------------------------#
        # Get Netlist input file paths
        self.Netlist_input_file_path = self.Netlist_input_entry.get()

        self.Netlist_Extract_Obj = DataExtracT_Export.DataExtraction(self.Netlist_input_file_path,col_select = self.Netlist_vars)
        self.Netlist_Extract_Obj.HTML_Data_Extract()

        Netlist_dict = {}
        Netlist_dict["Netlist_option1"] = self.Netlist_Extract_Obj.col_data_Netlist_NetName,self.sheet,int(0)
        Netlist_dict["Netlist_option2_1st_data"] = self.Netlist_Extract_Obj.col_data_Netlist_NetPins_1st_data,self.sheet,int(1)
        Netlist_dict["Netlist_option2_2nd_data"] = self.Netlist_Extract_Obj.col_data_Netlist_NetPins_2nd_data,self.sheet,int(2)
        Netlist_dict["Netlist_option2_3rd_data"] = self.Netlist_Extract_Obj.col_data_Netlist_NetPins_3rd_data,self.sheet,int(3)
        Netlist_dict["Netlist_option2_4th_data"] = self.Netlist_Extract_Obj.col_data_Netlist_NetPins_4th_data,self.sheet,int(4)
        Netlist_dict["Netlist_option2_5th_data"] = self.Netlist_Extract_Obj.col_data_Netlist_NetPins_5th_data,self.sheet,int(5)
        Netlist_dict["Netlist_option2_6th_data"] = self.Netlist_Extract_Obj.col_data_Netlist_NetPins_6th_data,self.sheet,int(6)
        Netlist_dict["Netlist_option2_7th_data"] = self.Netlist_Extract_Obj.col_data_Netlist_NetPins_7th_data,self.sheet,int(7)  


        for key,value in Netlist_dict.items():
            for i in self.Netlist_vars:
                if key == i.get():
                    DataExtracT_Export.ExportTOexcel(value[0],value[1],column_num=value[2]).WriteTOexcel()

        for key,value in Netlist_dict.items():
            for i in self.Netlist_vars:
                if key == "Netlist_option2_1st_data":
                    DataExtracT_Export.ExportTOexcel(value[0],value[1],column_num=value[2]).WriteTOexcel()
                if key == "Netlist_option2_2nd_data":
                    DataExtracT_Export.ExportTOexcel(value[0],value[1],column_num=value[2]).WriteTOexcel()
                if key == "Netlist_option2_3rd_data":
                    DataExtracT_Export.ExportTOexcel(value[0],value[1],column_num=value[2]).WriteTOexcel()
                if key == "Netlist_option2_4th_data":
                    DataExtracT_Export.ExportTOexcel(value[0],value[1],column_num=value[2]).WriteTOexcel()
                if key == "Netlist_option2_5th_data":
                    DataExtracT_Export.ExportTOexcel(value[0],value[1],column_num=value[2]).WriteTOexcel()
                if key == "Netlist_option2_6th_data":
                    DataExtracT_Export.ExportTOexcel(value[0],value[1],column_num=value[2]).WriteTOexcel()
                if key == "Netlist_option2_7th_data":
                    DataExtracT_Export.ExportTOexcel(value[0],value[1],column_num=value[2]).WriteTOexcel()