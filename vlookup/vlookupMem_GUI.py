from tkinter import *
from vlookup.Memory.vlookup_LyrStackup_GUI import vlookup_LyrStackup_Gui
from vlookup.Memory.vlookup_NetName_GUI import vlookup_NetName_Gui
from vlookup.Memory.vlookup_RoutLyr_TtlLength_Gui import vlookup_RoutLyr_TtlLength_Gui
from vlookup.Memory.vlookup_RoutePerMbdg_GUI import vlookupMem_RoutrPerMbdg_Gui
from vlookup.Memory.vlookupMem_BreakOutLgth_GUI import vlookupMem_BreakOutLgth_Gui
from vlookup.Memory.vlookup_Impedance_GUI import vlookupMem_Impedance_Gui
from vlookup.CheckMinMax.Create_Channel_LayerTable import ChannelLayerName_Table_Gui
from vlookup.CheckMinMax.vlookup_BoMinMax_GUI import vlookup_Bo_MinMax_Gui


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


        self.Mem_LyrStackup_Frame = LabelFrame(self.frame,text="MEMORY CPU0",labelanchor="n")
        self.Mem_LyrStackup_Frame.grid(row=0,column=0)

        self.MemCpu0_Frame = LabelFrame(self.frame,text="MEMORY CPU0",labelanchor="n")
        self.MemCpu0_Frame.grid(row=1,column=0,pady=15,padx=60)

        self.MemCpu1_Frame = LabelFrame(self.frame,text="MEMORY CPU1",labelanchor="n")
        self.MemCpu1_Frame.grid(row=2,column=0,pady=15)

        #---------------------------CPU0 Memory GUI Object--------------------------#
        self.vlookup_MemCpu0_LyrStackup_Gui_obj = vlookup_LyrStackup_Gui(
                                                rootframe = self.Mem_LyrStackup_Frame,
                                                first_sheet = 4,
                                                tabel_col= "A",
                                                result_col= "B",
                                                second_sheet = 5,
                                                insert_col= "G",
                                                insert_row= "2")
        self.vlookup_MemCpu0_NetName_Gui_obj =vlookup_NetName_Gui(
                                            rootframe = self.MemCpu0_Frame,
                                            first_sheet = 0,
                                            tabel_col= "C",
                                            result_col= "D",
                                            second_sheet = 5,
                                            value_col = "M",
                                            insert_col= "N",
                                            header= "NetName")
        self.vlookup_MemCpu0_RoutLyr_TtlLength_Gui_obj = vlookup_RoutLyr_TtlLength_Gui(
                                                        rootframe = self.MemCpu0_Frame,
                                                        first_sheet = 3,
                                                        tabel_col= "A",
                                                        RouteLayer_result_col = "E",
                                                        totalLength_result_col = "F",
                                                        second_sheet = 5,
                                                        value_col = "N",
                                                        LayerName_insert_col = "O",
                                                        TotalLength_insert_col = "R",
                                                        LayerName_header = "Routing Layer",
                                                        TotalLength_header = "Total Length")
        self.vlookup_MemCpu0_RoutrPerMbdg_Gui_obj = vlookupMem_RoutrPerMbdg_Gui(
                                                    rootframe = self.MemCpu0_Frame,
                                                    first_sheet = 5,
                                                    tabel_col= "G",
                                                    second_sheet = 5,
                                                    value_col = "O",
                                                    insert_col= "P",
                                                    header= "Route Per MBDG")
        self.vlookup_MemCpu0__BreakOutLgth_Gui_obj = vlookupMem_BreakOutLgth_Gui(
                                                    rootframe = self.MemCpu0_Frame,
                                                    first_sheet = 3,
                                                    NetName_table_col = "A",
                                                    LineWidth_tabel_col = "B",
                                                    result_col= "G",
                                                    second_sheet = 5,
                                                    value_col = "N",
                                                    insert_col= "Q",
                                                    header= "Breakout Length")
        self.vlookup_MemCpu0_Impedance_Gui_obj = vlookupMem_Impedance_Gui(
                                                rootframe = self.MemCpu0_Frame,
                                                first_sheet = 5,
                                                tabel_col= "F",
                                                second_sheet = 5,
                                                NetName_value_col = "N",
                                                TotalLength_value_col = "R",
                                                insert_col= "S",
                                                header= "Impedance")
        #---------------------------CPU1 Memory GUI Object--------------------------#
        self.vlookup_MemCpu1_NetName_Gui_obj =vlookup_NetName_Gui(
                                                rootframe = self.MemCpu1_Frame,
                                                first_sheet = 0,
                                                tabel_col= "C",
                                                result_col= "D",
                                                second_sheet = 5,
                                                value_col = "U",
                                                insert_col= "V",
                                                header= "NetName")
        self.vlookup_MemCpu1_RoutLyr_TtlLength_Gui_obj = vlookup_RoutLyr_TtlLength_Gui(
                                                        rootframe = self.MemCpu1_Frame,
                                                        first_sheet = 3,
                                                        tabel_col= "A",
                                                        RouteLayer_result_col = "E",
                                                        totalLength_result_col = "F",
                                                        second_sheet = 5,
                                                        value_col = "V",
                                                        LayerName_insert_col = "W",
                                                        TotalLength_insert_col = "Z",
                                                        LayerName_header = "Routing Layer",
                                                        TotalLength_header = "Total Length")
        self.vlookup_MemCpu1_RoutrPerMbdg_Gui_obj = vlookupMem_RoutrPerMbdg_Gui(
                                                rootframe = self.MemCpu1_Frame,
                                                first_sheet = 5,
                                                tabel_col= "G",
                                                second_sheet = 5,
                                                value_col = "W",
                                                insert_col= "X",
                                                header= "Route Per MBDG")
        self.vlookup_MemCpu1__BreakOutLgth_Gui_obj = vlookupMem_BreakOutLgth_Gui(
                                                    rootframe = self.MemCpu1_Frame,
                                                    first_sheet = 3,
                                                    NetName_table_col = "A",
                                                    LineWidth_tabel_col = "B",
                                                    result_col= "G",
                                                    second_sheet = 5,
                                                    value_col = "V",
                                                    insert_col= "Y",
                                                    header= "Breakout Length")
        self.vlookup_MemCpu1_Impedance_Gui_obj = vlookupMem_Impedance_Gui(
                                                rootframe = self.MemCpu1_Frame,
                                                first_sheet = 5,
                                                tabel_col= "F",
                                                second_sheet = 5,
                                                NetName_value_col = "V",
                                                TotalLength_value_col = "Z",
                                                insert_col= "AA",
                                                header= "Impedance")
        #-------------------------CPU0 Check Breakout Min/Max Value-----------------------#
        self.vlookup_MemCpu0_ChlLyrTbl_Gui_obj = ChannelLayerName_Table_Gui(
                                                rootframe = self.MemCpu0_Frame,
                                                first_sheet = 4,
                                                tabel_col= "A",
                                                result_col= "B",
                                                second_sheet = 5,
                                                insert_col_ChlNm= "F",
                                                insert_col_LyrNm= "G",
                                                insert_row= "19")
        self.vlookup_MemCpu0_BoMinMax_Gui_obj = vlookup_Bo_MinMax_Gui(
                                                rootframe = self.MemCpu0_Frame,
                                                first_sheet = 5,
                                                tabel_col= "O",
                                                result_col="Q",
                                                second_sheet = 5,
                                                value_col = "G",
                                                Min_insert_col= "I",
                                                Max_insert_col="J",
                                                insert_row= 19,
                                                Min_header= "BO Length Min(mils/mm)",
                                                Max_header = "BO Length Max(mils/mm)")

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

    #---------------------------CPU0 Memory method--------------------------#
    def run_MemCpu0_LyrStackup_Tbl_vlookup(self):
        self.vlookup_MemCpu0_LyrStackup_Gui_obj.run_LyrStackup_Tbl_vlookup(self.fileName)

    def run_MemCpu0_vlookup_Netnm(self):
        self.vlookup_MemCpu0_NetName_Gui_obj.run_vlookup_NetName(self.fileName)

    def run_MemCpu0_vlookup_RoutLyr(self):
        self.vlookup_MemCpu0_RoutLyr_TtlLength_Gui_obj.run_vlookup_RoutLyr(self.fileName)

    def run_MemCpu0_vlookup_TtlLgth(self):
        self.vlookup_MemCpu0_RoutLyr_TtlLength_Gui_obj.run_vlookup_TtlLgth(self.fileName)

    def run_MemCpu0_vlookup_RoutePerMbdg(self):
        self.vlookup_MemCpu0_RoutrPerMbdg_Gui_obj.run_vlookup_RoutePerMbdg(self.fileName)

    def run_MemCpu0_vlookup_BoLength(self):
        self.vlookup_MemCpu0__BreakOutLgth_Gui_obj.run_vlookup_BoLength(self.fileName)

    def run_MemCpu0_vlookup_Impedance(self):
        self.vlookup_MemCpu0_Impedance_Gui_obj.run_vlookup_Impedance(self.fileName)

    #---------------------------CPU1 Check Breakout Min/Max Value--------------------------#
    def run_MemCpu0_ChlLyrTbl_vlookup(self):
        self.vlookup_MemCpu0_ChlLyrTbl_Gui_obj.run_CreateChllNmTbl(self.fileName)
        self.vlookup_MemCpu0_ChlLyrTbl_Gui_obj.run_ChlLyrTbl_vlookup(self.fileName)

    def run_MemCpu0_BoMinMax_vlookup(self):
        self.vlookup_MemCpu0_BoMinMax_Gui_obj.run_vlookup_BoMinMax(self.fileName)

    #---------------------------CPU1 Memory method--------------------------#
    def run_MemCpu1_vlookup_Netnm(self):
        self.vlookup_MemCpu1_NetName_Gui_obj.run_vlookup_NetName(self.fileName)

    def run_MemCpu1_vlookup_RoutLyr(self):
        self.vlookup_MemCpu1_RoutLyr_TtlLength_Gui_obj.run_vlookup_RoutLyr(self.fileName)

    def run_MemCpu1_vlookup_TtlLgth(self):
        self.vlookup_MemCpu1_RoutLyr_TtlLength_Gui_obj.run_vlookup_TtlLgth(self.fileName)

    def run_MemCpu1_vlookup_RoutePerMbdg(self):
        self.vlookup_MemCpu1_RoutrPerMbdg_Gui_obj.run_vlookup_RoutePerMbdg(self.fileName)

    def run_MemCpu1_vlookup_BoLength(self):
        self.vlookup_MemCpu1__BreakOutLgth_Gui_obj.run_vlookup_BoLength(self.fileName)

    def run_MemCpu1_vlookup_Impedance(self):
        self.vlookup_MemCpu1_Impedance_Gui_obj.run_vlookup_Impedance(self.fileName)
