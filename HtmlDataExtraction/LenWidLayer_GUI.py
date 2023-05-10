from tkinter import *
from HtmlDataExtraction import DataExtracT_Export
import Background_GUI_Tool

class LenWidLaper_Gui:
    def __init__(self,rootframe,sheet):
        self.rootframe = rootframe
        self.sheet = sheet
        #----------------------tkinder GUI: Length Width Layer--------------------------------#
        self.LenWidLayer_frame = LabelFrame(self.rootframe,text= "Length Width Layer Report Generator",padx=50, pady=10,labelanchor='n')
        self.LenWidLayer_frame.grid(padx=20,pady=10,row=3,column=0)

        # create a label for the input field
        self.LenWidLayer_input_label = Label(self.LenWidLayer_frame, text="Length Width Layer File:")
        self.LenWidLayer_input_label.grid(row=0, column=0)

        # create an entry widget for the input field
        self.LenWidLayer_input_entry = Entry(self.LenWidLayer_frame,width=70,background='white',fg="black",borderwidth=3)
        self.LenWidLayer_input_entry.grid(row=0, column=1,columnspan=6)

        self.LenWidLayer_Extractlable = Label(self.LenWidLayer_frame,text="Extract:").grid(row=2,column=0)

        # Create a list of tuples that contains the text and values of the check buttons
        self.LenWidLayer_check_options = [("Net Name", "LenWidLayer_option1"), 
                            ("Layer", "LenWidLayer_option2"),
                            ("Total Length", "LenWidLayer_option3"),
                            ("Line Width", "LenWidLayer_option4"),
                            ("Length at Width", "LenWidLayer_option5")]

        # Create a list of IntVar variables to store the selected check button values
        self.LenWidLayer_vars = []
        for self.option in self.LenWidLayer_check_options:
            self.var = StringVar()
            self.LenWidLayer_vars.append(self.var)

        # Use a for loop to create the check buttons
        for i, (text, value) in enumerate(self.LenWidLayer_check_options):
            self.LenWidLayer_check_button = Checkbutton(self.LenWidLayer_frame, text=text, variable=self.LenWidLayer_vars[i], onvalue=value, offvalue=0)
            self.LenWidLayer_check_button.grid(row=2, column=i+1,sticky="w")
            self.LenWidLayer_check_button.deselect()

            # Set to Default when first launch the GUI
            self.LenWidLayer_vars[0].set("LenWidLayer_option1")
            self.LenWidLayer_vars[1].set("LenWidLayer_option2")
            self.LenWidLayer_vars[2].set("LenWidLayer_option3")
            self.LenWidLayer_vars[3].set("LenWidLayer_option4")
            self.LenWidLayer_vars[4].set("LenWidLayer_option5")

        self.LenWidLayer_default_Button = Button(self.LenWidLayer_frame, text="Default",command=self.LenWidLayer)
        self.LenWidLayer_default_Button.grid(row=2,column=8)

    def LenWidLayer(self):
        self.LenWidLayer_vars[0].set("LenWidLayer_option1")
        self.LenWidLayer_vars[1].set("LenWidLayer_option2")
        self.LenWidLayer_vars[2].set("LenWidLayer_option3")
        self.LenWidLayer_vars[3].set("LenWidLayer_option4")
        self.LenWidLayer_vars[4].set("LenWidLayer_option5")

    def LenWidLayerOutputData(self):
        #--------------------------LenWidLayer Output Data--------------------------------#
        # Get LenWidLayer input file paths
        self.LenWidLayer_input_file_path = self.LenWidLayer_input_entry.get()

        self.LenWidLayer_Extract_Obj =DataExtracT_Export.DataExtraction(self.LenWidLayer_input_file_path,col_select = self.LenWidLayer_vars)
        self.LenWidLayer_Extract_Obj.HTML_Data_Extract()

        LenWidLayer_dict = {}
        LenWidLayer_dict["LenWidLayer_option1"] = self.LenWidLayer_Extract_Obj.col_data_TraceLenWid_NetName,self.sheet,int(0)
        LenWidLayer_dict["LenWidLayer_option2"] = self.LenWidLayer_Extract_Obj.col_data_TraceLenWid_LayerName,self.sheet,int(4)
        LenWidLayer_dict["LenWidLayer_option3"] = self.LenWidLayer_Extract_Obj.col_data_TraceLenWid_TotalLength,self.sheet,int(5)
        LenWidLayer_dict["LenWidLayer_option4"] = self.LenWidLayer_Extract_Obj.col_data_TraceLenWid_LineWidth,self.sheet,int(1)
        LenWidLayer_dict["LenWidLayer_option5"] = self.LenWidLayer_Extract_Obj.col_data_TraceLenWid_LenATwidth,self.sheet,int(6)


        for key,value in LenWidLayer_dict.items():
            for i in self.LenWidLayer_vars:
                if key == i.get():
                    DataExtracT_Export.ExportTOexcel(value[0],value[1],column_num=value[2]).WriteTOexcel()

    


        