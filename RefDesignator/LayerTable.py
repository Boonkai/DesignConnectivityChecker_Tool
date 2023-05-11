import openpyxl
from HtmlDataExtraction import DataExtracT_Export
from openpyxl.styles import Border, Side
from openpyxl.styles import Alignment

class CreateChlTable:
    def __init__(self,
                 fileName,
                 sheet_name,
                 TableValue,
                 col_insert):
        self.fileName = fileName
        self.sheet_name = sheet_name
        self.TableValue = TableValue
        self.col_insert = col_insert

        workbook = openpyxl.load_workbook(self.fileName)
        df1 = workbook[self.sheet_name]

        # Set the border for each cell
        self.border = Border(left=Side(border_style='thin', color='000000'),
                        right=Side(border_style='thin', color='000000'),
                        top=Side(border_style='thin', color='000000'),
                        bottom=Side(border_style='thin', color='000000'))
        
        # set the alignment of the cell to center
        self.center_alignment = Alignment(horizontal='center', vertical='center')

        for num, chl in enumerate(self.TableValue):
            df1[self.col_insert + str(num+2)].value = chl

            # Set Alignment and border for each cell
            df1[self.col_insert + str(num+2)].alignment = self.center_alignment
            df1[self.col_insert + str(num+2)].border = self.border

        workbook.save(self.fileName)

