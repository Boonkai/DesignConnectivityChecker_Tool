import openpyxl
from HtmlDataExtraction import DataExtracT_Export
from openpyxl.styles import Border, Side
from openpyxl.styles import Alignment

class CreateLyrTable:
    def __init__(self,
                 fileName,
                 Insert_sheet_name,
                 col_insert):
        self.fileName = fileName
        self.Insert_sheet_name = Insert_sheet_name
        self.col_insert = col_insert
        self.Ch_Name =  ["Channel","ChA","ChB","ChC","ChD","ChE","CHF","ChG","ChH","ChI","ChJ","ChK","ChL"]

        workbook = openpyxl.load_workbook(self.fileName)
        df1 = workbook[self.Insert_sheet_name]

        # Set the border for each cell
        self.border = Border(left=Side(border_style='thin', color='000000'),
                        right=Side(border_style='thin', color='000000'),
                        top=Side(border_style='thin', color='000000'),
                        bottom=Side(border_style='thin', color='000000'))
        
        # set the alignment of the cell to center
        self.center_alignment = Alignment(horizontal='center', vertical='center')

        for num, chl in enumerate(self.Ch_Name):
            df1[self.col_insert + str(num)].value = chl

            # Set Alignment and border for each cell
            df1[self.col_insert + str(num)].alignment = self.center_alignment
            df1[self.col_insert + str(num)].border = self.border

        workbook.save(self.fileName)

