from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from datetime import datetime
import re
import Background_GUI_Tool
import pandas as pd
import openpyxl
from openpyxl.utils import get_column_letter

# Files declaration:
NetPin_file = "Component_Pin_Report.htm"
Netlist_file = "Netlist.htm"
BOM_file = "BOM.htm"
LenWidLayer_file = "Etch_Length_Width_Layer.htm"


class DataExtraction:
    # Provide required files for the first argument as follow:
    #1.NetPin_file OR
    #2.Netlist_file OR
    #3.BOM_file OR
    #4.TraceLengthWidthLayer_file

    # Provide column extract for the second argument:
    # e.g:
    # "col_index = [0,1,5]" --> represent 1st,2nd and 6th column data will be extract
    #NOTE: [0,1,5] is an index base where 1st index always start from Zero 

    def __init__(self,file,col_select):
        self.file = file
        self.col_select = col_select

        # Component_Pin_Report empty list:
        self.col_data_ComponentPin_REFDES = []
        self.col_data_ComponentPin_PinNumber = []
        self.col_data_ComponentPin_CompDeviceTyp = []
        self.col_data_ComponentPin_PinTyp= []
        self.col_data_ComponentPin_PinName = []
        self.col_data_ComponentPin_NetName = []

        # Netlist empty list:
        self.col_data_Netlist_NetName = []
        self.col_data_Netlist_NetPins = []
        self.col_data_Netlist_NetPins_1st_data = []
        self.col_data_Netlist_NetPins_2nd_data = [' ']

        # BOM Report empty list:
        self.col_data_BOM_SymName = []
        self.col_data_BOM_CompDeviceTyp = []
        self.col_data_BOM_CompValue = []
        self.col_data_BOM_CompTol = []
        self.col_data_BOM_CompClass = []
        self.col_data_BOM_REFDES = []

        # Trace Length by Layer and Width Report empty list:
        self.col_data_TraceLenWid_NetName = []
        self.col_data_TraceLenWid_LayerName = []
        self.col_data_TraceLenWid_TotalLength = []
        self.col_data_TraceLenWid_LineWidth = []
        self.col_data_TraceLenWid_LenATwidth = []


    def HTML_Data_Extract(self):
        # Open the HTML file
        with open(str(self.file), 'r') as html_file:
            # Read the file's contents
            html_content = html_file.read()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the table element you want to extract data from
        table = soup.find("table")

        #Component Pin Report data extract:
        if NetPin_file in self.file:
            for row in table.find_all("tr"):
                columns = row.find_all("td")
                for i in self.col_select:
                    if i.get() == "NetPin_option1":
                        self.col_data_ComponentPin_REFDES.append(columns[0].text.strip())
                    if i.get() == "NetPin_option2":
                        # Using "Regular expression" to detect html mixed number (numbers that contain digits and non-digits)
                        # if mixed-number / empty ==> store in to list, else convert to integer and sotre to list.
                        if re.findall('[A-Z]+',columns[1].text.strip()):
                            self.col_data_ComponentPin_PinNumber.append(columns[1].text.strip())
                        elif len(columns[1].text.strip()) == 0:
                            self.col_data_ComponentPin_PinNumber.append(columns[1].text.strip())
                        else:
                            j = int(columns[1].text.strip())
                            self.col_data_ComponentPin_PinNumber.append(j)
                    if i.get() == "NetPin_option3":
                        self.col_data_ComponentPin_CompDeviceTyp.append(columns[2].text.strip())
                    if i.get() == "NetPin_option4":
                        self.col_data_ComponentPin_PinTyp.append(columns[3].text.strip())
                    if i.get() == "NetPin_option5":
                        self.col_data_ComponentPin_PinName.append(columns[4].text.strip())
                    if i.get() == "NetPin_option6":
                        self.col_data_ComponentPin_NetName.append(columns[5].text.strip())

        #Netlist Report data extract:
        if Netlist_file in self.file:
            for row in table.find_all("tr"):
                columns = row.find_all("td")
                for i in self.col_select:
                    if i.get() == "Netlist_option1":
                        self.col_data_Netlist_NetName.append(columns[0].text.strip())
                    if i.get() == "Netlist_option2":
                        self.col_data_Netlist_NetPins.append(columns[1].text.strip())
            
            # Separate out 2nd data afater spacing
            for index, separate in enumerate(self.col_data_Netlist_NetPins):
                if index == 0:
                    self.col_data_Netlist_NetPins_1st_data.append(separate)
                else:
                    atpos = separate.find(' ')
                    self.col_data_Netlist_NetPins_1st_data.append(separate[:atpos ])
                    self.col_data_Netlist_NetPins_2nd_data.append(separate[atpos: ])
                    # print(separate[atpos: ])

        #BOM Report data extract:
        if BOM_file in self.file:
            for row in table.find_all("tr"):
                columns = row.find_all("td")
                for i in self.col_select:
                    if i.get() == "BOM_option1":
                        self.col_data_BOM_SymName.append(columns[0].text.strip())
                    if i.get() == "BOM_option2":
                        self.col_data_BOM_CompDeviceTyp.append(columns[1].text.strip())
                    if i.get() == "BOM_option3":
                        self.col_data_BOM_CompValue.append(columns[2].text.strip())
                    if i.get() == "BOM_option4":
                        self.col_data_BOM_CompTol.append(columns[3].text.strip())
                    if i.get() == "BOM_option5":
                        self.col_data_BOM_CompClass.append(columns[4].text.strip())
                    if i.get() == "BOM_option6":
                        self.col_data_BOM_REFDES.append(columns[5].text.strip())

        # Trace Length by Layer and Width Report data extract:
        if LenWidLayer_file in self.file:
            for row in table.find_all("tr"):
                columns = row.find_all("td")
                for i in self.col_select:
                    if i.get() == "LenWidLayer_option1":
                        self.col_data_TraceLenWid_NetName.append(columns[0].text.strip())
                    if i.get() == "LenWidLayer_option2":
                        self.col_data_TraceLenWid_LayerName.append(columns[1].text.strip())
                    if i.get() == "LenWidLayer_option3":
                        # Using "Regular expression" to detect html mixed number (numbers that contain digits and non-digits)
                        # if mixed-number ==> store in to list, else convert to integer and sotre to list.
                        if re.findall('[A-Z]+',columns[2].text.strip()):
                            self.col_data_TraceLenWid_TotalLength.append(columns[2].text.strip())
                        else:
                            k = float(columns[2].text.strip())
                            self.col_data_TraceLenWid_TotalLength.append(k)
                    if i.get()== "LenWidLayer_option4":
                        if re.findall('[A-Z]+',columns[3].text.strip()):
                            self.col_data_TraceLenWid_LineWidth.append(columns[3].text.strip())
                        else:
                            l = float(columns[3].text.strip())
                            self.col_data_TraceLenWid_LineWidth.append(l)
                    if i.get() == "LenWidLayer_option5":
                        if re.findall('[A-Z]+',columns[4].text.strip()):
                            self.col_data_TraceLenWid_LenATwidth.append(columns[4].text.strip())
                        else:
                            m = float(columns[4].text.strip())
                            self.col_data_TraceLenWid_LenATwidth.append(m)  

class ExportTOexcel:
    def __init__(self,object,sheet,column_num):
        self.row = 0
        self.object = object
        self.sheet = sheet
        self.column_num =column_num

    def WriteTOexcel(self):
        # print(len(self.object))
        for i in self.object:
            self.sheet.cell(self.row +1,self.column_num +1).value = i
            self.row += 1


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