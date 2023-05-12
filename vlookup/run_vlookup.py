import openpyxl
from openpyxl.styles import Border, Side
from openpyxl.styles import Alignment

class vlookup:
    def __init__(self,
                 filename,
                 sheet1,
                 sheet2,
                 lookup_out_insert,
                 lookup_Tbl_column,
                 lookup_Tbl_output,
                 lookup_val_col=None,
                 header=None,
                 BO_DQ_Col=None,
                 symbol1=None,
                 NetName_Col=None):
        
        
        self.filename = filename
        self.sheet1 = sheet1
        self.sheet2 = sheet2
        self.lookup_out_insert = lookup_out_insert.upper()
        self.lookup_Tbl_column = lookup_Tbl_column.upper()
        self.lookup_Tbl_output = lookup_Tbl_output.upper()
        self.header = header
        self.BO_DQ_Col = BO_DQ_Col
        self.symbol1 = symbol1
        self.NetName_Col = NetName_Col
        if lookup_val_col == None :
            pass
        else:
            self.lookup_val_col = lookup_val_col.upper()

        # Open the Excel file
        self.workbook = openpyxl.load_workbook(self.filename)

        # Select the sheet to work with
        # sheet1 is table lookup whereas sheet2 is lookup value
        self.sheet1 = self.workbook[self.sheet1]
        self.sheet2 = self.workbook[self.sheet2]

        #Character Aconvertion to Int
        self.lkvTbl_Col  = self.column_label_to_number(self.lookup_Tbl_column)
        self.lkvTbl_Result_Col = self.column_label_to_number(self.lookup_Tbl_output)
        self.lkv_out_insert = self.column_label_to_number(self.lookup_out_insert)
        if lookup_val_col == None:
            pass
        else:
            self.lkv_val_Col  = self.column_label_to_number(self.lookup_val_col)

        # Set the border for each cell                    
        self.border = Border(left=Side(border_style='thin', color='000000'),
                        right=Side(border_style='thin', color='000000'),
                        top=Side(border_style='thin', color='000000'),
                        bottom=Side(border_style='thin', color='000000'))
        # Set Alignment to each cell
        self.center_alignment = Alignment(horizontal='center', vertical='center')

    def column_label_to_number(self,label):
        total = 0
        for i, char in enumerate(reversed(label)):
            value = ord(char) - 64
            total += value * (26 ** i)
        return total
    
    def vlookupTable(self):
        # Define lookup list
        self.lookup_value = []
        self.lookup_output = []

        for row in self.sheet2.iter_rows(values_only=True):
            self.lookup_value.append(row[self.lkv_val_Col -1])
            
        for value in self.lookup_value:
            for vlook_row in self.sheet1.iter_rows(values_only=True):
                if value == None:
                    continue
                if value == vlook_row[self.lkvTbl_Col - 1]:
                    self.lookup_output.append(vlook_row[self.lkvTbl_Result_Col -1])
    
        # Insert header with boarder and alignment styling
        self.sheet2.cell(row=2, column= self.lkv_out_insert).value = self.header
        self.sheet2.cell(row=2, column= self.lkv_out_insert).border = self.border
        self.sheet2.cell(row=2, column= self.lkv_out_insert).alignment = self.center_alignment


        for i, output in enumerate(self.lookup_output):
            cell = self.sheet2.cell(row=i+3, column= self.lkv_out_insert) 
            cell.value = output
            cell.border = self.border
            cell.alignment = self.center_alignment

        self.workbook.save(self.filename)

    def vlookup_Stackup_Table(self):
        # Define lookup list
        self.lookup_value = ["Layer Name"]
        self.lookup_output = ["Layer Name"]

        self.DDR_14L = ["L1","L14","L3","L5","L10","L12","L1","L14","L3","L5","L10","L12"]
        self.DDR_16L = ["L1","L14","L3","L5","L7","L12","L1","L14","L3","L5","L7","L12",]
        self.DDR_18L = ["L1","L14","L3","L5","L7","L12","L1","L14","L3","L5","L7","L12",]

        # Retrive total layer and store into lookup_value list
        for row in self.sheet1.iter_rows(values_only=True):
            if row[self.lkvTbl_Col -1] == None:
                continue
            else:
                self.lookup_value.append(row[self.lkvTbl_Col -1])
        
        # check the last index of a list 
        if self.lookup_value[-1] == "L14":
            # Perform Layer comparision 
            for value in self.DDR_14L:
                for vlook_row in self.sheet1.iter_rows(values_only=True):
                    if value == vlook_row[self.lkvTbl_Col - 1]:
                        self.lookup_output.append(vlook_row[self.lkvTbl_Result_Col -1])

        # check the last index of a list 
        if self.lookup_value[-1] == "L16":
            # Perform Layer comparision 
            for value in self.DDR_16L:
                for vlook_row in self.sheet1.iter_rows(values_only=True):
                    if value == vlook_row[self.lkvTbl_Col - 1]:
                        self.lookup_output.append(vlook_row[self.lkvTbl_Result_Col -1])

        # check the last index of a list 
        if self.lookup_value[-1] == "L18":
            # Perform Layer comparision 
            for value in self.DDR_18L:
                for vlook_row in self.sheet1.iter_rows(values_only=True):
                    if value == vlook_row[self.lkvTbl_Col - 1]:
                        self.lookup_output.append(vlook_row[self.lkvTbl_Result_Col -1])

        # print(self.lookup_output)

        for i, output in enumerate(self.lookup_output):
            cell = self.sheet2.cell(row=i+2, column= self.lkv_out_insert) 
            cell.value = output
            cell.border = self.border
            cell.alignment = self.center_alignment

        self.workbook.save(self.filename)

    def vlookup_Routing_layer(self):
        # Define lookup list
        self.lkv_NetNm_Col = self.column_label_to_number(self.NetName_Col)
        self.lkv_BO_Dq_Col = self.column_label_to_number(self.BO_DQ_Col)
        self.lookup_value = []
        self.lookup_output = []
        self.lookup_bodq_val = []

        self.bodq_col = self.lkv_BO_Dq_Col

        for bodq_Val in self.sheet2.iter_rows(min_row=3,max_row=14,values_only=True):
            self.lookup_bodq_val.append(bodq_Val[self.lkv_BO_Dq_Col-1])
        
        for vals in self.lookup_bodq_val:
            for Netnm_val in self.sheet2.iter_rows(min_row=3, values_only=True):
                self.Concat_Val = Netnm_val[self.lkv_NetNm_Col -1] + self.symbol1 + str((vals))
                self.lookup_value.append(self.Concat_Val)
            
        # for i in self.lookup_value:
        #     print(i)
            
        max_row = self.sheet1.max_row

        for value in self.lookup_value:
            self.row_count = 1
            for vlook_row in self.sheet1.iter_rows(min_row=1, values_only=True):
                if self.row_count < max_row:
                    # print(self.row_count)
                    if value == vlook_row[self.lkvTbl_Col - 1]:
                        self.lookup_output.append(vlook_row[self.lkvTbl_Result_Col -1])
                        continue
                    else:
                        self.row_count +=1
                else:
                    # self.lookup_output.append(vlook_row[6])
                    self.lookup_output.append("#N/A")

        # for i in self.lookup_output:
        #     print(i)
        
    
        # Insert header with boarder and alignment styling
        self.sheet2.cell(row=2, column= self.lkv_out_insert).value = self.header
        self.sheet2.cell(row=2, column= self.lkv_out_insert).border = self.border
        self.sheet2.cell(row=2, column= self.lkv_out_insert).alignment = self.center_alignment


        for i, output in enumerate(self.lookup_output):
            cell = self.sheet2.cell(row=i+3, column= self.lkv_out_insert) 
            cell.value = output
            cell.border = self.border
            cell.alignment = self.center_alignment

        self.workbook.save(self.filename)

