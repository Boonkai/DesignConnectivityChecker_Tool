from tkinter import *
from vlookup.run_vlookup import vlookup

class vlookupMem_RoutLyr_TtlLength_Gui:
    def __init__(self,rootframe):
        self.rootframe = rootframe

        self.Mem_RoutLyr_frame = LabelFrame(self.rootframe, text="Routing Layer & Total Length",labelanchor="n")
        self.Mem_RoutLyr_frame.grid(row=1,column=0,padx=10,pady=10,columnspan=2)


        #------------------------First Sheet Gui-----------------------# 
        self.Mem_RoutLayer_sheet1 = LabelFrame(self.Mem_RoutLyr_frame,text="First Sheet (Vlookup Table)",labelanchor="n")
        self.Mem_RoutLayer_sheet1.grid(row=0,column=0,padx=5,pady=5)

        self.shee1_label = Label(self.Mem_RoutLayer_sheet1,text="Sheet:").grid(row=0,column=0,padx=3,pady=3)

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

        self.Sheet1_drop = OptionMenu(self.Mem_RoutLayer_sheet1,self.Sheet1_clicked,*self.Sheet1_options)
        self.Sheet1_drop.grid(row=1,column=0,padx=5,pady=5)

        self.sheet1_lkupTbl_Col = Label(self.Mem_RoutLayer_sheet1,text="Vlookup \nNetName Col").grid(row=0,column=1,padx=5,pady=5,sticky="n")
        self.sheet1_lkupTbl_Col_Entry = Entry(self.Mem_RoutLayer_sheet1,borderwidth=3,width=6,fg="black",background="white")
        self.sheet1_lkupTbl_Col_Entry.grid(row=1,column=1,padx=2,pady=2)

        self.sheet1_lkupTbl_LyrNm_result_Col = Label(self.Mem_RoutLayer_sheet1,text="LayerName\nCol").grid(row=0,column=2,padx=5,pady=5,sticky="n")
        self.sheet1_lkupTbl_LyrNm_result_Entry = Entry(self.Mem_RoutLayer_sheet1,borderwidth=3,width=6,fg="black", background="white")
        self.sheet1_lkupTbl_LyrNm_result_Entry.grid(row=1,column=2,padx=2,pady=2)

        self.sheet1_lkupTbl_TtlLgth_result_Col = Label(self.Mem_RoutLayer_sheet1,text="Total Length\nCol").grid(row=0,column=3,padx=5,pady=5,sticky="n")
        self.sheet1_lkupTbl_TtlLgth_result_Entry = Entry(self.Mem_RoutLayer_sheet1,borderwidth=3,width=6,fg="black", background="white")
        self.sheet1_lkupTbl_TtlLgth_result_Entry.grid(row=1,column=3,padx=2,pady=2)

        #------------------------Second Sheet Gui-----------------------# 
        self.Mem_RoutLayer_sheet2 = LabelFrame(self.Mem_RoutLyr_frame,text="Second Sheet (Vlookup value)",labelanchor="n")
        self.Mem_RoutLayer_sheet2.grid(row=0,column=1,padx=5,pady=5)

        # Drop down Sheet
        self.shee2_label = Label(self.Mem_RoutLayer_sheet2,text="Sheet:").grid(row=0,column=0)
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

        self.Sheet2_drop = OptionMenu(self.Mem_RoutLayer_sheet2,self.Sheet2_clicked,*self.Sheet2_options)
        self.Sheet2_drop.grid(row=1,column=0)

        #LayerName input entry
        self.sheet2_Netnm_col_label = Label(self.Mem_RoutLayer_sheet2,text="Vlookup NetName\nValue Col").grid(row=0,column=1,sticky="n")
        self.sheet2_vlookup_Netnm_col_entry = Entry(self.Mem_RoutLayer_sheet2,border=3,width=6,fg="black",background="white")
        self.sheet2_vlookup_Netnm_col_entry.grid(row=1,column=1,padx=3)

        # Layer Name Result Col insert input entry
        self.sheet2_LyrNm_result_Col_label = Label(self.Mem_RoutLayer_sheet2,text="Layer name \nOutput Col Insert").grid(row=0,column=2,padx=3,sticky="n")
        self.sheet2_LyrNm_result_insert_col_Entry = Entry(self.Mem_RoutLayer_sheet2,border=3,width=6,fg="black",background="white")
        self.sheet2_LyrNm_result_insert_col_Entry.grid(row=1,column=2,padx=3)

        # Total Length Result Col insert input entry
        self.sheet2_TtlLgth_result_Col_label = Label(self.Mem_RoutLayer_sheet2,text="Total Length \nOutput Col Insert").grid(row=0,column=3,padx=3,sticky="n")
        self.sheet2_TtlLgth_result_insert_col_Entry = Entry(self.Mem_RoutLayer_sheet2,border=3,width=6,fg="black",background="white")
        self.sheet2_TtlLgth_result_insert_col_Entry.grid(row=1,column=3,padx=3)

        # Layer Name Header input entry
        self.sheet2_LyrNm_header_label = Label(self.Mem_RoutLayer_sheet2,text="Layer Name\nHeader").grid(row=0,column=4,padx=3,sticky="n")
        self.sheet2_LyrNm_header_entry = Entry(self.Mem_RoutLayer_sheet2,border=5,width=10,fg="black",background="white")
        self.sheet2_LyrNm_header_entry.grid(row=1,column=4,padx=3)

        # Total length Header input entry
        self.sheet2_TtlLgth_header_label = Label(self.Mem_RoutLayer_sheet2,text="Total Length\nHeader").grid(row=0,column=5,padx=3,sticky="n")
        self.sheet2_TtlLgth_header_entry = Entry(self.Mem_RoutLayer_sheet2,border=5,width=10,fg="black",background="white")
        self.sheet2_TtlLgth_header_entry.grid(row=1,column=5,padx=3)

        #Set Default input
        self.sheet1_lkupTbl_Col_Entry.insert(0,"A")
        self.sheet1_lkupTbl_LyrNm_result_Entry.insert(0,"E")
        self.sheet1_lkupTbl_TtlLgth_result_Entry.insert(0,"F")
        self.sheet2_vlookup_Netnm_col_entry.insert(0,"N")
        self.sheet2_LyrNm_result_insert_col_Entry.insert(0,"O")
        self.sheet2_TtlLgth_result_insert_col_Entry.insert(0,"P")
        self.sheet2_LyrNm_header_entry.insert(0,"Routing Layer")
        self.sheet2_TtlLgth_header_entry.insert(0,"Total length")

    def run_vlookup_Mem_RoutLyr(self,fileName):
        self.fileName = fileName
        vlookup(filename= self.fileName,
                sheet1=self.Sheet1_clicked.get(),
                sheet2= self.Sheet2_clicked.get(),
                lookup_Tbl_column = self.sheet1_lkupTbl_Col_Entry.get(),
                lookup_Tbl_LyrNm_out = self.sheet1_lkupTbl_LyrNm_result_Entry.get(),
                lookup_lyrNm_out_insert = self.sheet2_LyrNm_result_insert_col_Entry.get(),
                header_LyrNm =self.sheet2_LyrNm_header_entry.get(),
                NetName_Col = self.sheet2_vlookup_Netnm_col_entry.get()).vlookup_Routing_layer()
        
    def run_vlookup_Mem_TtlLgth(self,fileName):
        self.fileName = fileName
        vlookup(filename= self.fileName,
                sheet1=self.Sheet1_clicked.get(),
                sheet2= self.Sheet2_clicked.get(),
                lookup_Tbl_column = self.sheet1_lkupTbl_Col_Entry.get(),
                lookup_Tbl_TtlLgth_out = self.sheet1_lkupTbl_TtlLgth_result_Entry.get(),
                lookup_TtlLgth_out_insert = self.sheet2_TtlLgth_result_insert_col_Entry.get(),
                header_TtlLgth = self.sheet2_TtlLgth_header_entry.get(),
                NetName_Col = self.sheet2_vlookup_Netnm_col_entry.get()).vlookup_TotalLength()


