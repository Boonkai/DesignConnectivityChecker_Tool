from tkinter import *
from tkinter import filedialog
from HtmlDataExtraction import DataExtracT_Export
import Background_GUI_Tool

class Netlist_Gui:
    def __init__(self):
        # self.BackGui_root = Background_GUI_Tool.BackGui_root
        # self.Netlist_root = self.BackGui_root

        self.Netlist_frame = LabelFrame(Background_GUI_Tool.tab1,text= "Netlist Report Generator",padx=88, pady=10,labelanchor='n')
        self.Netlist_frame.grid(padx=50,pady=10,row=1,column=0)

        # create a label for the input field
        self.Netlist_input_label = Label(self.Netlist_frame, text="NetList File:")
        self.Netlist_input_label.grid(row=0, column=0)

        # create an entry widget for the input field
        self.Netlist_input_entry = Entry(self.Netlist_frame,width=70,background='white',fg="black",borderwidth=3)
        self.Netlist_input_entry.grid(row=0, column=1,columnspan=6)

        # create a button to launch the file browser
        self.Netlist_file_path_label = Label(self.Netlist_frame, text="")
        self.Netlist_browser_button = Button(self.Netlist_frame, text="Browse", command=self.Netlist_browse_file)
        self.Netlist_browser_button.grid(row=0, column=8)

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


    def Netlist_browse_file(self):
        # Netlist Report File input:
        self.Netlist_file_path = filedialog.askopenfilename(initialdir="/Users/yeamboonkai/Desktop/AMD_Project/Input", 
                                            title="Select a File", 
                                            filetypes=(("htm", "*.htm"), ("All files", "*.*")))
        self.Netlist_input_entry.delete(0, END)
        self.Netlist_input_entry.insert(0, self.Netlist_file_path)

        # Update Netlist directory path label
        self.Netlist_file_path_label.config(text=self.Netlist_file_path)

    def NetlistOutputData(self):
        #-------------------------Netlist Output Data------------------------------#
        # Get Netlist input file paths
        self.Netlist_input_file_path = self.Netlist_file_path_label.cget("text")

        self.Netlist_Extract_Obj = DataExtracT_Export.DataExtraction(self.Netlist_input_file_path,col_select = self.Netlist_vars)
        self.Netlist_Extract_Obj.HTML_Data_Extract()

        Netlist_dict = {}
        Netlist_dict["Netlist_option1"] = self.Netlist_Extract_Obj.col_data_Netlist_NetName,Background_GUI_Tool.sheet2,int(0)
        Netlist_dict["Netlist_option2"] = self.Netlist_Extract_Obj.col_data_Netlist_NetPins_1st_data,Background_GUI_Tool.sheet2,int(1)
        Netlist_dict["Netlist_option2_2nd_data"] = self.Netlist_Extract_Obj.col_data_Netlist_NetPins_2nd_data,Background_GUI_Tool.sheet2,int(2) 


        for key,value in Netlist_dict.items():
            for i in self.Netlist_vars:
                if key == i.get():
                    DataExtracT_Export.ExportTOexcel(value[0],value[1],column_num=value[2]).WriteTOexcel()

        for key,value in Netlist_dict.items():
            for i in self.Netlist_vars:
                if key == i.get():
                    DataExtracT_Export.ExportTOexcel(value[0],value[1],column_num=value[2]).WriteTOexcel()
                if key == "Netlist_option2_2nd_data":
                    DataExtracT_Export.ExportTOexcel(value[0],value[1],column_num=value[2]).WriteTOexcel()