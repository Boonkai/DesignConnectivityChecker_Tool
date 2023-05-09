from tkinter import *
from RefDesignator.RefDesign_DataConcat import RefDesig_Concat
from RefDesignator import SourceFile_browse
InterfaceMmy_Src_file = "/Users/yeamboonkai/Desktop/AMD_Project/Input_Files/DesignConnectivityChecker_Tool/RefDesignator/Interface.xlsx"


class RefDesignator_Gui:
    def __init__(self,rootframe, fileName):
        self.rootframe = rootframe
        self.fileName= fileName
        #-------------------tkinder GUI: Reference Designator-------------------------#
        # Create a Canvas widget to hold the frame and scrollbar
        self.canvas = Canvas(self.rootframe)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # Create a frame to hold the label and button
        self.frame = Frame(self.canvas)
        self.frame.grid(row=0, column=0, sticky="nsew")


        self.RefDesignator = LabelFrame(self.frame, text="Reference Designator",labelanchor='n')
        self.RefDesignator.grid(padx=80,pady=10,row=0,column=0,columnspan=5)

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

        #--------------------------Interface Memory Source File--------------------------------#
        self.SourceFile_Frame = LabelFrame(self.RefDesignator, text="Interface Memory Source File",labelanchor='n')
        self.SourceFile_Frame.grid(padx=10,pady=10,row=0,column=0,columnspan=3)

        Label(self.SourceFile_Frame,text='Interface Memory Source File:').grid(row=0,column=0)
        Label(self.SourceFile_Frame,text='Sheet Tab:').grid(row=1,column=0)

        # create an entry widget for the input field
        self.SourceFile_input_entry = Entry(self.SourceFile_Frame,width=70,background='white',fg="black",borderwidth=3)
        self.SourceFile_input_entry.grid(row=0, column=1,columnspan=9)

        self.SourceFile_input_entry.delete(0,END) 
        self.SourceFile_input_entry.insert(0,InterfaceMmy_Src_file)

        # Create a list of tuples that contains the text and values of the check buttons
        self.SourceFile_check_options = [("MEMORY", "MEMORY"),
                                        ("XGMI", "XGMI"),
                                        ("PCIE", "PCIE"),
                                        ("SATA", "SATA"),
                                        ("MISC", "MISC"),
                                        ("USB", "USB"),
                                        ("CLK", "CLK")]

        # Create a list of IntVar variables to store the selected check button values
        self.SourceFile_vars = []
        self.SrcFile_MemIntf_Chkbox_Btn = []
        for self.option in self.SourceFile_check_options:
            var = StringVar()
            self.SourceFile_vars.append(var)

        # Use a for loop to create the check buttons
        for i, (text, value) in enumerate(self.SourceFile_check_options):
            self.SourceFile_check_button = Checkbutton(self.SourceFile_Frame , text=text, variable=self.SourceFile_vars[i], onvalue=value, offvalue=0)
            self.SourceFile_check_button.grid(row=1, column=i+1,sticky="w")
            self.SourceFile_check_button.deselect()
            self.SrcFile_MemIntf_Chkbox_Btn.append(self.SourceFile_check_button)

        self.SourceFile_browser_button = Button(self.SourceFile_Frame, text="Browse",command=self.RefDesign_Src_file_output)
        self.SourceFile_browser_button.grid(row=0, column=10)

         #-------------------------------------------------------------------------------------#

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
            Label(Ref_frame,text='Ref Value:').grid(row=0,column=0,sticky="w")
            Label(Ref_frame,text='Symbol').grid(row=1,column=0,sticky="w")
            Label(Ref_frame,text='Header').grid(row=2,column=0,sticky="w")
            Label(Ref_frame,text='Set To Default').grid(row=4,column=0,sticky="w")
            Label(Ref_frame,text='Clear Input').grid(row=5,column=0,sticky="w")

            self.CUP_Ref_defult_button = Button(Ref_frame,text="Default",command=lambda Button_select=num: self.Default_Button(Button_select))
            self.CUP_Ref_defult_button.grid(row=4,column=1)

            self.CUP_Ref_clear_button = Button(Ref_frame,text="Clear",command=lambda Button_select=num: self.Clear_Button(Button_select))
            self.CUP_Ref_clear_button.grid(row=5,column=1)

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

            for i in range(0,7):
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

            # # Create a list of tuples that contains the text and values of the check buttons
            # self.Ref_design_check_options = [("DDR_14L", "DDR_14L"), 
            #                 ("DDR_16L", "DDR_16L"),
            #                 ("DDR_18L", "DDR_18L"),
            #                 ("XGMI", "XGMI"),
            #                 ("PCIE", "PCIE"),
            #                 ("SATA", "SATA"),
            #                 ("MISC", "MISC"),
            #                 ("USB", "USB"),
            #                 ("CLK", "CLK")]

            # # Create a list of IntVar variables to store the selected check button values
            # self.Ref_design_vars = []
            # for self.option in self.Ref_design_check_options:
            #     var = StringVar()
            #     self.Ref_design_vars.append(var)

            # Use a for loop to create the check buttons
            for i, (text, value) in enumerate(self.SourceFile_check_options):
                self.Ref_design_check_button = Checkbutton(Ref_frame , text=text, variable=self.SourceFile_vars[i], onvalue=value, offvalue=0)
                self.Ref_design_check_button.grid(row=i+1, column=4,sticky="w")
                self.Ref_design_check_button.deselect()
                self.Ref_design_check_button_list.append(self.SourceFile_vars[i])

            self.Ref_design_check_button_widgets.append(self.Ref_design_check_button_list)

            for i in range(0,7):
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
            # clear/empty the list to avoid existing value continue append into CPU_col_insert_entry_widgets
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

        #-------------------------------Breakout/Bus Channel Width GUI---------------------------------------#
        self.RefDsn_BO_Chnl_width = LabelFrame(self.frame,text="Breakout width",labelanchor="n")
        self.RefDsn_BO_Chnl_width.grid(column=1,row=1,padx=20)

        self.RefDsn_Bus_Chnl_width = LabelFrame(self.frame,text="Bus Channel Width",labelanchor="n")
        self.RefDsn_Bus_Chnl_width.grid(column=2,row=1)

        Label(self.RefDsn_BO_Chnl_width,text="DQ").grid(row=0,column=1,padx=5)
        Label(self.RefDsn_BO_Chnl_width,text="DQS").grid(row=0,column=2,padx=5)
        Label(self.RefDsn_BO_Chnl_width,text="Channel A").grid(row=1,column=0,padx=10)
        Label(self.RefDsn_BO_Chnl_width,text="Channel B").grid(row=2,column=0)
        Label(self.RefDsn_BO_Chnl_width,text="Channel C").grid(row=3,column=0)
        Label(self.RefDsn_BO_Chnl_width,text="Channel D").grid(row=4,column=0)
        Label(self.RefDsn_BO_Chnl_width,text="Channel E").grid(row=5,column=0)
        Label(self.RefDsn_BO_Chnl_width,text="Channel F").grid(row=6,column=0)
        Label(self.RefDsn_BO_Chnl_width,text="Channel G").grid(row=7,column=0)
        Label(self.RefDsn_BO_Chnl_width,text="Channel H").grid(row=8,column=0)
        Label(self.RefDsn_BO_Chnl_width,text="Channel I").grid(row=9,column=0)
        Label(self.RefDsn_BO_Chnl_width,text="Channel J").grid(row=10,column=0)
        Label(self.RefDsn_BO_Chnl_width,text="Channel K").grid(row=11,column=0)
        Label(self.RefDsn_BO_Chnl_width,text="Channel L").grid(row=12,column=0)

        self.RefDsn_BO_Chnl_width_DQ_entry_list = []
        for bo_dq_row in range(0,12):
            self.RefDsn_BO_Chnl_width_DQ_entry = Entry(self.RefDsn_BO_Chnl_width,width=5,background='white',fg="black",borderwidth=3)
            self.RefDsn_BO_Chnl_width_DQ_entry.grid(row=bo_dq_row+1,column=1,pady=5,padx=5)
            self.RefDsn_BO_Chnl_width_DQ_entry_list.append(self.RefDsn_BO_Chnl_width_DQ_entry)

        self.RefDsn_BO_Chnl_width_DQS_entry_list = []
        for bo_dqS_row in range(0,12):
            self.RefDsn_BO_Chnl_width_DQS_entry = Entry(self.RefDsn_BO_Chnl_width,width=5,background='white',fg="black",borderwidth=3)
            self.RefDsn_BO_Chnl_width_DQS_entry.grid(row=bo_dqS_row+1,column=2,pady=5,padx=5)
            self.RefDsn_BO_Chnl_width_DQS_entry_list.append(self.RefDsn_BO_Chnl_width_DQS_entry)

        Label(self.RefDsn_Bus_Chnl_width,text="DQ").grid(row=0,column=1,padx=5)
        Label(self.RefDsn_Bus_Chnl_width,text="DQS").grid(row=0,column=2,padx=5)
        Label(self.RefDsn_Bus_Chnl_width,text="Channel A").grid(row=1,column=0,padx=10)
        Label(self.RefDsn_Bus_Chnl_width,text="Channel B").grid(row=2,column=0)
        Label(self.RefDsn_Bus_Chnl_width,text="Channel C").grid(row=3,column=0)
        Label(self.RefDsn_Bus_Chnl_width,text="Channel D").grid(row=4,column=0)
        Label(self.RefDsn_Bus_Chnl_width,text="Channel E").grid(row=5,column=0)
        Label(self.RefDsn_Bus_Chnl_width,text="Channel F").grid(row=6,column=0)
        Label(self.RefDsn_Bus_Chnl_width,text="Channel G").grid(row=7,column=0)
        Label(self.RefDsn_Bus_Chnl_width,text="Channel H").grid(row=8,column=0)
        Label(self.RefDsn_Bus_Chnl_width,text="Channel I").grid(row=9,column=0)
        Label(self.RefDsn_Bus_Chnl_width,text="Channel J").grid(row=10,column=0)
        Label(self.RefDsn_Bus_Chnl_width,text="Channel K").grid(row=11,column=0)
        Label(self.RefDsn_Bus_Chnl_width,text="Channel L").grid(row=12,column=0)

        self.RefDsn_Bus_Chnl_width_DQ_entry_list = []
        for bus_dq_row in range(0,12):
            self.RefDsn_Bus_Chnl_width_DQ_entry = Entry(self.RefDsn_Bus_Chnl_width,width=5,background='white',fg="black",borderwidth=3)
            self.RefDsn_Bus_Chnl_width_DQ_entry.grid(row=bus_dq_row+1,column=1,pady=5,padx=5)
            self.RefDsn_Bus_Chnl_width_DQ_entry_list.append(self.RefDsn_Bus_Chnl_width_DQ_entry)

        self.RefDsn_Bus_Chnl_width_DQS_entry_list = []
        for bus_dqS_row in range(0,12):
            self.RefDsn_Bus_Chnl_width_DQS_entry = Entry(self.RefDsn_Bus_Chnl_width,width=5,background='white',fg="black",borderwidth=3)
            self.RefDsn_Bus_Chnl_width_DQS_entry.grid(row=bus_dqS_row+1,column=2,pady=5,padx=5)
            self.RefDsn_Bus_Chnl_width_DQS_entry_list.append(self.RefDsn_Bus_Chnl_width_DQS_entry)
            
        #------------------------Canvas Scroll BarConfigure---------------------------#
        # Attach a scrollbar to the canvas
        self.scrollbar = Scrollbar(self.rootframe, orient="vertical", command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Configure the canvas and frame to resize with the root window
        self.rootframe.grid_rowconfigure(0, weight=1)
        self.rootframe.grid_columnconfigure(0, weight=1)

        # Add the frame to the canvas
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        # Set the scrollable region of the canvas
        self.frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        #Configure to default when object is initialise:
        self.CUP0_Default(SheetName=False,Col_Lookup=True,StartRowInsert=True,Col_Insert=True)
        self.CUP1_Default(SheetName=False,Col_Lookup=True,StartRowInsert=True,Col_Insert=True)
        self.UsbHub_Default(SheetName=False,Col_Lookup=True,StartRowInsert=True,Col_Insert=True)
        self.ClkBuff_Default(SheetName=False,Col_Lookup=True,StartRowInsert=True,Col_Insert=True)

    def RefDesign_Src_file_output(self):
        self.src_file_output = SourceFile_browse.RefDesign_browse_file()

        self.SourceFile_input_entry.delete(0,END) 
        self.SourceFile_input_entry.insert(0,self.src_file_output)

        # SourceFile_browse.copy_tab(self.src_file_output,Background_GUI_Tool.y,self.SourceFile_vars)

    def copy_InterfaceMmy_data_to_dst(self):
        SourceFile_browse.copy_tab(self.SourceFile_input_entry.get(),self.fileName,self.SourceFile_vars)

    def Clear_Button(self,Button_select):
        for j in range(0,7):
            self.CPU_col_insert_entry_widgets[Button_select][j].delete(0,END)
            self.CPU_col_lookup_entry_widgets[Button_select][j].delete(0,END)
            self.CPU_col_StartRow_entry_widgets[Button_select][j].delete(0,END)

    def Default_Button(self,Button_select):
        self.Clear_Button(Button_select)
        if Button_select == 0:
            self.CUP0_Default(SheetName=False,Col_Lookup=True,StartRowInsert=True,Col_Insert=True)
        if Button_select == 1:
            self.CUP1_Default(SheetName=False,Col_Lookup=True,StartRowInsert=True,Col_Insert=True)
        if Button_select == 2:
            self.UsbHub_Default(SheetName=False,Col_Lookup=True,StartRowInsert=True,Col_Insert=True)
        if Button_select == 3:
                self.ClkBuff_Default(SheetName=False,Col_Lookup=True,StartRowInsert=True,Col_Insert=True)

    def Run_RefDesign_Concat(self):
        for i in range(0,4):
            if self.CPU_Ref_input_entry_widgets[i].get() or self.CPU_Ref_header_entry_widgets[i].get():
                for j in range(0,7):
                    # print((self.Ref_design_check_button_widgets[i][j]).get())
                    if (self.Ref_design_check_button_widgets[i][j].get() != "0" and 
                        self.CPU_col_insert_entry_widgets[i][j].get() != "0" and
                        self.CPU_col_lookup_entry_widgets[i][j].get()!= "0"  and
                        self.CPU_col_StartRow_entry_widgets[i][j].get()!= "0" ):
                            RefDesig_Concat(fileName = self.fileName,
                                            Ref_value=self.CPU_Ref_input_entry_widgets[i].get(),
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


    def CUP0_Default(self, SheetName,Col_Lookup,StartRowInsert,Col_Insert):
        if SheetName == True:
            # -----------------1. Configure Default Sheet Name--------------------------
            self.Ref_design_check_button_widgets[0][0].set("MEMORY")
            self.Ref_design_check_button_widgets[0][1].set("XGMI")
            self.Ref_design_check_button_widgets[0][2].set("PCIE")
            self.Ref_design_check_button_widgets[0][3].set("SATA")
            self.Ref_design_check_button_widgets[0][4].set("MISC")
            self.Ref_design_check_button_widgets[0][5].set("USB")
            self.Ref_design_check_button_widgets[0][6].set("CLK")

        if Col_Lookup == True:
            # -------------------2. Configure Default Column Lookup input-------------------
            self.CPU_col_lookup_entry_widgets[0][0].insert(0,"C")
            self.CPU_col_lookup_entry_widgets[0][1].insert(0,"C")
            self.CPU_col_lookup_entry_widgets[0][2].insert(0,"C")
            self.CPU_col_lookup_entry_widgets[0][3].insert(0,"C")
            self.CPU_col_lookup_entry_widgets[0][4].insert(0,"C")
            self.CPU_col_lookup_entry_widgets[0][5].insert(0,"C")
            self.CPU_col_lookup_entry_widgets[0][6].insert(0,"C")

        if StartRowInsert == True:
            # --------------3. Configure Default Start Row Insert------------------------
            self.CPU_col_StartRow_entry_widgets[0][0].insert(0,"3")
            self.CPU_col_StartRow_entry_widgets[0][1].insert(0,"3")
            self.CPU_col_StartRow_entry_widgets[0][2].insert(0,"3")
            self.CPU_col_StartRow_entry_widgets[0][3].insert(0,"3")
            self.CPU_col_StartRow_entry_widgets[0][4].insert(0,"3")
            self.CPU_col_StartRow_entry_widgets[0][5].insert(0,"3")
            self.CPU_col_StartRow_entry_widgets[0][6].insert(0,"3")


        if Col_Insert == True:
            # --------------4. Configure Default Column Insert-------------------------
            self.CPU_col_insert_entry_widgets[0][0].insert(0,"K")
            self.CPU_col_insert_entry_widgets[0][1].insert(0,"K")
            self.CPU_col_insert_entry_widgets[0][2].insert(0,"K")
            self.CPU_col_insert_entry_widgets[0][3].insert(0,"K")
            self.CPU_col_insert_entry_widgets[0][4].insert(0,"K")
            self.CPU_col_insert_entry_widgets[0][5].insert(0,"K")
            self.CPU_col_insert_entry_widgets[0][6].insert(0,"K")
            
    def CUP1_Default(self, SheetName,Col_Lookup,StartRowInsert,Col_Insert):
        if SheetName == True:
            # -----------------1. Configure Default Sheet Name--------------------------
            self.Ref_design_check_button_widgets[1][0].set("MEMORY")
            self.Ref_design_check_button_widgets[1][1].set("XGMI")
            self.Ref_design_check_button_widgets[1][2].set("PCIE")
            self.Ref_design_check_button_widgets[1][3].set("SATA")
            self.Ref_design_check_button_widgets[1][4].set("MISC")
            self.Ref_design_check_button_widgets[1][5].set("USB")
            self.Ref_design_check_button_widgets[1][6].set("CLK")

        if Col_Lookup == True:
            # -------------------2. Configure Default Column Lookup input-------------------
            self.CPU_col_lookup_entry_widgets[1][0].insert(0,"C")
            self.CPU_col_lookup_entry_widgets[1][1].insert(0,"C")
            self.CPU_col_lookup_entry_widgets[1][2].insert(0,"C")
            self.CPU_col_lookup_entry_widgets[1][3].insert(0,"C")
            self.CPU_col_lookup_entry_widgets[1][4].insert(0,"C")
            self.CPU_col_lookup_entry_widgets[1][5].insert(0,"C")
            self.CPU_col_lookup_entry_widgets[1][6].insert(0,"C")

        if StartRowInsert == True:
            # --------------3. Configure Default Start Row Insert------------------------
            self.CPU_col_StartRow_entry_widgets[1][0].insert(0,"3")
            self.CPU_col_StartRow_entry_widgets[1][1].insert(0,"3")
            self.CPU_col_StartRow_entry_widgets[1][2].insert(0,"3")
            self.CPU_col_StartRow_entry_widgets[1][3].insert(0,"3")
            self.CPU_col_StartRow_entry_widgets[1][4].insert(0,"3")
            self.CPU_col_StartRow_entry_widgets[1][5].insert(0,"3")
            self.CPU_col_StartRow_entry_widgets[1][6].insert(0,"3")


        if Col_Insert == True:
            # --------------4. Configure Default Column Insert-------------------------
            self.CPU_col_insert_entry_widgets[1][0].insert(0,"L")
            self.CPU_col_insert_entry_widgets[1][1].insert(0,"L")
            self.CPU_col_insert_entry_widgets[1][2].insert(0,"L")
            self.CPU_col_insert_entry_widgets[1][3].insert(0,"L")
            self.CPU_col_insert_entry_widgets[1][4].insert(0,"L")
            self.CPU_col_insert_entry_widgets[1][5].insert(0,"L")
            self.CPU_col_insert_entry_widgets[1][6].insert(0,"L")

    def UsbHub_Default(self, SheetName,Col_Lookup,StartRowInsert,Col_Insert):
        if SheetName == True:
            # -----------------1. Configure Default Sheet Name--------------------------
            self.Ref_design_check_button_widgets[2][0].set("MEMORY")
            self.Ref_design_check_button_widgets[2][1].set("XGMI")
            self.Ref_design_check_button_widgets[2][2].set("PCIE")
            self.Ref_design_check_button_widgets[2][3].set("SATA")
            self.Ref_design_check_button_widgets[2][4].set("MISC")
            self.Ref_design_check_button_widgets[2][5].set("USB")
            self.Ref_design_check_button_widgets[2][6].set("CLK")

        if Col_Lookup == True:
            # -------------------2. Configure Default Column Lookup input-------------------
            self.CPU_col_lookup_entry_widgets[2][0].insert(0,"C")
            self.CPU_col_lookup_entry_widgets[2][1].insert(0,"C")
            self.CPU_col_lookup_entry_widgets[2][2].insert(0,"C")
            self.CPU_col_lookup_entry_widgets[2][3].insert(0,"C")
            self.CPU_col_lookup_entry_widgets[2][4].insert(0,"C")
            self.CPU_col_lookup_entry_widgets[2][5].insert(0,"C")
            self.CPU_col_lookup_entry_widgets[2][6].insert(0,"C")

        if StartRowInsert == True:
            # --------------3. Configure Default Start Row Insert------------------------
            self.CPU_col_StartRow_entry_widgets[2][0].insert(0,"3")
            self.CPU_col_StartRow_entry_widgets[2][1].insert(0,"3")
            self.CPU_col_StartRow_entry_widgets[2][2].insert(0,"3")
            self.CPU_col_StartRow_entry_widgets[2][3].insert(0,"3")
            self.CPU_col_StartRow_entry_widgets[2][4].insert(0,"3")
            self.CPU_col_StartRow_entry_widgets[2][5].insert(0,"3")
            self.CPU_col_StartRow_entry_widgets[2][6].insert(0,"3")


        if Col_Insert == True:
            # --------------4. Configure Default Column Insert-------------------------
            self.CPU_col_insert_entry_widgets[2][0].insert(0,"M")
            self.CPU_col_insert_entry_widgets[2][1].insert(0,"M")
            self.CPU_col_insert_entry_widgets[2][2].insert(0,"M")
            self.CPU_col_insert_entry_widgets[2][3].insert(0,"M")
            self.CPU_col_insert_entry_widgets[2][4].insert(0,"M")
            self.CPU_col_insert_entry_widgets[2][5].insert(0,"M")
            self.CPU_col_insert_entry_widgets[2][6].insert(0,"M")

    def ClkBuff_Default(self, SheetName,Col_Lookup,StartRowInsert,Col_Insert):
        if SheetName == True:
            # -----------------1. Configure Default Sheet Name--------------------------
            self.Ref_design_check_button_widgets[3][0].set("MEMORY")
            self.Ref_design_check_button_widgets[3][1].set("XGMI")
            self.Ref_design_check_button_widgets[3][2].set("PCIE")
            self.Ref_design_check_button_widgets[3][3].set("SATA")
            self.Ref_design_check_button_widgets[3][4].set("MISC")
            self.Ref_design_check_button_widgets[3][5].set("USB")
            self.Ref_design_check_button_widgets[3][6].set("CLK")

        if Col_Lookup == True:
            # -------------------2. Configure Default Column Lookup input-------------------
            self.CPU_col_lookup_entry_widgets[3][0].insert(0,"C")
            self.CPU_col_lookup_entry_widgets[3][1].insert(0,"C")
            self.CPU_col_lookup_entry_widgets[3][2].insert(0,"C")
            self.CPU_col_lookup_entry_widgets[3][3].insert(0,"C")
            self.CPU_col_lookup_entry_widgets[3][4].insert(0,"C")
            self.CPU_col_lookup_entry_widgets[3][5].insert(0,"C")
            self.CPU_col_lookup_entry_widgets[3][6].insert(0,"C")

        if StartRowInsert == True:
            # --------------3. Configure Default Start Row Insert------------------------
            self.CPU_col_StartRow_entry_widgets[3][0].insert(0,"3")
            self.CPU_col_StartRow_entry_widgets[3][1].insert(0,"3")
            self.CPU_col_StartRow_entry_widgets[3][2].insert(0,"3")
            self.CPU_col_StartRow_entry_widgets[3][3].insert(0,"3")
            self.CPU_col_StartRow_entry_widgets[3][4].insert(0,"3")
            self.CPU_col_StartRow_entry_widgets[3][5].insert(0,"3")
            self.CPU_col_StartRow_entry_widgets[3][6].insert(0,"3")


        if Col_Insert == True:
            # --------------4. Configure Default Column Insert-------------------------
            self.CPU_col_insert_entry_widgets[3][0].insert(0,"O")
            self.CPU_col_insert_entry_widgets[3][1].insert(0,"O")
            self.CPU_col_insert_entry_widgets[3][2].insert(0,"O")
            self.CPU_col_insert_entry_widgets[3][3].insert(0,"O")
            self.CPU_col_insert_entry_widgets[3][4].insert(0,"O")
            self.CPU_col_insert_entry_widgets[3][5].insert(0,"O")
            self.CPU_col_insert_entry_widgets[3][6].insert(0,"O")
        

# if __name__ =='__main__':
#     test()