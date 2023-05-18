from tkinter import *
from vlookup.run_vlookup import vlookup

class vlookup_LyrStackup_Gui:
    def __init__(self,rootframe, fileName):
        self.rootframe = rootframe
        self.fileName = fileName

        # Create a Canvas widget to hold the frame and scrollbar
        self.canvas = Canvas(self.rootframe)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # Create a frame to hold the label and button
        self.frame = Frame(self.canvas)
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.lyrStack_fme = LabelFrame(self.frame, text="LAYER STACKUP",labelanchor="n")
        self.lyrStack_fme.grid(row=0,column=0)


        #------------------------First Sheet Gui-----------------------# 
        self.lyrStack_sheet_1 = LabelFrame(self.lyrStack_fme,text="First Sheet (As a Lookup Table)",labelanchor="n")
        self.lyrStack_sheet_1.grid(row=0,column=0,padx=5,pady=5)

        self.shee1_label = Label(self.lyrStack_sheet_1,text="Sheet:").grid(row=0,column=0,padx=3,pady=3)

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
        self.Sheet1_clicked.set(self.Sheet1_options[4])
        # self.Sheet1_drop_list.append(self.Sheet1_clicked)

        self.Sheet1_drop = OptionMenu(self.lyrStack_sheet_1,self.Sheet1_clicked,*self.Sheet1_options)
        self.Sheet1_drop.grid(row=1,column=0,padx=5,pady=5)

        # print(self.Sheet1_clicked.get())

        self.sheet1_lkupTbl_Col = Label(self.lyrStack_sheet_1,text="Lookup \nTable Col").grid(row=0,column=1,padx=5,pady=5,sticky="n")
        self.sheet1_lkupTbl_Col_Entry = Entry(self.lyrStack_sheet_1,borderwidth=3,width=4,fg="black",background="white")
        self.sheet1_lkupTbl_Col_Entry.grid(row=1,column=1,padx=3,pady=3)

        self.sheet1_lkupTbl_result_Col = Label(self.lyrStack_sheet_1,text="Result Col").grid(row=0,column=2,padx=5,pady=5,sticky="n")
        self.sheet1_lkupTbl_result_Entry = Entry(self.lyrStack_sheet_1,borderwidth=3,width=4,fg="black", background="white")
        self.sheet1_lkupTbl_result_Entry.grid(row=1,column=2,padx=3,pady=3)

        #------------------------Second Sheet Gui-----------------------# 
        self.lyrStack_sheet_2 = LabelFrame(self.lyrStack_fme,text="Second Sheet (As a Lookup value)",labelanchor="n")
        self.lyrStack_sheet_2.grid(row=0,column=1,padx=5,pady=5)

        self.shee2_label = Label(self.lyrStack_sheet_2,text="Sheet:").grid(row=0,column=0,padx=3,pady=3)

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
        self.Sheet2_clicked.set(self.Sheet2_options[5])
        # self.Sheet1_drop_list.append(self.Sheet1_clicked)

        self.Sheet2_drop = OptionMenu(self.lyrStack_sheet_2,self.Sheet2_clicked,*self.Sheet2_options)
        self.Sheet2_drop.grid(row=1,column=0,padx=5,pady=5)

        # print(self.Sheet2_clicked.get())

        self.sheet2_lkup_result_Col = Label(self.lyrStack_sheet_2,text="Result\nCol Insert").grid(row=0,column=1,padx=5,pady=5,sticky="n")
        self.sheet2_result_insert_col_Entry = Entry(self.lyrStack_sheet_2,border=3,width=4,fg="black",background="white")
        self.sheet2_result_insert_col_Entry.grid(row=1,column=1,padx=3,pady=3)

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

        #Set Default input
        self.sheet1_lkupTbl_Col_Entry.insert(0,"A")
        self.sheet1_lkupTbl_result_Entry.insert(0,"B")
        self.sheet2_result_insert_col_Entry.insert(0,"G")


    def run_LyrStackup_Tbl_vlookup(self):
        vlookup(filename= self.fileName,
                sheet1=self.Sheet1_clicked.get(),
                sheet2= self.Sheet2_clicked.get(),
                lookup_Tbl_column = self.sheet1_lkupTbl_Col_Entry.get(),
                lookup_Tbl_output = self.sheet1_lkupTbl_result_Entry.get(),
                lookup_out_insert = self.sheet2_result_insert_col_Entry.get()).vlookup_Stackup_Table()


