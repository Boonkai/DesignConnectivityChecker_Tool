from tkinter import *
from HtmlDataExtraction import DataExtracT_Export

class LyrStack_Gui:
    def __init__(self,rootframe,sheet):
        self.rootframe = rootframe
        self.sheet = sheet
        self.LyrStack_frame = LabelFrame(self.rootframe,text= "Layer Stack up Generator",padx=70, pady=10,labelanchor='n')
        self.LyrStack_frame.grid(padx=50,pady=10,row=4,column=0)

        # create a label for the input field
        self.LyrStack_input_label = Label(self.LyrStack_frame, text="Layer Stackup File:")
        self.LyrStack_input_label.grid(row=0, column=0)

        # create an entry widget for the input field
        self.LyrStack_input_entry = Entry(self.LyrStack_frame,width=70,background='white',fg="black",borderwidth=3)
        self.LyrStack_input_entry.grid(row=0, column=1,columnspan=6)


        self.LyrStack_Extractlable = Label(self.LyrStack_frame,text="Extract:").grid(row=1,column=0)

        # Create a list of tuples that contains the text and values of the check buttons
        self.LyrStack_check_options = [("Subclass Name", "LyrStack_option1"), 
                                    ("Type", "LyrStack_option2"),
                                    ("Material", "LyrStack_option3"),
                                    ("Thickness", "LyrStack_option4")]

        # Create a list of IntVar variables to store the selected check button values
        self.LyrStack_vars = []
        for self.option in self.LyrStack_check_options:
            var = StringVar()
            self.LyrStack_vars.append(var)

        # Use a for loop to create the check buttons
        for i, (text, value) in enumerate(self.LyrStack_check_options):
            self.LyrStack_check_button = Checkbutton(self.LyrStack_frame, text=text, variable=self.LyrStack_vars[i], onvalue=value, offvalue=0)
            self.LyrStack_check_button.grid(row=1, column=i+1,sticky="w")
            self.LyrStack_check_button.deselect()

            # Set to Default when first launch the GUI
            self.LyrStack_vars[0].set("LyrStack_option1")
            self.LyrStack_vars[1].set("LyrStack_option2")
            self.LyrStack_vars[2].set("LyrStack_option3")
            self.LyrStack_vars[3].set("LyrStack_option4")

        self.LyrStack_default_Button = Button(self.LyrStack_frame, text="Default",command=self.LyrStackDefault)
        self.LyrStack_default_Button.grid(row=1,column=8)

    def LyrStackDefault(self):
        self.LyrStack_vars[0].set("LyrStack_option1")
        self.LyrStack_vars[1].set("LyrStack_option2")
        self.LyrStack_vars[2].set("LyrStack_option3")
        self.LyrStack_vars[3].set("LyrStack_option4")

    def LyrStackupOutputData(self):
        #-------------------------Netlist Output Data------------------------------#
        # Get Netlist input file paths
        self.LyrStack_input_file_path = self.LyrStack_input_entry.get()

        self.LyrStack_Extract_Obj = DataExtracT_Export.DataExtraction(self.LyrStack_input_file_path,col_select = self.LyrStack_vars)
        self.LyrStack_Extract_Obj.HTML_Data_Extract()

        LyrStack_dict = {}
        LyrStack_dict["LyrStack_option1"] = self.LyrStack_Extract_Obj.col_layer_stackup_SubName,self.sheet,int(1)
        LyrStack_dict["LyrStack_option2"] = self.LyrStack_Extract_Obj.col_layer_stackup_Type,self.sheet,int(2)
        LyrStack_dict["LyrStack_option3"] = self.LyrStack_Extract_Obj.col_layer_stackup_Material,self.sheet,int(3)
        LyrStack_dict["LyrStack_option4"] = self.LyrStack_Extract_Obj.col_layer_stackup_Thickness,self.sheet,int(4)

        for key,value in LyrStack_dict.items():
            for i in self.LyrStack_vars:
                if key == i.get():
                    DataExtracT_Export.ExportTOexcel(value[0],value[1],column_num=value[2]).WriteTOexcel()

        # Export Layer name to column first column
        DataExtracT_Export.ExportTOexcel(self.LyrStack_Extract_Obj.col_layer_stackup_LayerName,self.sheet,column_num=0).WriteTOexcel()