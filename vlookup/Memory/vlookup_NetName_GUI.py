from tkinter import *
from vlookup.run_vlookup import vlookup


class vlookup_NetName_Gui:
    def __init__(self,
                 rootframe,
                 first_sheet,
                 tabel_col,
                 result_col,
                 second_sheet,
                 value_col,
                 insert_col,
                 header):
        self.rootframe = rootframe
        self.first_sheet = first_sheet
        self.tabel_col = tabel_col
        self.result_col = result_col
        self.second_sheet = second_sheet
        self.value_col = value_col
        self.insert_col = insert_col
        self.header = header

        self.Mem_frame = LabelFrame(self.rootframe, text="NetName",labelanchor="n")
        self.Mem_frame.grid(row=0,column=0,padx=60,pady=10)

        #------------------------First Sheet Gui-----------------------# 
        self.Mem_sheet_1 = LabelFrame(self.Mem_frame,text="First Sheet (Vlookup Table)",labelanchor="n")
        self.Mem_sheet_1.grid(row=0,column=0,padx=5,pady=5)

        self.shee1_label = Label(self.Mem_sheet_1,text="Sheet:").grid(row=0,column=0,padx=3,pady=3)

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
        self.Sheet1_clicked.set(self.Sheet1_options[int(self.first_sheet)])
        # self.Sheet1_drop_list.append(self.Sheet1_clicked)

        self.Sheet1_drop = OptionMenu(self.Mem_sheet_1,self.Sheet1_clicked,*self.Sheet1_options)
        self.Sheet1_drop.grid(row=0,column=1,padx=5,pady=5)

        # print(self.Sheet1_clicked.get())

        self.sheet1_lkupTbl_Col = Label(self.Mem_sheet_1,text="Lookup \nTable Col").grid(row=1,column=0,padx=5,pady=5,sticky="n")
        self.sheet1_lkupTbl_Col_Entry = Entry(self.Mem_sheet_1,borderwidth=3,width=10,fg="black",background="white")
        self.sheet1_lkupTbl_Col_Entry.grid(row=1,column=1,padx=2,pady=2)

        self.sheet1_lkupTbl_result_Col = Label(self.Mem_sheet_1,text="Result Col").grid(row=2,column=0,padx=5,pady=5,sticky="n")
        self.sheet1_lkupTbl_result_Entry = Entry(self.Mem_sheet_1,borderwidth=3,width=10,fg="black", background="white")
        self.sheet1_lkupTbl_result_Entry.grid(row=2,column=1,padx=2,pady=2)

        #------------------------Second Sheet Gui-----------------------# 
        self.Mem_sheet_2 = LabelFrame(self.Mem_frame,text="Second Sheet (Vlookup value)",labelanchor="n")
        self.Mem_sheet_2.grid(row=0,column=1,padx=5,pady=5)

        self.shee2_label = Label(self.Mem_sheet_2,text="Sheet:").grid(row=0,column=0,padx=3,pady=3)

        # self.Sheet1_drop_list = []
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

        #Drop Down Boxes
        self.Sheet2_clicked = StringVar()
        self.Sheet2_clicked.set(self.Sheet2_options[int(self.second_sheet)])
        # self.Sheet1_drop_list.append(self.Sheet1_clicked)

        self.Sheet2_drop = OptionMenu(self.Mem_sheet_2,self.Sheet2_clicked,*self.Sheet2_options)
        self.Sheet2_drop.grid(row=0,column=1,padx=3,pady=3)

        # print(self.Sheet2_clicked.get())

        self.sheet2_lkupTbl_Col = Label(self.Mem_sheet_2,text="Lookup\nValue Col").grid(row=1,column=0,padx=5,pady=5,sticky="n")
        self.sheet2_lkup_val_Col_Entry = Entry(self.Mem_sheet_2,border=3,width=10,fg="black",background="white")
        self.sheet2_lkup_val_Col_Entry.grid(row=1,column=1,padx=3,pady=3)

        self.sheet2_lkup_result_Col = Label(self.Mem_sheet_2,text="Result\nInsert Col").grid(row=2,column=0,padx=5,pady=5,sticky="n")
        self.sheet2_result_insert_col_Entry = Entry(self.Mem_sheet_2,border=3,width=10,fg="black",background="white")
        self.sheet2_result_insert_col_Entry.grid(row=2,column=1,padx=3,pady=3)

        self.sheet2_header_label = Label(self.Mem_sheet_2,text="Header").grid(row=3,column=0,padx=5,pady=5,sticky="n")
        self.sheet2_header_entry = Entry(self.Mem_sheet_2,border=3,width=10,fg="black",background="white")
        self.sheet2_header_entry.grid(row=3,column=1,padx=3,pady=3)

        #Set Default input
        self.sheet1_lkupTbl_Col_Entry.insert(0,str(self.tabel_col))
        self.sheet1_lkupTbl_result_Entry.insert(0,str(self.result_col))
        self.sheet2_lkup_val_Col_Entry.insert(0,str(value_col))
        self.sheet2_result_insert_col_Entry.insert(0,str(insert_col))
        self.sheet2_header_entry.insert(0,str(self.header))

    def run_vlookup_NetName(self,fileName):
        self.fileName = fileName
        vlookup(filename= self.fileName,
                sheet1=self.Sheet1_clicked.get(),
                sheet2= self.Sheet2_clicked.get(),
                lookup_Tbl_column = self.sheet1_lkupTbl_Col_Entry.get(),
                lookup_Tbl_output = self.sheet1_lkupTbl_result_Entry.get(),
                lookup_val_col = self.sheet2_lkup_val_Col_Entry.get(),
                lookup_out_insert = self.sheet2_result_insert_col_Entry.get(),
                header=self.sheet2_header_entry.get()).vlookupTable()


