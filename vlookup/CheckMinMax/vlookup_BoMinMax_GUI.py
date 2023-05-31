from tkinter import *
from vlookup.run_vlookup import vlookup

class vlookup_Bo_MinMax_Gui:
    def __init__(self,
                 rootframe,
                 first_sheet,
                 tabel_col,
                 result_col,
                 second_sheet,
                 value_col,
                 Min_insert_col,
                 Max_insert_col,
                 insert_row,
                 Min_header,
                 Max_header):
        self.rootframe = rootframe
        self.first_sheet = first_sheet
        self.tabel_col = tabel_col
        self.result_col = result_col
        self.second_sheet = second_sheet
        self.value_col = value_col
        self.Min_insert_col = Min_insert_col
        self.Max_insert_col = Max_insert_col
        self.insert_row = insert_row
        self.Min_header = Min_header
        self.Max_header = Max_header

        self.Bo_MinMax_frame = LabelFrame(self.rootframe, text="Breakout Length Min and Max value",labelanchor="n")
        self.Bo_MinMax_frame.grid(row=3,column=0,pady=10)


        #------------------------First Sheet Gui-----------------------# 
        self.Mem_Bo_MinMax_frame_sheet1 = LabelFrame(self.Bo_MinMax_frame,text="First Sheet(Vlookup Table)",labelanchor="n")
        self.Mem_Bo_MinMax_frame_sheet1.grid(row=0,column=0,padx=5,pady=5)

        self.shee1_label = Label(self.Mem_Bo_MinMax_frame_sheet1,text="Sheet:").grid(row=0,column=0,padx=3,pady=3)

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

        self.Sheet1_drop = OptionMenu(self.Mem_Bo_MinMax_frame_sheet1,self.Sheet1_clicked,*self.Sheet1_options)
        self.Sheet1_drop.grid(row=0,column=1,padx=5,pady=5)

        self.sheet1_lkupTbl_Col = Label(self.Mem_Bo_MinMax_frame_sheet1,text="Vlookup Routing\nLayer Col").grid(row=1,column=0,padx=5,pady=5,sticky="n")
        self.sheet1_lkupTbl_Col_Entry = Entry(self.Mem_Bo_MinMax_frame_sheet1,borderwidth=3,width=10,fg="black",background="white")
        self.sheet1_lkupTbl_Col_Entry.grid(row=1,column=1,padx=2,pady=2)

        self.sheet1_result_Col_Label = Label(self.Mem_Bo_MinMax_frame_sheet1,text="Result Col").grid(row=2,column=0,padx=5,pady=5,sticky="n")
        self.sheet1_lkupTbl_result_Entry = Entry(self.Mem_Bo_MinMax_frame_sheet1,borderwidth=3,width=10,fg="black", background="white")
        self.sheet1_lkupTbl_result_Entry.grid(row=2,column=1,padx=2,pady=2)

        #------------------------Second Sheet Gui-----------------------# 
        self.Bo_MinMax_sheet2 = LabelFrame(self.Bo_MinMax_frame,text="Second Sheet(Vlookup value)",labelanchor="n")
        self.Bo_MinMax_sheet2.grid(row=0,column=1,padx=5,pady=5)

        # Drop down Sheet
        self.shee2_label = Label(self.Bo_MinMax_sheet2,text="Sheet:").grid(row=0,column=0)
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

        self.Sheet2_drop = OptionMenu(self.Bo_MinMax_sheet2,self.Sheet2_clicked,*self.Sheet2_options)
        self.Sheet2_drop.grid(row=0,column=1)

        #Vlookup Layer Name input entry
        self.sheet2_vlookup_LyrNm_val_col_label = Label(self.Bo_MinMax_sheet2,text="Vlookup Layer\nName value Col ").grid(row=1,column=0,sticky="n")
        self.sheet2_vlookup_LyrNm_val_col_entry = Entry(self.Bo_MinMax_sheet2,border=3,width=10,fg="black",background="white")
        self.sheet2_vlookup_LyrNm_val_col_entry.grid(row=1,column=1,padx=3)

        # Breakout Length Min Result Col insert input entry
        self.sheet2_result_Col_label = Label(self.Bo_MinMax_sheet2,text="Min Output\nInsert Col").grid(row=2,column=0,padx=3,sticky="n")
        self.sheet2_BoMin_insert_col_Entry = Entry(self.Bo_MinMax_sheet2,border=3,width=10,fg="black",background="white")
        self.sheet2_BoMin_insert_col_Entry.grid(row=2,column=1,padx=3)

        # Breakout Length Max Result Col insert input entry
        self.sheet2_result_Col_label = Label(self.Bo_MinMax_sheet2,text="Max Output\nInsert Col").grid(row=3,column=0,padx=3,sticky="n")
        self.sheet2_BoMax_insert_col_Entry = Entry(self.Bo_MinMax_sheet2,border=3,width=10,fg="black",background="white")
        self.sheet2_BoMax_insert_col_Entry.grid(row=3,column=1,padx=3)

        # Breakout Length Min/Max Result Row insert input entry
        self.sheet2_result_Row_label = Label(self.Bo_MinMax_sheet2,text="Start Insert Row").grid(row=4,column=0,padx=5,pady=5,sticky="n")
        self.sheet2_insert_row_Entry = Entry(self.Bo_MinMax_sheet2,borderwidth=3,width=10,fg="black",background="white")
        self.sheet2_insert_row_Entry.grid(row=4,column=1,padx=2,pady=2)

        # Breakout Length Min Header input entry
        self.sheet2_header_label = Label(self.Bo_MinMax_sheet2,text="Header").grid(row=5,column=0,padx=3,sticky="n")
        self.sheet2_Minheader_entry = Entry(self.Bo_MinMax_sheet2,border=5,width=10,fg="black",background="white")
        self.sheet2_Minheader_entry.grid(row=5,column=1,padx=3)

        # Breakout Length Max Header input entry
        self.sheet2_header_label = Label(self.Bo_MinMax_sheet2,text="Min Header").grid(row=5,column=0,padx=3,sticky="n")
        self.sheet2_Minheader_entry = Entry(self.Bo_MinMax_sheet2,border=5,width=10,fg="black",background="white")
        self.sheet2_Minheader_entry.grid(row=5,column=1,padx=3)

        # Breakout Length Max Header input entry
        self.sheet2_header_label = Label(self.Bo_MinMax_sheet2,text="Max Header").grid(row=6,column=0,padx=3,sticky="n")
        self.sheet2_Maxheader_entry = Entry(self.Bo_MinMax_sheet2,border=5,width=10,fg="black",background="white")
        self.sheet2_Maxheader_entry.grid(row=6,column=1,padx=3)

        #Set Default input
        self.sheet1_lkupTbl_Col_Entry.insert(0,str(self.tabel_col))
        self.sheet1_lkupTbl_result_Entry.insert(0,str(self.result_col))
        self.sheet2_vlookup_LyrNm_val_col_entry.insert(0,str(self.value_col))
        self.sheet2_BoMin_insert_col_Entry.insert(0,str(self.Min_insert_col))
        self.sheet2_BoMax_insert_col_Entry.insert(0,str(self.Max_insert_col))
        self.sheet2_insert_row_Entry.insert(0,str(insert_row))
        self.sheet2_Minheader_entry.insert(0,str(self.Min_header))
        self.sheet2_Maxheader_entry.insert(0,str(self.Max_header))


    def run_vlookup_BoMinMax(self,fileName):
        self.fileName = fileName
        vlookup(filename= self.fileName,
                sheet1=self.Sheet1_clicked.get(),
                sheet2= self.Sheet2_clicked.get(),
                lookup_Tbl_column = self.sheet1_lkupTbl_Col_Entry.get(),
                lookup_Tbl_output= self.sheet1_lkupTbl_result_Entry.get(),
                lookup_val_col= self.sheet2_vlookup_LyrNm_val_col_entry.get(),
                lookup_Min_insert_col = self.sheet2_BoMin_insert_col_Entry.get(),
                lookup_Max_insert_col = self.sheet2_BoMax_insert_col_Entry.get(),
                lookup_out_insert_row = self.sheet2_insert_row_Entry.get(),
                Min_header = self.sheet2_Minheader_entry.get(),
                Max_header = self.sheet2_Maxheader_entry.get()).vlookup_BreakoutLength_MinMax()
        

