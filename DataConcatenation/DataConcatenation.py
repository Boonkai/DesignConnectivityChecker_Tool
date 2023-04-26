import openpyxl
from datetime import datetime
import Background_GUI_Tool

class DataConcatenation:
    def __init__(self, 
                 col_1= None,
                 col_2=None,
                 sheet1_name=None,
                 sheet2_name=None,
                 col_insert_sheet_name= None,
                 col_insert=None,
                 concat_symbol=None,
                 header = None):
        
        self.col_1 = col_1
        self.col_2 = col_2
        self.sheet1_name = sheet1_name
        self.sheet2_name = sheet2_name
        self.col_insert = col_insert
        self.start_row = 2 # start from the specific row to exclude the header row
        self.concat_symbol = concat_symbol
        self.header = header
        self.col_insert_sheet_name = col_insert_sheet_name

    def data_concat(self):
        # Load the Excel file
        # workbook = openpyxl.load_workbook("2023-04-13 171628.xlsx")
        workbook = openpyxl.load_workbook(Background_GUI_Tool.y)

        # Select the worksheet
        df1 = workbook[self.sheet1_name]
        df2 = workbook[self.sheet2_name]
        df3 = workbook[self.col_insert_sheet_name]

        end_row = df1.max_row

        if len(self.col_insert) >=2:
            col_header_insert = 0
            for c in self.col_insert:
                col_header_insert = col_header_insert * 26 + ord(c) - ord('A') + 1
            print(col_header_insert)
        else:
            col_header_insert= ord(self.col_insert) - ord('A') + 1


        if self.header != None:
            df3.cell(row=1, column=col_header_insert).value = self.header
        else:
            pass

        for row in range(self.start_row, end_row+1):
            column_1_value = df1[self.col_1 + str(row)].value
            column_2_value = df2[self.col_2 + str(row)].value
            combined_value = str(column_1_value) + self.concat_symbol + str(column_2_value) # combine the two column values with a space in between

            if self.col_insert == None:
                print(combined_value)
            else:
                df3[self.col_insert + str(row)].value = combined_value # write the combined value to the third column (column C)    
                
        workbook.save(Background_GUI_Tool.y)