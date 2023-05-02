from tkinter import *
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

BackGui_root = Tk()
#---------------------Create the Notebook widget------------------------#
notebook = ttk.Notebook(BackGui_root)

# Create the first tab
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text='HTML Data Extraction')
notebook.grid(columnspan=2)

# Create the second tab
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text='Data Concatenation')
notebook.grid()

# Create the third tab
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text='REFDES')
notebook.grid()

# Create the fourth tab
tab4 = ttk.Frame(notebook)
notebook.add(tab4, text='Vlookup Table')
notebook.grid()

NetPin_Gui_obj = NetPin_Gui()
Netlist_Gui_obj = Netlist_Gui()
BOM_Gui_obj = BOM_Gui()
LenWidLayer_Gui_obj = LenWidLaper_Gui()
DataConcat_Gui_obj = DataConcat_Gui()
RefDesignator_Gui_obj = RefDesignator_Gui()

class Background_GUI:
    def __init__(self):
        BackGui_root.title("Development Tool")
        BackGui_root.protocol("WM_DELETE_WINDOW",BackGui_root.withdraw)

        BackGui_root.withdraw()

    def export_report(self):
        input_check = {}
        input_check["Netpin"] = NetPin_Gui_obj.NetPin_input_entry.get()
        input_check["Netlist"] = Netlist_Gui_obj.Netlist_input_entry.get()
        input_check["BOM"] = BOM_Gui_obj.BOM_input_entry.get()
        input_check["Layer Stackup"] = LenWidLayer_Gui_obj.LenWidLayer_input_entry.get()
        if all(value for value in input_check.values()):
            # load workbook
            #----------------Create New Report Workbook---------------#
            Date_Time=datetime.now().strftime('%Y-%m-%d %H%M%S')
            global y
            # y =str("Design Connectivity Checker_"+Date_Time)+'.'+'xlsx'
            y =str(Date_Time)+'.'+'xlsx'

            global sheet1, sheet2,sheet3,sheet4,workbook

            # Create a new workbook
            workbook = openpyxl.Workbook()

            # Remove the default Sheet
            default_sheet = workbook['Sheet']
            workbook.remove(default_sheet)

            # Create a new sheet
            sheet1 = workbook.create_sheet('Pin_Net')
            sheet2 = workbook.create_sheet('Netlist')
            sheet3 = workbook.create_sheet('BOM')
            sheet4 = workbook.create_sheet('NetWidth')
            #---------------------------------------------------------#

            NetPin_Gui_obj.NetPinOutputData()
            Netlist_Gui_obj.NetlistOutputData()
            BOM_Gui_obj.BomOutputData()
            LenWidLayer_Gui_obj.LenWidLayerOutputData()

            # Save the workbook
            workbook.save(y)

            DataConcat_Gui_obj.DataConcat_Execute()
            RefDesignator_Gui_obj.copy_InterfaceMmy_data_to_dst()
            RefDesignator_Gui_obj.Run_RefDesign_Concat()
        else:
            for key, val in input_check.items():
                if not val:
                     messagebox.showinfo("Popup!", "The "+ key + " file input cannot be empty\nPlease select " +key+ " html file")

    def hidebackground(self):
        BackGui_root.withdraw()

background = Background_GUI()

#-------------------Create the export button--------------------------#
export_button = Button(BackGui_root, text="Generate Report", command=background.export_report)
export_button.grid(row=4,column=0)

#-------------------Hide, Show,Exit Button-------------------------------#
presshide = Button(BackGui_root, text="Close Development Tool",command= background.hidebackground)
presshide.grid(row=4,column=1)