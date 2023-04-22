from Background_GUI_Tool import *
from tkinter import *
from HtmlDataExtraction import *
from tkinter import filedialog


class mainGUI:
    def __init__(self):
        Background_GUI()
        self.main_Gui_root = Tk()
        self.main_Gui_root.title("Main screen")
        self.ReportFile_Frame = LabelFrame(self.main_Gui_root,text="Report Files Input",labelanchor="n")
        self.ReportFile_Frame.grid(row=0,column=1,columnspan=3,padx=10,pady=10)
        self.main_Gui_root.protocol("WM_DELETE_WINDOW",self.pressExit)

        #-------------------tkinder GUI: Reference Designator-------------------------#
        self.RefDesignator = LabelFrame(self.main_Gui_root, text="Reference Designator",padx=10, pady=10,labelanchor='n')
        self.RefDesignator.grid(padx=10,pady=10,row=0,column=0,rowspan=2)

        self.CPU0_Label = Label(self.RefDesignator,text="CPU0:")
        self.CPU0_Label.grid(row=0,column=0,sticky='w',pady=20)
        self.CPU0_input_entry = Entry(self.RefDesignator,width=5,background='white',fg="black",borderwidth=3)
        self.CPU0_input_entry.grid(row=0, column=1)

        self.CPU1_Label = Label(self.RefDesignator,text="CPU1:")
        self.CPU1_Label.grid(row=1,column=0,sticky='w',pady=20)
        self.CPU1_input_entry = Entry(self.RefDesignator,width=5,background='white',fg="black",borderwidth=3)
        self.CPU1_input_entry.grid(row=1, column=1)

        self.UsbHub_Label = Label(self.RefDesignator,text="USB HUB:")
        self.UsbHub_Label.grid(row=2,column=0,sticky='w',pady=20)
        self.UsbHub_input_entry = Entry(self.RefDesignator,width=5,background='white',fg="black",borderwidth=3)
        self.UsbHub_input_entry.grid(row=2, column=1)

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

        self.NetPin_main_browser_button = Button(self.ReportFile_Frame , text="Browse",command=self.NetPin_main_browse_file)
        self.NetPin_main_browser_button.grid(row=0, column=2,padx=15,pady=15)

        #--------------------Netlist tkinder GUI------------------------------------#
        # create a label for the input field
        self.Netlist_main_input_label = Label(self.ReportFile_Frame, text="Netlist File:")
        self.Netlist_main_input_label.grid(row=1, column=0,padx=15,pady=15)
    
        self.Netlist_main_input_entry = Entry(self.ReportFile_Frame ,width=70,background='white',fg="black",borderwidth=3)
        self.Netlist_main_input_entry.grid(row=1,column=1,padx=15,pady=15)

        self.Netlist_main_browser_button = Button(self.ReportFile_Frame , text="Browse",command=self.Netlist_main_browse_file)
        self.Netlist_main_browser_button.grid(row=1, column=2,padx=15,pady=15)

        #--------------------BOM tkinder GUI------------------------------------#
        # create a label for the input field
        self.BOM_main_input_label = Label(self.ReportFile_Frame, text="BOM File:")
        self.BOM_main_input_label.grid(row=2, column=0,padx=15,pady=15)
    
        self.BOM_main_input_entry = Entry(self.ReportFile_Frame ,width=70,background='white',fg="black",borderwidth=3)
        self.BOM_main_input_entry.grid(row=2,column=1,padx=15,pady=15)

        self.BOM_main_browser_button = Button(self.ReportFile_Frame , text="Browse",command=self.BOM_main_browse_file)
        self.BOM_main_browser_button.grid(row=2, column=2,padx=15,pady=15)

        #--------------------LenWidLayer tkinder GUI------------------------------------#
        # create a label for the input field
        self.LenWidLayer_main_input_label = Label(self.ReportFile_Frame, text="Length Width Layer File:")
        self.LenWidLayer_main_input_label.grid(row=3, column=0,padx=15,pady=15)
    
        self.LenWidLayer_main_input_entry = Entry(self.ReportFile_Frame ,width=70,background='white',fg="black",borderwidth=3)
        self.LenWidLayer_main_input_entry.grid(row=3,column=1,padx=15,pady=15)

        self.LenWidLayer_main_browser_button = Button(self.ReportFile_Frame , text="Browse",command=self.LenWidLayer_main_browse_file)
        self.LenWidLayer_main_browser_button.grid(row=3, column=2,padx=15,pady=15)

        #--------------------Layer Stackup tkinder GUI------------------------------------#
        # create a label for the input field
        self.LayerStackup_main_input_label = Label(self.ReportFile_Frame, text="Layer Stackup File:")
        self.LayerStackup_main_input_label.grid(row=4, column=0,padx=15,pady=15)
    
        self.LayerStackup_main_input_entry = Entry(self.ReportFile_Frame ,width=70,background='white',fg="black",borderwidth=3)
        self.LayerStackup_main_input_entry.grid(row=4,column=1,padx=15,pady=15)

        self.LayerStackup_main_browser_button = Button(self.ReportFile_Frame , text="Browse",command=self.LenWidLayer_main_browse_file)
        self.LayerStackup_main_browser_button.grid(row=4, column=2,padx=15,pady=15)

        #--------------------Memory, PCIe, XGMI, USB, SATA , MISC label and Checkbox-----------------#
        # Create a list of tuples that contains the text and values of the check buttons
        self.mainGUI_check_options = [("Memory", "mainGUI_Checkbox_option1"), 
                            ("PCIe", "mainGUI_Checkbox_option2"),
                            ("XGMI", "mainGUI_Checkbox_option3"),
                            ("USB", "mainGUI_Checkbox_option4"),
                            ("SATA", "mainGUI_Checkbox_option5"),
                            ("MISC", "mainGUI_Checkbox_option6")]

        # Create a list of IntVar variables to store the selected check button values
        self.mainGUI_vars = []
        for self.option in self.mainGUI_check_options:
            self.var = StringVar()
            self.mainGUI_vars.append(self.var)

        # Use a for loop to create the check buttons
        for i, (text, value) in enumerate(self.mainGUI_check_options):
            self.mainGUI_check_button = Checkbutton(self.main_Gui_root, text=text, variable=self.mainGUI_vars[i], onvalue=value, offvalue=0, font=("Arial",20))
            if i < 3:
                self.mainGUI_check_button.grid(row=1, padx=20,pady=20,column=i+1,sticky="w")
                self.mainGUI_check_button.deselect()
            else:
                self.mainGUI_check_button.grid(row=2, padx=20,pady=20,column=i+1-3,sticky="w")
                self.mainGUI_check_button.deselect()

        #-------------------Show Development Tool and Exit Button-------------------------------#
        # self.presshow = Button(self.main_Gui_root, text="Close Development Tool",command=self.hidebackground)
        # self.presshow.grid(row=5,column=1)

        self.presshow = Button(self.main_Gui_root, text="Development Tool",command=self.showBack)
        self.presshow.grid(row=3,column=1,pady=20)

        self.pressexit = Button(self.main_Gui_root, text="Exit",command=self.pressExit)
        self.pressexit.grid(row=3,column=3,pady=20)

        #-------------------Create the export button--------------------------#
        self.export_button = Button(self.main_Gui_root, text="Generate Report", command=export_report)
        self.export_button.grid(row=3,column=2,pady=20)

    #---------------------NetPin File Browser-----------------------------------
    # create a function to open the file browser and select a file
    def NetPin_main_browse_file(self):
        # Component Pin Report File input:
        self.NetPin_main_file_path = filedialog.askopenfilename(initialdir="/Users/yeamboonkai/Desktop/AMD_Project/Input", 
                                            title="Select a File", 
                                            filetypes=(("htm", "*.htm"), ("All files", "*.*")))
        self.NetPin_main_input_entry.delete(0, END)
        self.NetPin_main_input_entry.insert(0, self.NetPin_main_file_path)

        # Update background input
        NetPin_Gui_obj.NetPin_input_entry.delete(0,END)
        NetPin_Gui_obj.NetPin_input_entry.insert(0,self.NetPin_main_file_path)

        # Update Background NetPin directory path label
        NetPin_Gui_obj.NetPin_file_path_label.config(text=self.NetPin_main_file_path)

    #---------------------Netlist Browse File-----------------------------------
    # create a function to open the file browser and select a file
    def Netlist_main_browse_file(self):
        # Component Pin Report File input:
        self.Netlist_main_file_path = filedialog.askopenfilename(initialdir="/Users/yeamboonkai/Desktop/AMD_Project/Input", 
                                            title="Select a File", 
                                            filetypes=(("htm", "*.htm"), ("All files", "*.*")))
        self.Netlist_main_input_entry.delete(0, END)
        self.Netlist_main_input_entry.insert(0, self.Netlist_main_file_path)

        # Update background input
        Netlist_Gui_obj.Netlist_input_entry.delete(0,END)
        Netlist_Gui_obj.Netlist_input_entry.insert(0,self.Netlist_main_file_path)

        # Update Background Netlist directory path label
        Netlist_Gui_obj.Netlist_file_path_label.config(text=self.Netlist_main_file_path)

    #---------------------BOM Browse File-----------------------------------
    # create a function to open the file browser and select a file
    def BOM_main_browse_file(self):
        # Component Pin Report File input:
        self.BOM_main_file_path = filedialog.askopenfilename(initialdir="/Users/yeamboonkai/Desktop/AMD_Project/Input", 
                                            title="Select a File", 
                                            filetypes=(("htm", "*.htm"), ("All files", "*.*")))
        self.BOM_main_input_entry.delete(0, END)
        self.BOM_main_input_entry.insert(0, self.BOM_main_file_path)

        # Update background input
        BOM_Gui_obj.BOM_input_entry.delete(0,END)
        BOM_Gui_obj.BOM_input_entry.insert(0,self.BOM_main_file_path)

        # Update Background BOM directory path label
        BOM_Gui_obj.BOM_file_path_label.config(text=self.BOM_main_file_path)

    #---------------------Length Width Layer Browse File-----------------------------------
    # create a function to open the file browser and select a file
    def LenWidLayer_main_browse_file(self):
        # Component Pin Report File input:
        self.LenWidLayer_main_file_path = filedialog.askopenfilename(initialdir="/Users/yeamboonkai/Desktop/AMD_Project/Input", 
                                            title="Select a File", 
                                            filetypes=(("htm", "*.htm"), ("All files", "*.*")))
        self.LenWidLayer_main_input_entry.delete(0, END)
        self.LenWidLayer_main_input_entry.insert(0, self.LenWidLayer_main_file_path)

        # Update background input
        LenWidLayer_Gui_obj.LenWidLayer_input_entry.delete(0,END)
        LenWidLayer_Gui_obj.LenWidLayer_input_entry.insert(0,self.LenWidLayer_main_file_path)

        # Update Background Length Width Layer directory path label
        LenWidLayer_Gui_obj.LenWidLayer_file_path_label.config(text=self.LenWidLayer_main_file_path)

    def pressExit(self):
        BackGui_root.destroy()
        self.main_Gui_root.destroy()

    def showBack(self):
        BackGui_root.deiconify()

    # def hidebackground(self):
    #     BackGui_root.withdraw()

    def run_mainGUI(self):
        self.main_Gui_root.mainloop()

MainGui_Obj = mainGUI()
MainGui_Obj.run_mainGUI()