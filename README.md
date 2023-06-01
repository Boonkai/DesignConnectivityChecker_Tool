# DesignConnectivityChecker_Tool

Step 1:
Download source files and extract the zip into “C:\” drive
e.g. “C:\DesignConnectivityChecker_Tool”
IMPORTANT: Must Extract in C:\ drive

Step 2:
Open CMD as administrator and then cd to the project path
Command : “cd C:\DesignConnectivityChecker_Tool”

Step 3: (Required for first time setup only)
Install openpyxl and Tkinter library
Command; pip install -r requirements.txt

Step 4:
Run Report Checker Main GUI 
Command: py -3 .\ReportChecker_Main_GUI.py

Step 5:
Browse following report files to extract:
1) Component_Pin_Report.htm
2) Netlist.htm
3) BOM.htm
4) Etch_Length_Width_Layer.htm
5) Layer_Stackup_report.htm
NOTE: All report files name shown above has already been set as default
      Any file name that is diffrent than above will produced an unexpected report output
      Thus, Kindly rename the file accordingly.

Step 6:
Fill in required “Reference Designator” input for CPU0 and CPU1.
Note: You can leave blank on CPU1 input entry if it's not is required

Step 7:
Click “Breakout/Bus Channel Width” navigation tab to fill in required value  

Step 8 (Optional)
Default Interface memory file is located in  “/DesignConnectivityChecker_Tool/RefDesignator/Interface.xlsx” folder which consists only TOP layer , User can add more interface name to the source file provided and “Please DO NOT Change the worksheet Tab NAME”.

Step 9:
Click “Generate Report” button to generate the report 

Step 10
The Generated report will be automatically save in “Report_output” folder