from tkinter import *
from vlookup.run_vlookup import vlookup

class vlookupMem_BreakOutLgth_Gui:
    def __init__(self,rootframe, fileName):
        self.rootframe = rootframe
        self.fileName = fileName

        self.Mem_BO_Lgth_frame = LabelFrame(self.rootframe, text="Breakout length",labelanchor="n")
        self.Mem_BO_Lgth_frame.grid(row=3,column=1,padx=10,pady=10)

        #------------------------First Sheet Gui-----------------------# 
        self.Mem_BO_Lgth_sheet1 = LabelFrame(self.Mem_BO_Lgth_frame,text="First Sheet (As a Lookup Table)",labelanchor="n")
        self.Mem_BO_Lgth_sheet1.grid(row=0,column=0,padx=5,pady=5)

        self.shee1_label = Label(self.Mem_BO_Lgth_sheet1,text="Sheet:").grid(row=0,column=0,padx=3,pady=3)

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
        self.Sheet1_clicked.set(self.Sheet1_options[3])
        # self.Sheet1_drop_list.append(self.Sheet1_clicked)

        self.Sheet1_drop = OptionMenu(self.Mem_BO_Lgth_sheet1,self.Sheet1_clicked,*self.Sheet1_options)
        self.Sheet1_drop.grid(row=1,column=0,padx=5,pady=5)

        self.sheet1_BO_Lgth_Col = Label(self.Mem_BO_Lgth_sheet1,text="Vlookup \nNetName Col").grid(row=0,column=1,padx=5,pady=5,sticky="n")
        self.sheet1_lkupTbl_NetName_Col_Entry = Entry(self.Mem_BO_Lgth_sheet1,borderwidth=3,width=4,fg="black",background="white")
        self.sheet1_lkupTbl_NetName_Col_Entry.grid(row=1,column=1,padx=2,pady=2)

        self.sheet1_BO_Lgth_Col = Label(self.Mem_BO_Lgth_sheet1,text="Vlookup Line\nWidth Col").grid(row=0,column=2,padx=5,pady=5,sticky="n")
        self.sheet1_lkupTbl_LineWdt_Col_Entry = Entry(self.Mem_BO_Lgth_sheet1,borderwidth=3,width=4,fg="black",background="white")
        self.sheet1_lkupTbl_LineWdt_Col_Entry.grid(row=1,column=2,padx=2,pady=2)

        self.sheet1_result_Col_Label = Label(self.Mem_BO_Lgth_sheet1,text="Result\nCol").grid(row=0,column=3,padx=5,pady=5,sticky="n")
        self.sheet1_lkupTbl_result_Entry = Entry(self.Mem_BO_Lgth_sheet1,borderwidth=3,width=4,fg="black", background="white")
        self.sheet1_lkupTbl_result_Entry.grid(row=1,column=3,padx=2,pady=2)

        # ------------------------Second Sheet Gui-----------------------# 
        self.Mem_BO_Lgth_sheet2 = LabelFrame(self.Mem_BO_Lgth_frame,text="Second Sheet (As a Lookup value)",labelanchor="n")
        self.Mem_BO_Lgth_sheet2.grid(row=0,column=1,padx=5,pady=5)

        # Drop down Mem_BO_Lgth_sheet2
        self.shee2_label = Label(self.Mem_BO_Lgth_sheet2,text="Sheet:").grid(row=0,column=0)
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

        self.Sheet2_drop = OptionMenu(self.Mem_BO_Lgth_sheet2,self.Sheet2_clicked,*self.Sheet2_options)
        self.Sheet2_drop.grid(row=1,column=0)

        #LayerName input entry
        self.sheet2_BO_Lgth_col_label = Label(self.Mem_BO_Lgth_sheet2,text="Vlookup\nValue Col").grid(row=0,column=1,sticky="n")
        self.sheet2_BO_Lgth_col_entry = Entry(self.Mem_BO_Lgth_sheet2,border=3,width=4,fg="black",background="white")
        self.sheet2_BO_Lgth_col_entry.grid(row=1,column=1)

        # Result Col insert input entry
        self.sheet2_lkup_result_Col = Label(self.Mem_BO_Lgth_sheet2,text="Result\nCol Insert").grid(row=0,column=7,sticky="n")
        self.sheet2_result_insert_col_Entry = Entry(self.Mem_BO_Lgth_sheet2,border=3,width=4,fg="black",background="white")
        self.sheet2_result_insert_col_Entry.grid(row=1,column=7)

        # Header input entry
        self.sheet2_header_label = Label(self.Mem_BO_Lgth_sheet2,text="Header").grid(row=0,column=8,sticky="n")
        self.sheet2_header_entry = Entry(self.Mem_BO_Lgth_sheet2,border=5,width=10,fg="black",background="white")
        self.sheet2_header_entry.grid(row=1,column=8)

        #Set Default input
        self.sheet1_lkupTbl_NetName_Col_Entry.insert(0,"A")
        self.sheet1_lkupTbl_LineWdt_Col_Entry.insert(0,"B")
        self.sheet1_lkupTbl_result_Entry.insert(0,"G")
        self.sheet2_BO_Lgth_col_entry.insert(0,"N")
        self.sheet2_result_insert_col_Entry.insert(0,"R")
        self.sheet2_header_entry.insert(0,"Breakout Length")

    def run_vlookup_Mem_BoLength(self):
        vlookup(filename= self.fileName,
                sheet1=self.Sheet1_clicked.get(),
                sheet2= self.Sheet2_clicked.get(),
                lookup_Tbl_column = self.sheet1_lkupTbl_NetName_Col_Entry.get(),
                lookup_Tbl_col_LineWdt = self.sheet1_lkupTbl_LineWdt_Col_Entry.get(),
                lookup_Tbl_output = self.sheet1_lkupTbl_result_Entry.get(),
                lookup_val_col = self.sheet2_BO_Lgth_col_entry.get(),
                lookup_out_insert = self.sheet2_result_insert_col_Entry.get(),
                header= self.sheet2_header_entry.get()).vlookup_BreakoutLength()

