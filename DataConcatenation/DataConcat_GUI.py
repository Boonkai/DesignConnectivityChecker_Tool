from tkinter import *
from DataConcatenation.DataConcatenation import DataConcatenation
import Background_GUI_Tool

class DataConcat_Gui:
    def __init__(self):
        #-------------------Data Concat--------------------------------------#
        self.DataConcat_frame = LabelFrame(Background_GUI_Tool.tab2,text= "Concatenation",padx=10, pady=10,labelanchor='n')
        self.DataConcat_frame.grid(padx=30,pady=10,row=0,column=0,columnspan=3,rowspan=2)

        self.concat_label = [("label1","Sheet 1"),
                        ("labe2","column"),
                        ("labe3"," "),
                        ("labe4","Simbol"),
                        ("labe5"," "),
                        ("labe6","Sheet 2"),
                        ("labe7","Column"),
                        ("labe8"," "),
                        ("labe9","Colum Insert"),
                        ("labe10","Col Insert Sheet"),
                        ("labe11","Header")]

        for i ,(self.key,self.value) in enumerate(self.concat_label):
            self.label = Label(self.DataConcat_frame, text=self.value)
            self.label.grid(row=0,column=i)

        self.col1_entry_widgets =[]
        self.col2_entry_widgets =[]
        self.col_insert_entry_widgets = []
        self.header_entry_widgets =[]
        self.simbol_drop_list = []
        self.Sheet1_drop_list = []
        self.Sheet2_drop_list = []
        self.col_insert_drop_list = []

        for j in range(1,11):
            self.Sheet1_options = [ "Pin_Net", 
                    "Netlist",
                    "BOM",
                    "NetWidth",
                    "DDR_14L",
                    "DDR_16L"]

            #Drop Down Boxes
            self.Sheet1_clicked = StringVar()
            self.Sheet1_clicked.set(self.Sheet1_options[0])
            self.Sheet1_drop_list.append(self.Sheet1_clicked)

            self.Sheet1_drop = OptionMenu(self.DataConcat_frame,self.Sheet1_clicked,*self.Sheet1_options)
            self.Sheet1_drop.grid(row=j,column=0)

            # create an entry widget for the input field
            self.Sheet1_col_input_entry = Entry(self.DataConcat_frame,width=5,background='white',fg="black",borderwidth=3)
            self.Sheet1_col_input_entry.grid(row=j, column=1)
            self.col1_entry_widgets.append(self.Sheet1_col_input_entry)

            self.DataConcat_plus1_label = Label(self.DataConcat_frame, text="+",font= ('TkDefaultFont', 25))
            self.DataConcat_plus1_label.grid(row=j,column=2)

            self.simbol_options = [ ".", 
                    "|"]
                
            #Drop Down Boxes
            self.Simbol_clicked = StringVar()
            self.Simbol_clicked.set(self.simbol_options[0])
            self.simbol_drop_list.append(self.Simbol_clicked)

            self.simbol_drop = OptionMenu(self.DataConcat_frame,self.Simbol_clicked,*self.simbol_options)
            self.simbol_drop.grid(row=j,column=3)

            self.DataConcat_plus2_label = Label(self.DataConcat_frame, text="+",font= ('TkDefaultFont', 25))
            self.DataConcat_plus2_label.grid(row=j,column=4)

            self.Sheet2_options = [ "Pin_Net", 
                    "Netlist",
                    "BOM",
                    "NetWidth",
                    "DDR_14L",
                    "DDR_16L"]
                
            #Drop Down Boxes
            self.Sheet2_clicked = StringVar()
            self.Sheet2_clicked.set(self.Sheet2_options[0])
            self.Sheet2_drop_list.append(self.Sheet2_clicked)

            self.Sheet2_drop = OptionMenu(self.DataConcat_frame,self.Sheet2_clicked,*self.Sheet2_options)
            self.Sheet2_drop.grid(row=j,column=5)

            # create an entry widget for the input field
            self.Sheet2_col_input_entry = Entry(self.DataConcat_frame,width=5,background='white',fg="black",borderwidth=3)
            self.Sheet2_col_input_entry.grid(row=j, column=6)
            self.col2_entry_widgets.append(self.Sheet2_col_input_entry)

            self.DataConcat_plus1_label = Label(self.DataConcat_frame, text="=",font= ('TkDefaultFont', 25))
            self.DataConcat_plus1_label.grid(row=j,column=7)

            # create an entry widget for the input field
            self.col_insert_entry = Entry(self.DataConcat_frame,width=5,background='white',fg="black",borderwidth=3)
            self.col_insert_entry.grid(row=j, column=8)
            self.col_insert_entry_widgets.append(self.col_insert_entry)

            self.col_insert_options = [ "Pin_Net", 
                    "Netlist",
                    "BOM",
                    "NetWidth",
                    "DDR_14L",
                    "DDR_16L"]
                
            #Drop Down Boxes
            self.col_insert_clicked = StringVar()
            self.col_insert_clicked.set(self.col_insert_options[0])
            self.col_insert_drop_list.append(self.col_insert_clicked)

            self.col_insert_drop = OptionMenu(self.DataConcat_frame,self.col_insert_clicked,*self.col_insert_options)
            self.col_insert_drop.grid(row=j,column=9)
            
            # create an entry widget for the input field
            self.header_entry = Entry(self.DataConcat_frame,width=10,background='white',fg="black",borderwidth=3)
            self.header_entry.grid(row=j, column=10,padx=10,pady=10)
            self.header_entry_widgets.append(self.header_entry)

        self.DataConcat_info_frame =LabelFrame(Background_GUI_Tool.tab2,text= "NOTE",padx=32, pady=10,labelanchor='n',width=10)
        self.DataConcat_info_frame.grid(row=1,column=4)

        self.DataConcat_list =["1. Column text input can be lower or upper case e.g: \"A\" or \"a\"\n",
            "2. Header input can be empty if no needed. Ensure that the input text has NO spacing.\n",
            "3. Default Button = Set all value to default acoording to the report standard output.\n",
            "4. Clear Button = Clear all input.\n"] 

        # create a label widget with the list text
        self.DataConcat_text = "\n".join(self.DataConcat_list)
        self.DataConcat_info_label = Label(self.DataConcat_info_frame,text=self.DataConcat_text,bd=1,justify='left',wraplength=300)
        self.DataConcat_info_label.grid()

        self.Test = Button(Background_GUI_Tool.tab2,text="test")
        self.Test.grid(row=12,column=0)

        self.Concat_default_Button = Button(Background_GUI_Tool.tab2, text="Default",command=self.dataConcat_default)
        self.Concat_default_Button.grid(row=12,column=1)

        self.Concat_clear_Button = Button(Background_GUI_Tool.tab2, text="Clear",command=self.dataConcat_clear)
        self.Concat_clear_Button.grid(row=12,column=2)

        # Automatic call Data Concat when first launch the GUI APPs
        self.dataConcat_default()

    def dataConcat_default(self):
        for i in range(0,10):
            self.Sheet1_drop_list[i].set(self.Sheet1_options[0])
            self.col1_entry_widgets[i].delete(0,END)
            self.simbol_drop_list[i].set(self.simbol_options[0])
            self.Sheet2_drop_list[i].set(self.Sheet2_options[0])
            self.col2_entry_widgets[i].delete(0,END)
            self.col_insert_entry_widgets[i].delete(0,END)
            self.col_insert_drop_list[i].set(self.col_insert_options[0])
            self.header_entry_widgets[i].delete(0,END)

        #Set Pin_Net data concate to dafault:
        self.Sheet1_drop_list[0].set(self.Sheet1_options[0])
        self.col1_entry_widgets[0].insert(0,"A")
        self.simbol_drop_list[0].set(self.simbol_options[0])
        self.Sheet2_drop_list[0].set(self.Sheet2_options[0])
        self.col2_entry_widgets[0].insert(0,"B")
        self.col_insert_entry_widgets[0].insert(0,"C")
        self.col_insert_drop_list[0].set(self.col_insert_options[0])

        #Set NetWidth Helper1 data concate to dafault:
        self.Sheet1_drop_list[1].set(self.Sheet1_options[3])
        self.col1_entry_widgets[1].insert(0,"A")
        self.simbol_drop_list[1].set(self.simbol_options[1])
        self.Sheet2_drop_list[1].set(self.Sheet2_options[3])
        self.col2_entry_widgets[1].insert(0,"B")
        self.col_insert_entry_widgets[1].insert(0,"C")
        self.col_insert_drop_list[1].set(self.col_insert_options[3])
        self.header_entry_widgets[1].insert(0,"Helper")

    #Set NetWidth Helper1 data concate to dafault:
        self.Sheet1_drop_list[2].set(self.Sheet1_options[3])
        self.col1_entry_widgets[2].insert(0,"C")
        self.simbol_drop_list[2].set(self.simbol_options[1])
        self.Sheet2_drop_list[2].set(self.Sheet2_options[3])
        self.col2_entry_widgets[2].insert(0,"E")
        self.col_insert_entry_widgets[2].insert(0,"D")
        self.col_insert_drop_list[2].set(self.col_insert_options[3])
        self.header_entry_widgets[2].insert(0,"Helper1")

    def dataConcat_clear(self):
        for i in range(0,10):
            self.Sheet1_drop_list[i].set(self.Sheet1_options[0])
            self.col1_entry_widgets[i].delete(0,END)
            self.simbol_drop_list[i].set(self.simbol_options[0])
            self.Sheet2_drop_list[i].set(self.Sheet2_options[0])
            self.col2_entry_widgets[i].delete(0,END)
            self.col_insert_entry_widgets[i].delete(0,END)
            self.col_insert_drop_list[i].set(self.col_insert_options[0])
            self.header_entry_widgets[i].delete(0,END)

    def DataConcat_Execute(self):
        for i in range(0,10):
            if self.col1_entry_widgets[i].get():
                if self.col2_entry_widgets[i].get():
                    if self.col_insert_entry_widgets[i].get():
                        DataConcatenation(col_1=str(self.col1_entry_widgets[i].get()),
                                        col_2=str(self.col2_entry_widgets[i].get()),
                                        sheet1_name=str(self.Sheet1_drop_list[i].get()),
                                        sheet2_name=str(self.Sheet2_drop_list[i].get()),
                                        col_insert=str(self.col_insert_entry_widgets[i].get()),
                                        concat_symbol=self.simbol_drop_list[i].get(),
                                        col_insert_sheet_name= self.col_insert_drop_list[i].get(),
                                        header=self.header_entry_widgets[i].get()).data_concat()
                    else:
                        continue
                else:
                    continue
            else:
                continue
