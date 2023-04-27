import Background_GUI_Tool
from tkinter import *
from RefDesignator.RefDesig_DataConcat import RefDesig_Concat

class RefDesignator_Gui:
    def __init__(self):
        #-------------------tkinder GUI: Reference Designator-------------------------#
        # Create a Canvas widget to hold the frame and scrollbar
        self.canvas = Canvas(Background_GUI_Tool.tab3)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # Create a frame to hold the label and button
        self.frame = Frame(self.canvas)
        self.frame.grid(row=0, column=0, sticky="nsew")


        self.RefDesignator = LabelFrame(self.frame, text="Reference Designator",labelanchor='n')
        self.RefDesignator.grid(padx=80,pady=10,row=0,column=0,columnspan=3)

        self.SourceFile_Frame = LabelFrame(self.RefDesignator, text="Interface Memory Source File",labelanchor='n')
        self.SourceFile_Frame.grid(padx=10,pady=10,row=0,column=0,columnspan=3)

        self.REFDES_Frame_List = []

        self.CPU0_Frame = LabelFrame(self.RefDesignator, text="CPU0",labelanchor='n')
        self.CPU0_Frame.grid(padx=10,pady=10,row=1,column=0,sticky="w")
        self.REFDES_Frame_List.append(self.CPU0_Frame)

        self.CPU1_Frame = LabelFrame(self.RefDesignator, text="CPU1",labelanchor='n')
        self.CPU1_Frame.grid(padx=10,pady=10,row=1,column=2,sticky="e")
        self.REFDES_Frame_List.append(self.CPU1_Frame)

        self.USB_HUB_Frame = LabelFrame(self.RefDesignator, text="USB HUB",labelanchor='n')
        self.USB_HUB_Frame.grid(padx=10,pady=10,row=2,column=0,sticky="w")
        self.REFDES_Frame_List.append(self.USB_HUB_Frame)

        self.Clk_Buff_Frame = LabelFrame(self.RefDesignator, text="Clock Buffer",labelanchor='n')
        self.Clk_Buff_Frame.grid(padx=10,pady=10,row=2,column=2,sticky="e")
        self.REFDES_Frame_List.append(self.Clk_Buff_Frame)

        Label(self.SourceFile_Frame,text='Interface Source File:').grid(row=0,column=0)
        Label(self.SourceFile_Frame,text='Sheet Tab:').grid(row=1,column=0)

        # create an entry widget for the input field
        self.SourceFile_input_entry = Entry(self.SourceFile_Frame,width=70,background='white',fg="black",borderwidth=3)
        self.SourceFile_input_entry.grid(row=0, column=1,columnspan=9)

        # Create a list of tuples that contains the text and values of the check buttons
        self.SourceFile_check_options = [("DDR_14L", "SourceFile_option1"), 
                        ("DDR_16L", "SourceFile_option2"),
                        ("DDR_18L", "SourceFile_option3"),
                        ("XGMI_PCIe", "SourceFile_option4"),
                        ("PCIE", "SourceFile_option5"),
                        ("MISC_SCL", "SourceFile_option6"),
                        ("MISC_LCL", "SourceFile_option7"),
                        ("USB", "SourceFile_option8"),
                        ("CLK", "SourceFile_option9")]

        # Create a list of IntVar variables to store the selected check button values
        self.SourceFile_vars = []
        for self.option in self.SourceFile_check_options:
            var = StringVar()
            self.SourceFile_vars.append(var)

        # Use a for loop to create the check buttons
        for i, (text, value) in enumerate(self.SourceFile_check_options):
            self.SourceFile_check_button = Checkbutton(self.SourceFile_Frame , text=text, variable=self.SourceFile_vars[i], onvalue=value, offvalue=0)
            self.SourceFile_check_button.grid(row=1, column=i+1,sticky="w")
            self.SourceFile_check_button.deselect()

        self.SourceFile_browser_button = Button(self.SourceFile_Frame, text="Browse")
        self.SourceFile_browser_button.grid(row=0, column=10)

        self.CUP_Ref_defult_button_widgets = []
        self.CPU_Ref_input_entry_widgets = []
        self.CPU_Ref_header_entry_widgets = []
        self.symbol_ref_drop_list = []
        self.Ref_design_check_button_list = []
        self.Ref_design_check_button_widgets = []
        self.CPU_col_insert_entry_list = []
        self.CPU_col_insert_entry_widgets = []
        self.CPU_col_lookup_entry_list = []
        self.CPU_col_lookup_entry_widgets = []
        self.CPU_col_StartRow_entry_list = []
        self.CPU_col_StartRow_entry_widgets = []

        for num,Ref_frame in enumerate(self.REFDES_Frame_List):
            Label(Ref_frame,text='CPU0 Ref:').grid(row=0,column=0,sticky="w")
            Label(Ref_frame,text='Symbol').grid(row=1,column=0,sticky="w")
            Label(Ref_frame,text='Header').grid(row=2,column=0,sticky="w")
            Label(Ref_frame,text='Set To Default').grid(row=4,column=0,sticky="w")

            self.CUP_Ref_defult_button = Button(Ref_frame,text="Default",command=lambda Button_select=num: self.test123(Button_select))

            self.CUP_Ref_defult_button.grid(row=4,column=1)
            self.CUP_Ref_defult_button_widgets.append(self.CUP_Ref_defult_button)

            self.CPU_Ref_input_entry = Entry(Ref_frame,width=5,background='white',fg="black",borderwidth=3)
            self.CPU_Ref_input_entry.grid(row=0, column=1)
            self.CPU_Ref_input_entry_widgets.append(self.CPU_Ref_input_entry)

            self.CPU_Ref_header_entry = Entry(Ref_frame,width=5,background='white',fg="black",borderwidth=3)
            self.CPU_Ref_header_entry.grid(row=2, column=1)
            self.CPU_Ref_header_entry_widgets.append(self.CPU_Ref_header_entry)

            self.symbol_ref_options = [ ".", 
                    "|"]
                
            #Drop Down Boxes
            self.Symbol_ref_clicked = StringVar()
            self.Symbol_ref_clicked.set(self.symbol_ref_options[0])
            self.symbol_ref_drop_list.append(self.Symbol_ref_clicked)

            self.symbol_drop = OptionMenu(Ref_frame ,self.Symbol_ref_clicked,*self.symbol_ref_options)
            self.symbol_drop.grid(row=1,column=1)

            for i in range(0,9):
                empty_col = Label(Ref_frame)
                empty_col.grid(row=i,column=3,sticky='w',padx=10,pady=5)

            self.Sheet_Name_Label = Label(Ref_frame ,text="Sheet Name")
            self.Sheet_Name_Label.grid(row=0,column=4,sticky='w',padx=5,pady=5)

            self.Sheet_lookup_col_label = Label(Ref_frame ,text="Column Lookup",wraplength=50)
            self.Sheet_lookup_col_label.grid(row=0,column=5,sticky='w',padx=5,pady=5)

            self.Sheet_StartRow_col_label = Label(Ref_frame ,text="Start Row\nInsert")
            self.Sheet_StartRow_col_label.grid(row=0,column=6,sticky='w',padx=5,pady=5)

            self.Sheet_col_insert_Label = Label(Ref_frame ,text="Column Insert",wraplength=50)
            self.Sheet_col_insert_Label.grid(row=0,column=7,sticky='w',padx=5,pady=5)

            # Create a list of tuples that contains the text and values of the check buttons
            self.Ref_design_check_options = [("DDR_14L", "DDR_14L"), 
                            ("DDR_16L", "DDR_16L"),
                            ("DDR_18L", "DDR_18L"),
                            ("XGMI_PCIe", "XGMI_PCIe"),
                            ("PCIE", "PCIE"),
                            ("MISC_SCL", "MISC_SCL"),
                            ("MISC_LCL", "MISC_LCL"),
                            ("USB", "USB"),
                            ("CLK", "CLK")]

            # Create a list of IntVar variables to store the selected check button values
            self.Ref_design_vars = []
            for self.option in self.Ref_design_check_options:
                var = StringVar()
                self.Ref_design_vars.append(var)

            # Use a for loop to create the check buttons
            for i, (text, value) in enumerate(self.Ref_design_check_options):
                self.Ref_design_check_button = Checkbutton(Ref_frame , text=text, variable=self.Ref_design_vars[i], onvalue=value, offvalue=0)
                self.Ref_design_check_button.grid(row=i+1, column=4,sticky="w")
                self.Ref_design_check_button.deselect()
                self.Ref_design_check_button_list.append(self.Ref_design_vars[i])

            self.Ref_design_check_button_widgets.append(self.Ref_design_check_button_list)

            for i in range(0,9):
                self.CPU_col_lookup_entry = Entry(Ref_frame,width=4,background='white',fg="black",borderwidth=3)
                self.CPU_col_lookup_entry.grid(row=i+1, column=5)
                self.CPU_col_lookup_entry_list.append(self.CPU_col_lookup_entry)

                self.CPU_col_StartRow_entry = Entry(Ref_frame,width=4,background='white',fg="black",borderwidth=3)
                self.CPU_col_StartRow_entry.grid(row=i+1, column=6)
                self.CPU_col_StartRow_entry_list.append(self.CPU_col_StartRow_entry)

                self.CPU_col_insert_entry = Entry(Ref_frame,width=4,background='white',fg="black",borderwidth=3)
                self.CPU_col_insert_entry.grid(row=i+1, column=7)
                self.CPU_col_insert_entry_list.append(self.CPU_col_insert_entry)

            self.CPU_col_lookup_entry_widgets.append(self.CPU_col_lookup_entry_list)
            self.CPU_col_StartRow_entry_widgets.append(self.CPU_col_StartRow_entry_list)
            self.CPU_col_insert_entry_widgets.append(self.CPU_col_insert_entry_list)
            
            # print(CPU_col_insert_entry_widgets)
            #clear/empty the list to avoid existing value continue append into CPU_col_insert_entry_widgets
            self.CPU_col_lookup_entry_list = []
            self.CPU_col_StartRow_entry_list = []
            self.CPU_col_insert_entry_list = []
            self.Ref_design_check_button_list = []

        #------------------Layer Stackup------------------------#
        self.Layer_Stackup_Frame = LabelFrame(self.frame ,text="Layer_Stackup",labelanchor='n')
        self.Layer_Stackup_Frame.grid(padx=10,pady=10,row=1,column=0,sticky="w")

        self.fourteen_layer_Frame = LabelFrame(self.Layer_Stackup_Frame ,text="14 Layer_Stackup",labelanchor='n')
        self.fourteen_layer_Frame.grid(padx=10,pady=10,row=0,column=0)

        self.sixteen_layer_Frame = LabelFrame(self.Layer_Stackup_Frame ,text="16 Layer_Stackup",labelanchor='n')
        self.sixteen_layer_Frame.grid(padx=10,pady=10,row=0,column=1)

        self.eighteen_layer_Frame = LabelFrame(self.Layer_Stackup_Frame ,text="18 Layer_Stackup",labelanchor='n')
        self.eighteen_layer_Frame.grid(padx=10,pady=10,row=0,column=2)

        for fourtheen_layer in range(1,15):
            Label(self.fourteen_layer_Frame,text="Layer "+ str(fourtheen_layer)).grid(row=fourtheen_layer,column=0)

            self.fourteen_layer_entry = Entry(self.fourteen_layer_Frame,width=5,background='white',fg="black",borderwidth=3)
            self.fourteen_layer_entry.grid(row=fourtheen_layer,column=1)
        for sixteen_layer in range(1,17):
            Label(self.sixteen_layer_Frame,text="Layer "+ str(sixteen_layer )).grid(row=sixteen_layer,column=0)

            self.sixteen_layer_entry = Entry(self.sixteen_layer_Frame,width=5,background='white',fg="black",borderwidth=3)
            self.sixteen_layer_entry.grid(row=sixteen_layer ,column=1)

        for eighteen_layer in range(1,19):
            Label(self.eighteen_layer_Frame,text="Layer "+ str(eighteen_layer )).grid(row=eighteen_layer,column=0)

            self.eighteen_layer_entry = Entry(self.eighteen_layer_Frame,width=5,background='white',fg="black",borderwidth=3)
            self.eighteen_layer_entry.grid(row=eighteen_layer ,column=1)

        # Attach a scrollbar to the canvas
        self.scrollbar = Scrollbar(Background_GUI_Tool.tab3, orient="vertical", command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Configure the canvas and frame to resize with the root window
        Background_GUI_Tool.tab3.grid_rowconfigure(0, weight=1)
        Background_GUI_Tool.tab3.grid_columnconfigure(0, weight=1)

        # Add the frame to the canvas
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        # Set the scrollable region of the canvas
        self.frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    # def RefDesign_Execute(self,Button_slect):

    def test123(self,Button_select):
        if Button_select == 0:
            for i in range(0,4):
                if self.CPU_Ref_input_entry_widgets[i].get() and self.CPU_Ref_header_entry_widgets[i].get():
                    for j in range(0,9):
                        # print((self.Ref_design_check_button_widgets[3][j]).get())
                        if (self.Ref_design_check_button_widgets[i][j].get() and 
                            self.CPU_col_insert_entry_widgets[i][j].get() and
                            self.CPU_col_lookup_entry_widgets[i][j].get() and
                            self.CPU_col_StartRow_entry_widgets[i][j].get()):
                                RefDesig_Concat(Ref_value=self.CPU_Ref_input_entry_widgets[i].get(),
                                                concat_symbol=self.symbol_ref_drop_list[i].get(),
                                                Insert_sheet_name=self.Ref_design_check_button_widgets[i][j].get(),
                                                col_insert=self.CPU_col_insert_entry_widgets[i][j].get(),
                                                col_lookup=self.CPU_col_lookup_entry_widgets[i][j].get(),
                                                col_insert_start_row=self.CPU_col_StartRow_entry_widgets[i][j].get(),
                                                header=self.CPU_Ref_header_entry_widgets[i].get()).data_concat()
                        else:
                            continue
                else:
                    continue

            # RefDesig_Concat(Ref_value=self.CPU_Ref_input_entry_widgets[1].get(),
            #                 concat_symbol=self.symbol_ref_drop_list[1].get(),
            #                 Insert_sheet_name=self.Ref_design_check_button_widgets[1][1].get(),
            #                 col_insert=self.CPU_col_insert_entry_widgets[1][1].get(),
            #                 col_lookup=self.CPU_col_lookup_entry_widgets[1][1].get(),
            #                 col_insert_start_row=self.CPU_col_StartRow_entry_widgets[1][1].get(),
            #                 header=self.CPU_Ref_header_entry_widgets[1].get()).data_concat()
        # if Button_select ==0:
        #     print(self.Ref_design_check_button_widgets[0][0].get())
        #     print(self.Ref_design_check_button_widgets[0][3].get())
        #     print(self.Ref_design_check_button_widgets[0][8].get())
        #     print(self.Ref_design_check_button_widgets[1][1].get())
        #     print(self.Ref_design_check_button_widgets[2][2].get())
        #     print(self.Ref_design_check_button_widgets[3][3].get())
        #     print(self.CPU_Ref_input_entry_widgets[0].get())
        #     print(self.CPU_col_insert_entry_widgets[0][0].get()) 
        #     print(self.CPU_col_insert_entry_widgets[1][0].get()) 
        #     print(self.CPU_col_insert_entry_widgets[3][8].get())      
        #     print(self.CPU_Ref_header_entry_widgets[0].get())
        #     print(self.symbol_ref_drop_list[0].get())
        #     print(self.Ref_design_check_button_widgets[0][0].get())
        #     print(self.CPU_col_insert_entry_widgets[0][0].get())
        #     print(self.CPU_col_insert_entry_widgets[1][0].get())
        #     print(self.CPU_col_lookup_entry_widgets[0][0].get())
        #     print(self.CPU_col_lookup_entry_widgets[2][6].get())
        #     print(self.CPU_col_StartRow_entry_widgets[0][0].get())
        #     print(self.CPU_col_StartRow_entry_widgets[2][6].get())
        # if Button_select== 1:
        #     print(self.CPU_Ref_input_entry_widgets[1].get())
        # if Button_select == 2:
        #     print(self.CPU_Ref_input_entry_widgets[2].get())

# if __name__ =='__main__':
#     test()