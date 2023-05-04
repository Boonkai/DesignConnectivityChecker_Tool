from tkinter import ttk
from datetime import datetime
import openpyxl
from tkinter import *
from HtmlDataExtraction.ComponentNetPin_GUI import NetPin_Gui
from HtmlDataExtraction.Netlist_GUI import Netlist_Gui
from HtmlDataExtraction.BOM_GUI import BOM_Gui
from HtmlDataExtraction.LenWidLayer_GUI import LenWidLaper_Gui
from DataConcatenation.DataConcat_GUI import DataConcat_Gui
from RefDesignator.RefDesignator_GUI import RefDesignator_Gui
from tkinter import messagebox

class Background_GUI:
    def __init__(self):
        self.BackGui_root = Tk()
        self.BackGui_root.title("Development Tool")
        self.BackGui_root.protocol("WM_DELETE_WINDOW",self.BackGui_root.withdraw)

        self.BackGui_root.withdraw()

        #---------------------Create the Notebook widget------------------------#
        self.notebook = ttk.Notebook(self.BackGui_root)

        # Create the first tab
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text='HTML Data Extraction')
        self.notebook.grid(columnspan=2)

        # Create the second tab
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text='Data Concatenation')
        self.notebook.grid()

        # Create the third tab
        self.tab3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab3, text='REFDES')
        self.notebook.grid()

        # Create the fourth tab
        self.tab4 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab4, text='Vlookup Table')
        self.notebook.grid()

        #----------------Create New Report Workbook---------------#
        Date_Time=datetime.now().strftime('%Y-%m-%d %H%M%S')
        # y =str("Design Connectivity Checker_"+Date_Time)+'.'+'xlsx'
        self.fileanme =str(Date_Time)+'.'+'xlsx'

        # Create a new workbook
        self.workbook = openpyxl.Workbook()

        # Remove the default Sheet
        default_sheet = self.workbook['Sheet']
        self.workbook.remove(default_sheet)

        # Create a new sheet
        self.sheet1 = self.workbook.create_sheet('Pin_Net')
        self.sheet2 = self.workbook.create_sheet('Netlist')
        self.sheet3 = self. workbook.create_sheet('BOM')
        self.sheet4 = self.workbook.create_sheet('NetWidth')
        #---------------------------------------------------------#
        self.NetPin_Gui_obj = NetPin_Gui(self.tab1,self.sheet1)
        self.Netlist_Gui_obj = Netlist_Gui(self.tab1,self.sheet2)
        self.BOM_Gui_obj = BOM_Gui(self.tab1,self.sheet3)
        self.LenWidLayer_Gui_obj = LenWidLaper_Gui(self.tab1,self.sheet4)
        self.DataConcat_Gui_obj = DataConcat_Gui(self.tab2,self.fileanme)
        self.RefDesignator_Gui_obj = RefDesignator_Gui(self.tab3,self.fileanme)

        #-------------------Create the export button--------------------------#
        export_button = Button(self.BackGui_root,text="Generate Report", command=self.export_report)
        export_button.grid(row=4,column=0)

        #-------------------Hide, Show,Exit Button-------------------------------#
        presshide = Button(self.BackGui_root, text="Close Development Tool",command=self.hidebackground)
        presshide.grid(row=4,column=1)

    def export_report(self):
        self.input_check = {}
        self.input_check["Netpin"] = self.NetPin_Gui_obj.NetPin_input_entry.get()
        self.input_check["Netlist"] = self.Netlist_Gui_obj.Netlist_input_entry.get()
        self.input_check["BOM"] = self.BOM_Gui_obj.BOM_input_entry.get()
        self.input_check["Layer Stackup"] = self.LenWidLayer_Gui_obj.LenWidLayer_input_entry.get()
        if all(value for value in self.input_check.values()):

            self.NetPin_Gui_obj.NetPinOutputData()
            self.Netlist_Gui_obj.NetlistOutputData()
            self.BOM_Gui_obj.BomOutputData()
            self.LenWidLayer_Gui_obj.LenWidLayerOutputData()

            # Save the workbook
            self.workbook.save(self.fileanme)

            self.DataConcat_Gui_obj.DataConcat_Execute()
            self.RefDesignator_Gui_obj.copy_InterfaceMmy_data_to_dst()
            self.RefDesignator_Gui_obj.Run_RefDesign_Concat()
        else:
            for key, val in self.input_check.items():
                if not val:
                     messagebox.showinfo("Popup!", "The "+ key + " file input cannot be empty\nPlease select " +key+ " html file")

    def hidebackground(self):
        self.BackGui_root.withdraw()

