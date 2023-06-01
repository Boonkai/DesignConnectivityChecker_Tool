import Background_GUI_Tool
from tkinter import *
from tkinter import ttk
from HtmlDataExtraction import *
from FileBrowser.FileBrowser import browser
# Set folowwing directory to default path for debugging purpose
# Netpin = "/Users/yeamboonkai/Desktop/AMD_Project/Input_Files/Component_Pin_Report.htm"
# Netlist = "/Users/yeamboonkai/Desktop/AMD_Project/Input_Files/Netlist.htm"
# BOMFile = "/Users/yeamboonkai/Desktop/AMD_Project/Input_Files/BOM.htm"
# lenWid = "/Users/yeamboonkai/Desktop/AMD_Project/Input_Files/Etch_Length_Width_Layer.htm"
# LayerStack = "/Users/yeamboonkai/Desktop/AMD_Project/Input_Files/Layer_Stackup_report.htm"

class mainGUI:
    def __init__(self):
        self.Browse_file = browser()
        self.BackGui_obj = Background_GUI_Tool.Background_GUI()
        self.main_Gui_root = Toplevel(self.BackGui_obj.BackGui_root)
        self.main_Gui_root.title("Main screen")
        #---------------------Create the Notebook widget------------------------#
        self.notebook = ttk.Notebook(self.main_Gui_root)

        # Create the first tab
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text='HTML Data Extraction')
        self.notebook.grid(columnspan=3)

        # Create the second tab
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text='Breakout/Bus Channel Width')
        self.notebook.grid()

        #---------------------kinder GUI: Report File Input-----------------------#
        self.ReportFile_Frame = LabelFrame(self.tab1,text="Report Files Input",labelanchor="n")
        self.ReportFile_Frame.grid(row=0,column=1,columnspan=4,padx=10,pady=10)
        self.main_Gui_root.protocol("WM_DELETE_WINDOW",self.pressExit)

        #-------------------tkinder GUI: Reference Designator-------------------------#
        self.RefDesignator = LabelFrame(self.tab1, text="Reference Designator",padx=10, pady=10,labelanchor='n')
        self.RefDesignator.grid(padx=10,pady=10,row=0,column=0,rowspan=2)

        #CPU0 Input field
        self.CPU0_Label = Label(self.RefDesignator,text="CPU0:")
        self.CPU0_Label.grid(row=0,column=0,sticky='w',pady=20)

        self.CPU0_input_entry = Entry(self.RefDesignator,width=5,background='white',fg="black",borderwidth=3)
        self.CPU0_input_entry.grid(row=0, column=1)

        #CPU1 Input field
        self.CPU1_Label = Label(self.RefDesignator,text="CPU1:")
        self.CPU1_Label.grid(row=1,column=0,sticky='w',pady=20)

        self.CPU1_input_entry = Entry(self.RefDesignator,width=5,background='white',fg="black",borderwidth=3)
        self.CPU1_input_entry.grid(row=1, column=1)

        #UsbHub Input field
        self.UsbHub_Label = Label(self.RefDesignator,text="USB HUB:")
        self.UsbHub_Label.grid(row=2,column=0,sticky='w',pady=20)
        self.UsbHub_input_entry = Entry(self.RefDesignator,width=5,background='white',fg="black",borderwidth=3)
        self.UsbHub_input_entry.grid(row=2, column=1)

        #Clock Buff Input field
        self.ClkBuff_Label = Label(self.RefDesignator,text="Clock Buffer:")
        self.ClkBuff_Label.grid(row=3,column=0,sticky='w',pady=20)
        self.ClkBuff_input_entry = Entry(self.RefDesignator,width=5,background='white',fg="black",borderwidth=3)
        self.ClkBuff_input_entry.grid(row=3, column=1)

        #--------------------NetPin tkinder GUI------------------------------------#
        # create a label for the input field
        self.NetPin_main_input_label = Label(self.ReportFile_Frame, text="Component Pin File:")
        self.NetPin_main_input_label.grid(row=0, column=0,padx=15,pady=15)
    
        self.NetPin_main_input_entry = Entry(self.ReportFile_Frame ,width=70,background='white',fg="black",borderwidth=3)
        self.NetPin_main_input_entry.grid(row=0,column=1,padx=15,pady=15)

        # create a button on Main Screen (Main Manager) to launch the file browser
        self.NetPin_main_browser_button = Button(self.ReportFile_Frame , text="Browse",command=self.NetPin_browse_file)
        self.NetPin_main_browser_button.grid(row=0, column=2,padx=15,pady=15)

        # create a button on Development Tool (Background Manager) to launch the file browser
        self.NetPin_browser_button = Button(self.BackGui_obj.NetPin_Gui_obj.NetPin_frame, text="Browse", command=self.NetPin_browse_file)
        self.NetPin_browser_button.grid(row=0, column=8)

        #--------------------Netlist tkinder GUI------------------------------------#
        # create a label for the input field
        self.Netlist_main_input_label = Label(self.ReportFile_Frame, text="Netlist File:")
        self.Netlist_main_input_label.grid(row=1, column=0,padx=15,pady=15)
    
        self.Netlist_main_input_entry = Entry(self.ReportFile_Frame ,width=70,background='white',fg="black",borderwidth=3)
        self.Netlist_main_input_entry.grid(row=1,column=1,padx=15,pady=15)

        # create a button on Main Screen (Main Manager) to launch the file browser
        self.Netlist_main_browser_button = Button(self.ReportFile_Frame , text="Browse",command=self.Netlist_browse_file)
        self.Netlist_main_browser_button.grid(row=1, column=2,padx=15,pady=15)

        # create a button on Development Tool (Background Manager) to launch the file browser
        self.Netlist_browser_button = Button(self.BackGui_obj.Netlist_Gui_obj.Netlist_frame, text="Browse", command=self.Netlist_browse_file)
        self.Netlist_browser_button.grid(row=0, column=8)

        #--------------------BOM tkinder GUI------------------------------------#
        # create a label for the input field
        self.BOM_main_input_label = Label(self.ReportFile_Frame, text="BOM File:")
        self.BOM_main_input_label.grid(row=2, column=0,padx=15,pady=15)
    
        self.BOM_main_input_entry = Entry(self.ReportFile_Frame ,width=70,background='white',fg="black",borderwidth=3)
        self.BOM_main_input_entry.grid(row=2,column=1,padx=15,pady=15)

        # create a button on Main Screen (Main Manager) to launch the file browser
        self.BOM_main_browser_button = Button(self.ReportFile_Frame , text="Browse",command=self.BOM_browse_file)
        self.BOM_main_browser_button.grid(row=2, column=2,padx=15,pady=15)

        # create a button on Development Tool (Background Manager) to launch the file browser
        self.BOM_browser_button = Button(self.BackGui_obj.BOM_Gui_obj.BOM_frame, text="Browse", command=self.BOM_browse_file)
        self.BOM_browser_button.grid(row=0, column=8)

        #--------------------LenWidLayer tkinder GUI------------------------------------#
        # create a label for the input field
        self.LenWidLayer_main_input_label = Label(self.ReportFile_Frame, text="Length Width Layer File:")
        self.LenWidLayer_main_input_label.grid(row=3, column=0,padx=15,pady=15)
    
        self.LenWidLayer_main_input_entry = Entry(self.ReportFile_Frame ,width=70,background='white',fg="black",borderwidth=3)
        self.LenWidLayer_main_input_entry.grid(row=3,column=1,padx=15,pady=15)

        # create a button on Main Screen (Main Manager) to launch the file browser
        self.LenWidLayer_main_browser_button = Button(self.ReportFile_Frame , text="Browse",command=self.LenWidLayer_browse_file)
        self.LenWidLayer_main_browser_button.grid(row=3, column=2,padx=15,pady=15)

        # create a button on Development Tool (Background Manager) to launch the file browser
        self.LenWidLayer_browser_button = Button(self.BackGui_obj.LenWidLayer_Gui_obj.LenWidLayer_frame, text="Browse", command=self.LenWidLayer_browse_file)
        self.LenWidLayer_browser_button.grid(row=0, column=8)

        #--------------------Layer Stackup tkinder GUI------------------------------------#
        # create a label for the input field
        self.LayerStackup_main_input_label = Label(self.ReportFile_Frame, text="Layer Stackup File:")
        self.LayerStackup_main_input_label.grid(row=4, column=0,padx=15,pady=15)
    
        self.LayerStackup_main_input_entry = Entry(self.ReportFile_Frame ,width=70,background='white',fg="black",borderwidth=3)
        self.LayerStackup_main_input_entry.grid(row=4,column=1,padx=15,pady=15)

        # create a button on Main Screen (Main Manager) to launch the file browser
        self.LayerStackup_main_browser_button = Button(self.ReportFile_Frame , text="Browse", command=self.LyrStack_browse_file)
        self.LayerStackup_main_browser_button.grid(row=4, column=2,padx=15,pady=15)

        # create a button on Development Tool (Background Manager) to launch the file browser
        self.LayerStackup_browser_button = Button(self.BackGui_obj.LayerStackup_Gui_obj.LyrStack_frame , text="Browse", command=self.LyrStack_browse_file)
        self.LayerStackup_browser_button.grid(row=0, column=8)

    #--------------------Set Report Files input to default path-----------------------
        # self.NetPin_main_input_entry.insert(0, Netpin)
        # self.BackGui_obj.NetPin_Gui_obj.NetPin_input_entry.insert(0,Netpin)

        # self.Netlist_main_input_entry.insert(0, Netlist)
        # self.BackGui_obj.Netlist_Gui_obj.Netlist_input_entry.insert(0,Netlist)

        # self.BOM_main_input_entry.insert(0, BOMFile)
        # self.BackGui_obj.BOM_Gui_obj.BOM_input_entry.insert(0,BOMFile)

        # self.LenWidLayer_main_input_entry.insert(0, lenWid)
        # self.BackGui_obj.LenWidLayer_Gui_obj.LenWidLayer_input_entry.insert(0,lenWid)

        # self.LayerStackup_main_input_entry.insert(0, LayerStack)
        # self.BackGui_obj.LayerStackup_Gui_obj.LyrStack_input_entry.insert(0,LayerStack)

        # --------------------Memory, PCIe, XGMI, USB, SATA , MISC label and Checkbox-----------------#
        self.MmyIntf_Frame = LabelFrame(self.tab1, text="Memory Interface",padx=10, pady=10,labelanchor='n')
        self.MmyIntf_Frame .grid(padx=5,pady=5,row=1,column=1)

        self.var =self.BackGui_obj.RefDesignator_Gui_obj.SourceFile_vars

        # Use a for loop to create the check buttons
        for i, (text, value) in enumerate(self.BackGui_obj.RefDesignator_Gui_obj.SourceFile_check_options):
            self.mainGUI_check_button = Checkbutton(self.MmyIntf_Frame, text=text, variable=self.var[i], onvalue=value, offvalue=0,font=("Arial", 18))
            if i < 3:
                self.mainGUI_check_button.grid(row=0,padx=110, column=i,sticky="w")
                self.mainGUI_check_button.select()
            if 3<=i<=5:
                self.mainGUI_check_button.grid(row=1,padx=110,column=i-3,sticky="w")
                self.mainGUI_check_button.deselect()
            if 6<=i<=8:
                self.mainGUI_check_button.grid(row=3,padx=110,column=i-6,sticky="w")
                self.mainGUI_check_button.deselect()


        #-------------------Create Development Tool button-------------------------------#
        self.presshow = Button(self.main_Gui_root, text="Development Tool",command=self.showBack)
        self.presshow.grid(row=1,column=0,pady=10)

        #-------------------Create the export button--------------------------#
        self.export_button = Button(self.main_Gui_root, text="Generate Report", command=self.BackGui_obj.Generate_Report)
        self.export_button.grid(row=1,column=1,pady=10)

        #------------------Create Sync input Button--------------------------------#
        # self.sync_button = Button(self.main_Gui_root, text="Sync Input")
        # self.sync_button.grid(row=1,column=2,pady=20)

        #----------------- Create Exit Button------------------------------------#
        self.pressexit = Button(self.main_Gui_root, text="Exit",command=self.pressExit)
        self.pressexit.grid(row=1,column=2,pady=10)

        #-------------------------------Breakout/Bus Channel Width GUI---------------------------------------#
        self.Main_BO_Chnl_width = LabelFrame(self.tab2,text="Breakout width",labelanchor="n")
        self.Main_BO_Chnl_width.grid(column=0,row=0,padx=20)

        self.Main_Bus_Chnl_width = LabelFrame(self.tab2,text="Bus Channel Width",labelanchor="n")
        self.Main_Bus_Chnl_width.grid(column=1,row=0)

        Label(self.Main_BO_Chnl_width,text="DQ").grid(row=0,column=1,padx=5)
        Label(self.Main_BO_Chnl_width,text="DQS").grid(row=0,column=2,padx=5)
        Label(self.Main_BO_Chnl_width,text="Channel A").grid(row=1,column=0,padx=10)
        Label(self.Main_BO_Chnl_width,text="Channel B").grid(row=2,column=0)
        Label(self.Main_BO_Chnl_width,text="Channel C").grid(row=3,column=0)
        Label(self.Main_BO_Chnl_width,text="Channel D").grid(row=4,column=0)
        Label(self.Main_BO_Chnl_width,text="Channel E").grid(row=5,column=0)
        Label(self.Main_BO_Chnl_width,text="Channel F").grid(row=6,column=0)
        Label(self.Main_BO_Chnl_width,text="Channel G").grid(row=7,column=0)
        Label(self.Main_BO_Chnl_width,text="Channel H").grid(row=8,column=0)
        Label(self.Main_BO_Chnl_width,text="Channel I").grid(row=9,column=0)
        Label(self.Main_BO_Chnl_width,text="Channel J").grid(row=10,column=0)
        Label(self.Main_BO_Chnl_width,text="Channel K").grid(row=11,column=0)
        Label(self.Main_BO_Chnl_width,text="Channel L").grid(row=12,column=0)

        self.Main_BO_Chnl_width_DQ_entry_list = []
        for bo_dq_row in range(0,12):
            self.Main_BO_Chnl_width_DQ_entry = Entry(self.Main_BO_Chnl_width,width=5,background='white',fg="black",borderwidth=3)
            self.Main_BO_Chnl_width_DQ_entry.grid(row=bo_dq_row+1,column=1,pady=5,padx=5)
            self.Main_BO_Chnl_width_DQ_entry_list.append(self.Main_BO_Chnl_width_DQ_entry)

        self.Main_BO_Chnl_width_DQS_entry_list = []
        for bo_dqS_row in range(0,12):
            self.Main_BO_Chnl_width_DQS_entry = Entry(self.Main_BO_Chnl_width,width=5,background='white',fg="black",borderwidth=3)
            self.Main_BO_Chnl_width_DQS_entry.grid(row=bo_dqS_row+1,column=2,pady=5,padx=5)
            self.Main_BO_Chnl_width_DQS_entry_list.append(self.Main_BO_Chnl_width_DQS_entry)

        Label(self.Main_Bus_Chnl_width,text="DQ").grid(row=0,column=1,padx=5)
        Label(self.Main_Bus_Chnl_width,text="DQS").grid(row=0,column=2,padx=5)
        Label(self.Main_Bus_Chnl_width,text="Channel A").grid(row=1,column=0,padx=10)
        Label(self.Main_Bus_Chnl_width,text="Channel B").grid(row=2,column=0)
        Label(self.Main_Bus_Chnl_width,text="Channel C").grid(row=3,column=0)
        Label(self.Main_Bus_Chnl_width,text="Channel D").grid(row=4,column=0)
        Label(self.Main_Bus_Chnl_width,text="Channel E").grid(row=5,column=0)
        Label(self.Main_Bus_Chnl_width,text="Channel F").grid(row=6,column=0)
        Label(self.Main_Bus_Chnl_width,text="Channel G").grid(row=7,column=0)
        Label(self.Main_Bus_Chnl_width,text="Channel H").grid(row=8,column=0)
        Label(self.Main_Bus_Chnl_width,text="Channel I").grid(row=9,column=0)
        Label(self.Main_Bus_Chnl_width,text="Channel J").grid(row=10,column=0)
        Label(self.Main_Bus_Chnl_width,text="Channel K").grid(row=11,column=0)
        Label(self.Main_Bus_Chnl_width,text="Channel L").grid(row=12,column=0)

        self.Main_Bus_Chnl_width_DQ_entry_list = []
        for bus_dq_row in range(0,12):
            self.Main_Bus_Chnl_width_DQ_entry = Entry(self.Main_Bus_Chnl_width,width=5,background='white',fg="black",borderwidth=3)
            self.Main_Bus_Chnl_width_DQ_entry.grid(row=bus_dq_row+1,column=1,pady=5,padx=5)
            self.Main_Bus_Chnl_width_DQ_entry_list.append(self.Main_Bus_Chnl_width_DQ_entry)

        self.Main_Bus_Chnl_width_DQS_entry_list = []
        for bus_dqS_row in range(0,12):
            self.Main_Bus_Chnl_width_DQS_entry = Entry(self.Main_Bus_Chnl_width,width=5,background='white',fg="black",borderwidth=3)
            self.Main_Bus_Chnl_width_DQS_entry.grid(row=bus_dqS_row+1,column=2,pady=5,padx=5)
            self.Main_Bus_Chnl_width_DQS_entry_list.append(self.Main_Bus_Chnl_width_DQS_entry)

        #------------------------DDR Length Input GUI--------------------------------#
        self.DDR_LengthFrm_mainScr = LabelFrame(self.tab2, text="DDR Length",labelanchor="n")
        self.DDR_LengthFrm_mainScr.grid(row=0,column=2,padx=20)

        self.DDR_Length_label_mainScr = Label(self.DDR_LengthFrm_mainScr,text="DDR Length Value:")
        self.DDR_Length_label_mainScr.grid(row=0,column=0,padx=5,pady=5,sticky="w")
        self.DDR_Length_val_entry_mainScr = Entry(self.DDR_LengthFrm_mainScr,width=10,borderwidth=3,background="white",fg="black")
        self.DDR_Length_val_entry_mainScr.grid(row=0,column=1,padx=5,pady=5)

        #-----------------------Sync main and background input--------------------------#
        # Bind sync_main_entry to the KeyRelease event of entry 
        # 1) CPU Reference Designator input
        self.CPU0_input_entry.bind("<KeyRelease>", self.sync_RefDsn_main_entry)
        self.CPU1_input_entry.bind("<KeyRelease>", self.sync_RefDsn_main_entry)
        self.UsbHub_input_entry.bind("<KeyRelease>", self.sync_RefDsn_main_entry)
        self.ClkBuff_input_entry.bind("<KeyRelease>", self.sync_RefDsn_main_entry)
        
        # 2) Breakout DQ input (main Page)
        for boDq in self.Main_BO_Chnl_width_DQ_entry_list:
            boDq.bind("<KeyRelease>", self.sync_LyrStack_main_entry)

        # 3) Breakout DQS input (main Page)
        for boDqs in self.Main_BO_Chnl_width_DQS_entry_list:
            boDqs.bind("<KeyRelease>", self.sync_LyrStack_main_entry)

        # 4) BUS Channel DQ input (main Page)
        for busDq in self.Main_Bus_Chnl_width_DQ_entry_list:
            busDq.bind("<KeyRelease>", self.sync_LyrStack_main_entry)

        # 5) BUS Channel DQS input (main Page)
        for busDqs in self.Main_Bus_Chnl_width_DQS_entry_list:
            busDqs.bind("<KeyRelease>", self.sync_LyrStack_main_entry)

        # 6) DDR Length input (main Page)
        self.DDR_Length_val_entry_mainScr.bind("<KeyRelease>",self.sync_DDR_Length_main_entry)


        # Bind sync_background_entry to the KeyRelease event of entry
         # 1) CPU Reference Designator input (developemnt Page)
        self.BackGui_obj.RefDesignator_Gui_obj.CPU_Ref_input_entry_widgets[0].bind("<KeyRelease>", self.sync_RefDsgn_background_entry)
        self.BackGui_obj.RefDesignator_Gui_obj.CPU_Ref_input_entry_widgets[1].bind("<KeyRelease>", self.sync_RefDsgn_background_entry)
        self.BackGui_obj.RefDesignator_Gui_obj.CPU_Ref_input_entry_widgets[2].bind("<KeyRelease>", self.sync_RefDsgn_background_entry)
        self.BackGui_obj.RefDesignator_Gui_obj.CPU_Ref_input_entry_widgets[3].bind("<KeyRelease>", self.sync_RefDsgn_background_entry)

        # 2) Breakout DQ input (developemnt Page)
        self.boDq_backgrd_entry_list = self.BackGui_obj.RefDesignator_Gui_obj.RefDsn_BO_Chnl_width_DQ_entry_list
        for boDq in self.boDq_backgrd_entry_list:
            boDq.bind("<KeyRelease>", self.sync_LyrStack_background_entry)

        # 3) Breakout DQS input (developemnt Page)
        self.boDqs_backgrd_entry_list = self.BackGui_obj.RefDesignator_Gui_obj.RefDsn_BO_Chnl_width_DQS_entry_list
        for boDqs in self.boDqs_backgrd_entry_list:
            boDqs.bind("<KeyRelease>", self.sync_LyrStack_background_entry)

        # 4) Bus Channel DQ input (developemnt Page)
        self.busDq_backgrd_entry_list = self.BackGui_obj.RefDesignator_Gui_obj.RefDsn_Bus_Chnl_width_DQ_entry_list
        for busDq in self.busDq_backgrd_entry_list:
            busDq.bind("<KeyRelease>", self.sync_LyrStack_background_entry)

        # 5) Bus Channel DQS input (developemnt Page)
        self.busDqs_backgrd_entry_list = self.BackGui_obj.RefDesignator_Gui_obj.RefDsn_Bus_Chnl_width_DQS_entry_list
        for busDqs in self.busDqs_backgrd_entry_list:
            busDqs.bind("<KeyRelease>", self.sync_LyrStack_background_entry)

        # 6) DDR Length input (developemnt Page)
        self.BackGui_obj.RefDesignator_Gui_obj.DDR_Length_val_entry.bind("<KeyRelease>", self.sync_DDR_Legth_background_entry)


    """
    In this case, the event parameter in the sync_entry1 method is the Event object associated with the event that 
    triggered the function.

    When we bind a function to an event, the function will receive an Event object as its first parameter. This object 
    contains information about the event that was triggered, such as the widget that triggered the event, the type of event, 
    the time the event occurred, and so on.

    In our case, we use the event parameter to get the current value of the first Entry widget using self.entry1.get(). 
    We don't actually use any information from the Event object itself, but we still need to include it as a parameter 
    in the function definition because it is automatically passed to the function when the event is triggered.
    """
    def sync_RefDsn_main_entry(self, event):
        # print(event) # press 'A' event output = <KeyRelease event keysym=a keycode=97 char='a' x=25 y=19>

        # Update the value of sync_background_entry
        self.BackGui_obj.RefDesignator_Gui_obj.CPU_Ref_input_entry_widgets[0].delete(0, END)
        self.BackGui_obj.RefDesignator_Gui_obj.CPU_Ref_input_entry_widgets[0].insert(0, self.CPU0_input_entry.get())

        self.BackGui_obj.RefDesignator_Gui_obj.CPU_Ref_input_entry_widgets[1].delete(0, END)
        self.BackGui_obj.RefDesignator_Gui_obj.CPU_Ref_input_entry_widgets[1].insert(0, self.CPU1_input_entry.get())

        self.BackGui_obj.RefDesignator_Gui_obj.CPU_Ref_input_entry_widgets[2].delete(0, END)
        self.BackGui_obj.RefDesignator_Gui_obj.CPU_Ref_input_entry_widgets[2].insert(0, self.UsbHub_input_entry.get())

        self.BackGui_obj.RefDesignator_Gui_obj.CPU_Ref_input_entry_widgets[3].delete(0, END)
        self.BackGui_obj.RefDesignator_Gui_obj.CPU_Ref_input_entry_widgets[3].insert(0, self.ClkBuff_input_entry.get())

    def sync_LyrStack_main_entry(self, event):

        for num, boDq in enumerate(self.boDq_backgrd_entry_list):
            boDq.delete(0, END)
            boDq.insert(0, self.Main_BO_Chnl_width_DQ_entry_list[num].get())

        for num, boDqs in enumerate(self.boDqs_backgrd_entry_list):
            boDqs.delete(0, END)
            boDqs.insert(0, self.Main_BO_Chnl_width_DQS_entry_list[num].get())

        for num, busDq in enumerate(self.busDq_backgrd_entry_list):
            busDq.delete(0, END)
            busDq.insert(0, self.Main_Bus_Chnl_width_DQ_entry_list[num].get())

        for num, busDqs in enumerate(self.busDqs_backgrd_entry_list):
            busDqs.delete(0, END)
            busDqs.insert(0, self.Main_Bus_Chnl_width_DQS_entry_list[num].get())

        #self.BackGui_obj.RefDesignator_Gui_obj.RefDsn_BO_Chnl_width_DQ_entry_list[0].delete(0, END)
        # self.BackGui_obj.RefDesignator_Gui_obj.RefDsn_BO_Chnl_width_DQ_entry_list[0].insert(0, self.Main_BO_Chnl_width_DQ_entry_list[0].get())

    def sync_DDR_Length_main_entry(self,event):
        self.BackGui_obj.RefDesignator_Gui_obj.DDR_Length_val_entry.delete(0,END)
        self.BackGui_obj.RefDesignator_Gui_obj.DDR_Length_val_entry.insert(0,self.DDR_Length_val_entry_mainScr.get())

    def sync_RefDsgn_background_entry(self, event):
        # Update the value of sync_main_entry
        self.CPU0_input_entry.delete(0, END)
        self.CPU0_input_entry.insert(0, self.BackGui_obj.RefDesignator_Gui_obj.CPU_Ref_input_entry_widgets[0].get())

        self.CPU1_input_entry.delete(0, END)
        self.CPU1_input_entry.insert(0, self.BackGui_obj.RefDesignator_Gui_obj.CPU_Ref_input_entry_widgets[1].get())

        self.UsbHub_input_entry.delete(0, END)
        self.UsbHub_input_entry.insert(0, self.BackGui_obj.RefDesignator_Gui_obj.CPU_Ref_input_entry_widgets[2].get())

        self.ClkBuff_input_entry.delete(0, END)
        self.ClkBuff_input_entry.insert(0, self.BackGui_obj.RefDesignator_Gui_obj.CPU_Ref_input_entry_widgets[3].get())

    def sync_LyrStack_background_entry(self, event):

        for num, boDq in enumerate(self.Main_BO_Chnl_width_DQ_entry_list):
            boDq.delete(0, END)
            boDq.insert(0, self.boDq_backgrd_entry_list[num].get())

        for num, boDqs in enumerate(self.Main_BO_Chnl_width_DQS_entry_list):
            boDqs.delete(0, END)
            boDqs.insert(0, self.boDqs_backgrd_entry_list[num].get())

        for num, busDq in enumerate(self.Main_Bus_Chnl_width_DQ_entry_list):
            busDq.delete(0, END)
            busDq.insert(0, self.busDq_backgrd_entry_list[num].get())

        for num, busDqs in enumerate(self.Main_Bus_Chnl_width_DQS_entry_list):
            busDqs.delete(0, END)
            busDqs.insert(0, self.busDqs_backgrd_entry_list[num].get())

        # self.Main_BO_Chnl_width_DQ_entry_list[0].delete(0, END)
        # self.Main_BO_Chnl_width_DQ_entry_list[0].insert(0,self.BackGui_obj.RefDesignator_Gui_obj.RefDsn_BO_Chnl_width_DQ_entry_list[0].get())
    
    def sync_DDR_Legth_background_entry(self,event):
        self.DDR_Length_val_entry_mainScr.delete(0, END)
        self.DDR_Length_val_entry_mainScr.insert(0, self.BackGui_obj.RefDesignator_Gui_obj.DDR_Length_val_entry.get())


    #---------------------NetPin File Browser-----------------------------------
    # create a function to open the file browser and select a file
    def NetPin_browse_file(self):
        self.NetPin_file_Path = self.Browse_file.browse_file()

        # set default path for quick debugging 
        # self.NetPin_file_Path = Netpin 
        
        # Update main input
        self.NetPin_main_input_entry.delete(0, END)
        self.NetPin_main_input_entry.insert(0, self.NetPin_file_Path)

        # Update background input
        self.BackGui_obj.NetPin_Gui_obj.NetPin_input_entry.delete(0,END)
        self.BackGui_obj.NetPin_Gui_obj.NetPin_input_entry.insert(0,self.NetPin_file_Path)

    #---------------------Netlist Browse File-----------------------------------
    # create a function to open the file browser and select a file
    def Netlist_browse_file(self):
        self.Netlist_file_Path = self.Browse_file.browse_file()

        # set default path for quick debugging 
        # self.Netlist_file_Path = Netlist
        
        # Update main input
        self.Netlist_main_input_entry.delete(0, END)
        self.Netlist_main_input_entry.insert(0, self.Netlist_file_Path)

        # Update background input
        self.BackGui_obj.Netlist_Gui_obj.Netlist_input_entry.delete(0,END)
        self.BackGui_obj.Netlist_Gui_obj.Netlist_input_entry.insert(0,self.Netlist_file_Path)

    #---------------------BOM Browse File-----------------------------------
    # create a function to open the file browser and select a file
    def BOM_browse_file(self):
        self.BOM_file_Path = self.Browse_file.browse_file()

        # set default path for quick debugging 
        # self.BOM_file_Path = BOMFile
        
        # Update main input
        self.BOM_main_input_entry.delete(0, END)
        self.BOM_main_input_entry.insert(0, self.BOM_file_Path)

        # Update background input
        self.BackGui_obj.BOM_Gui_obj.BOM_input_entry.delete(0,END)
        self.BackGui_obj.BOM_Gui_obj.BOM_input_entry.insert(0,self.BOM_file_Path)

    #---------------------Length Width Layer Browse File-----------------------------------
    # create a function to open the file browser and select a file
    def LenWidLayer_browse_file(self):
        self.LenWidLayer_file_Path = self.Browse_file.browse_file()
        
        # set default path for quick debugging 
        # self.LenWidLayer_file_Path = lenWid

        # Update main input
        self.LenWidLayer_main_input_entry.delete(0, END)
        self.LenWidLayer_main_input_entry.insert(0, self.LenWidLayer_file_Path)

        # Update background input
        self.BackGui_obj.LenWidLayer_Gui_obj.LenWidLayer_input_entry.delete(0,END)
        self.BackGui_obj.LenWidLayer_Gui_obj.LenWidLayer_input_entry.insert(0,self.LenWidLayer_file_Path)

    #---------------------Layer Stackup Browse File-----------------------------------
    # create a function to open the file browser and select a file
    def LyrStack_browse_file(self):
        self.LyrStack_file_Path = self.Browse_file.browse_file()

        # set default path for quick debugging 
        # self.LyrStack_file_Path = LayerStack
        
        # Update main input
        self.LayerStackup_main_input_entry.delete(0, END)
        self.LayerStackup_main_input_entry.insert(0, self.LyrStack_file_Path)

        # Update background input
        self.BackGui_obj.LayerStackup_Gui_obj.LyrStack_input_entry.delete(0,END)
        self.BackGui_obj.LayerStackup_Gui_obj.LyrStack_input_entry.insert(0,self.LyrStack_file_Path)

    def pressExit(self):
        self.BackGui_obj.BackGui_root.destroy()
        # self.main_Gui_root.destroy()

    def showBack(self):
        self.BackGui_obj.BackGui_root.deiconify()

    def run_mainGUI(self):
        self.main_Gui_root.mainloop()

MainGui_Obj = mainGUI()
MainGui_Obj.run_mainGUI()