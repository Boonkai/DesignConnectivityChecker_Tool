from tkinter import *
from vlookup.run_vlookup import vlookup

class vlookupMem_Impedance_Gui:
    def __init__(self,
                 rootframe,
                 first_sheet,
                 tabel_col,
                 second_sheet,
                 NetName_value_col,
                 TotalLength_value_col,
                 insert_col,
                 header):
        self.rootframe = rootframe
        self.first_sheet = first_sheet
        self.tabel_col = tabel_col
        self.second_sheet = second_sheet
        self.NetName_value_col = NetName_value_col
        self.TotalLength_value_col = TotalLength_value_col
        self.insert_col = insert_col
        self.header = header

        self.Mem_Impdce_frame = LabelFrame(self.rootframe, text="Impedance",labelanchor="n")
        self.Mem_Impdce_frame.grid(row=2,column=0,pady=10)


        #------------------------First Sheet Gui-----------------------# 
        self.Mem_Impdce_frame_sheet1 = LabelFrame(self.Mem_Impdce_frame,text="First Sheet(Vlookup Table)",labelanchor="n")
        self.Mem_Impdce_frame_sheet1.grid(row=0,column=0,padx=5,pady=5)

        self.shee1_label = Label(self.Mem_Impdce_frame_sheet1,text="Sheet:").grid(row=0,column=0,padx=3,pady=3)

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

        self.Sheet1_drop = OptionMenu(self.Mem_Impdce_frame_sheet1,self.Sheet1_clicked,*self.Sheet1_options)
        self.Sheet1_drop.grid(row=0,column=1,padx=5,pady=5)

        self.sheet1_lkupTbl_Col = Label(self.Mem_Impdce_frame_sheet1,text="Vlookup DDR\nLength Col").grid(row=1,column=0,padx=5,pady=5,sticky="n")
        self.sheet1_lkupTbl_Col_Entry = Entry(self.Mem_Impdce_frame_sheet1,borderwidth=3,width=10,fg="black",background="white")
        self.sheet1_lkupTbl_Col_Entry.grid(row=1,column=1,padx=2,pady=2)

        #------------------------Second Sheet Gui-----------------------# 
        self.Mem_Impdce_sheet2 = LabelFrame(self.Mem_Impdce_frame,text="Second Sheet(Vlookup value)",labelanchor="n")
        self.Mem_Impdce_sheet2.grid(row=0,column=1,padx=5,pady=5)

        # Drop down Sheet
        self.shee2_label = Label(self.Mem_Impdce_sheet2,text="Sheet:").grid(row=0,column=0)
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
        self.Sheet2_clicked.set(self.Sheet2_options[int(self.second_sheet)])

        self.Sheet2_drop = OptionMenu(self.Mem_Impdce_sheet2,self.Sheet2_clicked,*self.Sheet2_options)
        self.Sheet2_drop.grid(row=0,column=1)

        #NetName input entry
        self.sheet2_Mem_Netname_col_label = Label(self.Mem_Impdce_sheet2,text="NetName Col\n(For DQS Checking)").grid(row=1,column=0,sticky="n")
        self.sheet2_vlookup_Mem_NetName_col_entry = Entry(self.Mem_Impdce_sheet2,border=3,width=10,fg="black",background="white")
        self.sheet2_vlookup_Mem_NetName_col_entry.grid(row=1,column=1,padx=3)

        #Total Length input entry
        self.sheet2_Mem_Impdce_col_label = Label(self.Mem_Impdce_sheet2,text="Vlookup Total\nLength Value Col").grid(row=2,column=0,sticky="n")
        self.sheet2_vlookup_Mem_Impdce_col_entry = Entry(self.Mem_Impdce_sheet2,border=3,width=10,fg="black",background="white")
        self.sheet2_vlookup_Mem_Impdce_col_entry.grid(row=2,column=1,padx=3)

        # Impedance Result Col insert input entry
        self.sheet2_Mem_Impdce_result_Col_label = Label(self.Mem_Impdce_sheet2,text="Impedance \nOutput Insert Col").grid(row=3,column=0,padx=3,sticky="n")
        self.sheet2_Mem_Impdceresult_insert_col_Entry = Entry(self.Mem_Impdce_sheet2,border=3,width=10,fg="black",background="white")
        self.sheet2_Mem_Impdceresult_insert_col_Entry.grid(row=3,column=1,padx=3)

        # Impedance Header input entry
        self.sheet2_Mem_Impdce_header_label = Label(self.Mem_Impdce_sheet2,text="Header").grid(row=4,column=0,padx=3,sticky="n")
        self.sheet2_Mem_Impdce_header_entry = Entry(self.Mem_Impdce_sheet2,border=5,width=10,fg="black",background="white")
        self.sheet2_Mem_Impdce_header_entry.grid(row=4,column=1,padx=3)

        #Set Default input
        self.sheet1_lkupTbl_Col_Entry.insert(0,str(self.tabel_col))
        self.sheet2_vlookup_Mem_NetName_col_entry.insert(0,str(self.NetName_value_col))
        self.sheet2_vlookup_Mem_Impdce_col_entry.insert(0,str(self.TotalLength_value_col))
        self.sheet2_Mem_Impdceresult_insert_col_Entry.insert(0,str(self.insert_col))
        self.sheet2_Mem_Impdce_header_entry.insert(0,str(self.header))

    def run_vlookup_Impedance(self,fileName):
        self.fileName = fileName
        vlookup(filename= self.fileName,
                sheet1=self.Sheet1_clicked.get(),
                sheet2= self.Sheet2_clicked.get(),
                NetName_Col= self.sheet2_vlookup_Mem_NetName_col_entry.get(),
                lookup_Tbl_column = self.sheet1_lkupTbl_Col_Entry.get(),
                header= self.sheet2_Mem_Impdce_header_entry.get(),
                lookup_val_col = self.sheet2_vlookup_Mem_Impdce_col_entry.get(),
                lookup_out_insert = self.sheet2_Mem_Impdceresult_insert_col_Entry.get()).vlookup_impedance()
        

