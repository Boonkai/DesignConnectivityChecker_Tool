from tkinter import *
from vlookup.vlookup_LyrStackup_GUI import vlookup_LyrStackup_Gui
from vlookup.vlookupMem_NetName_GUI import vlookupMem_NetName_Gui
from vlookup.vlookupMem_RoutLyr_TtlLength_Gui import vlookupMem_RoutLyr_TtlLength_Gui
from vlookup.vlookup_RoutePerMbdg_GUI import vlookupMem_RoutrPerMbdg_Gui
from vlookup.vlookupMem_BreakOutLgth_GUI import vlookupMem_BreakOutLgth_Gui
from vlookup.vlookup_Impedance_GUI import vlookupMem_Impedance_Gui


class vlookup_gui:
    def __init__(self,rootframe, fileName):
        self.rootframe = rootframe
        self.fileName = fileName

        # Create a Canvas widget to hold the frame and scrollbar
        self.canvas = Canvas(self.rootframe)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # Create a frame to hold the label and button
        self.frame = Frame(self.canvas)
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.Memoey_Frame = LabelFrame(self.frame,text="MEMORY",labelanchor="n")
        self.Memoey_Frame.grid(row=0,column=0)

        self.vlookup_LyrStackup_Gui_obj = vlookup_LyrStackup_Gui(self.Memoey_Frame)
        self.vlookup_Mem_NetName_Gui_obj =vlookupMem_NetName_Gui(self.Memoey_Frame)
        self.vlookupMem_RoutLyr_TtlLength_Gui_obj = vlookupMem_RoutLyr_TtlLength_Gui(self.Memoey_Frame)
        self.vlookupMem_RoutrPerMbdg_Gui_obj = vlookupMem_RoutrPerMbdg_Gui(self.Memoey_Frame)
        self.vlookupMem_BreakOutLgth_Gui_obj = vlookupMem_BreakOutLgth_Gui(self.Memoey_Frame)
        self.vlookupMem_Impedance_Gui_obj = vlookupMem_Impedance_Gui(self.Memoey_Frame)

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

    def run_LyrStackup_Tbl_vlookup(self):
        self.vlookup_LyrStackup_Gui_obj.run_LyrStackup_Tbl_vlookup(self.fileName)

    def run_vlookup_Mem_Netnm(self):
        self.vlookup_Mem_NetName_Gui_obj.run_vlookup_Mem_Netnm(self.fileName)

    def run_vlookup_Mem_RoutLyr(self):
        self.vlookupMem_RoutLyr_TtlLength_Gui_obj.run_vlookup_Mem_RoutLyr(self.fileName)

    def run_vlookup_Mem_TtlLgth(self):
        self.vlookupMem_RoutLyr_TtlLength_Gui_obj.run_vlookup_Mem_TtlLgth(self.fileName)

    def run_vlookup_RoutePerMbdg(self):
        self.vlookupMem_RoutrPerMbdg_Gui_obj.run_vlookup_RoutePerMbdg(self.fileName)

    def run_vlookup_Mem_BoLength(self):
        self.vlookupMem_BreakOutLgth_Gui_obj.run_vlookup_Mem_BoLength(self.fileName)

    def run_vlookup_Impedance(self):
        self.vlookupMem_Impedance_Gui_obj.run_vlookup_Impedance(self.fileName)

