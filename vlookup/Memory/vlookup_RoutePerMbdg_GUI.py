from tkinter import *
from vlookup.run_vlookup import vlookup

class vlookupMem_RoutrPerMbdg_Gui:
    def __init__(self,rootframe):
        self.rootframe = rootframe

        self.Mem_RouteMBDG_frame = LabelFrame(self.rootframe, text="Route Per MBDG",labelanchor="n")
        self.Mem_RouteMBDG_frame.grid(row=1,column=0,pady=10)


        #------------------------First Sheet Gui-----------------------# 
        self.Mem_RouteMBDG_frame_sheet1 = LabelFrame(self.Mem_RouteMBDG_frame,text="First Sheet(Vlookup Table)",labelanchor="n")
        self.Mem_RouteMBDG_frame_sheet1.grid(row=0,column=0,padx=5,pady=5)

        self.shee1_label = Label(self.Mem_RouteMBDG_frame_sheet1,text="Sheet:").grid(row=0,column=0,padx=3,pady=3)

        # self.Sheet1_drop_list = []
        self.Sheet1_options = [ "Pin_Net", 
                            "Netlist",
                            "BOM",
                            "NetWidth",
                            "Layer_Stackup",
                            "MEMORY",
                            "XGMI",
                            "PCIe",
                            "SATA",
                            "MISC",
                            "USB",
                            "CLK"]

        #Drop Down Boxes
        self.Sheet1_clicked = StringVar()
        self.Sheet1_clicked.set(self.Sheet1_options[5])
        # self.Sheet1_drop_list.append(self.Sheet1_clicked)

        self.Sheet1_drop = OptionMenu(self.Mem_RouteMBDG_frame_sheet1,self.Sheet1_clicked,*self.Sheet1_options)
        self.Sheet1_drop.grid(row=0,column=1,padx=5,pady=5)

        self.sheet1_lkupTbl_Col = Label(self.Mem_RouteMBDG_frame_sheet1,text="Vlookup Layer\nName Col").grid(row=1,column=0,padx=5,pady=5,sticky="n")
        self.sheet1_lkupTbl_Col_Entry = Entry(self.Mem_RouteMBDG_frame_sheet1,borderwidth=3,width=10,fg="black",background="white")
        self.sheet1_lkupTbl_Col_Entry.grid(row=1,column=1,padx=2,pady=2)

        #------------------------Second Sheet Gui-----------------------# 
        self.Mem_RouteMBDG_sheet2 = LabelFrame(self.Mem_RouteMBDG_frame,text="Second Sheet(Vlookup value)",labelanchor="n")
        self.Mem_RouteMBDG_sheet2.grid(row=0,column=1,padx=5,pady=5)

        # Drop down Sheet
        self.shee2_label = Label(self.Mem_RouteMBDG_sheet2,text="Sheet:").grid(row=0,column=0)
        self.Sheet2_options = [ "Pin_Net", 
                            "Netlist",
                            "BOM",
                            "NetWidth",
                            "Layer_Stackup",
                            "MEMORY",
                            "XGMI",
                            "PCIe",
                            "SATA",
                            "MISC",
                            "USB",
                            "CLK"]

        self.Sheet2_clicked = StringVar()
        self.Sheet2_clicked.set(self.Sheet2_options[5])

        self.Sheet2_drop = OptionMenu(self.Mem_RouteMBDG_sheet2,self.Sheet2_clicked,*self.Sheet2_options)
        self.Sheet2_drop.grid(row=0,column=1)

        #LayerName input entry
        self.sheet2_Mem_RouteMBDG_col_label = Label(self.Mem_RouteMBDG_sheet2,text="Vlookup Route\nLayer Value Col").grid(row=1,column=0,sticky="n")
        self.sheet2_vlookup_Mem_RouteMBDG_col_entry = Entry(self.Mem_RouteMBDG_sheet2,border=3,width=10,fg="black",background="white")
        self.sheet2_vlookup_Mem_RouteMBDG_col_entry.grid(row=1,column=1,padx=3)

        # Layer Name Result Col insert input entry
        self.sheet2_Mem_RouteMBDG_result_Col_label = Label(self.Mem_RouteMBDG_sheet2,text="Route Per MBDG \nOutput Insert Col").grid(row=2,column=0,padx=3,sticky="n")
        self.sheet2_Mem_RouteMBDG_result_insert_col_Entry = Entry(self.Mem_RouteMBDG_sheet2,border=3,width=10,fg="black",background="white")
        self.sheet2_Mem_RouteMBDG_result_insert_col_Entry.grid(row=2,column=1,padx=3)

        # Layer Name Header input entry
        self.sheet2_Mem_RouteMBDG_header_label = Label(self.Mem_RouteMBDG_sheet2,text="Header").grid(row=3,column=0,padx=3,sticky="n")
        self.sheet2_Mem_RouteMBDG_header_entry = Entry(self.Mem_RouteMBDG_sheet2,border=5,width=10,fg="black",background="white")
        self.sheet2_Mem_RouteMBDG_header_entry.grid(row=3,column=1,padx=3)

        #Set Default input
        self.sheet1_lkupTbl_Col_Entry.insert(0,"G")
        self.sheet2_vlookup_Mem_RouteMBDG_col_entry.insert(0,"O")
        self.sheet2_Mem_RouteMBDG_result_insert_col_Entry.insert(0,"P")
        self.sheet2_Mem_RouteMBDG_header_entry.insert(0,"Route Per MBDG")

    def run_vlookup_RoutePerMbdg(self,fileName):
        self.fileName = fileName
        vlookup(filename= self.fileName,
                sheet1=self.Sheet1_clicked.get(),
                sheet2= self.Sheet2_clicked.get(),
                lookup_Tbl_column = self.sheet1_lkupTbl_Col_Entry.get(),
                header= self.sheet2_Mem_RouteMBDG_header_entry.get(),
                lookup_val_col = self.sheet2_vlookup_Mem_RouteMBDG_col_entry.get(),
                lookup_out_insert = self.sheet2_Mem_RouteMBDG_result_insert_col_Entry.get()).vlookup_RoutePerMbdg()
        

