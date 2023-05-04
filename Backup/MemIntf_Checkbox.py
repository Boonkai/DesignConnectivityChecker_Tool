from tkinter import *

class CheckBox:
    def __init__(self,root):
        self.root = root
        # self.root = Tk()
        self.mainGUI_check_options = [("DDR_14L", "DDR_14LL"),
                                    ("DDR_16L", "DDR_16L"), 
                                    ("DDR_18L", "DDR_18L"),  
                                    ("PCIe", "PCie"),
                                    ("XGMI", "XGMI"),
                                    ("USB", "USB"),
                                    ("SATA", "SATA"),
                                    ("MISC", "MISC"),
                                    ("CLK", "CLK")]

        # Create a list of StringVar variables to store the selected check button values
        self.mainGUI_MemIntf_Chkbox_vars = []
        self.mainGUI_MemIntf_Chkbox_Btn = []
        for self.option in self.mainGUI_check_options:
            var = StringVar()
            self.mainGUI_MemIntf_Chkbox_vars.append(var)

        # Use a for loop to create the check buttons
        for i, (text, value) in enumerate(self.mainGUI_check_options):
            check_button = Checkbutton(self.root, text=text, variable=self.mainGUI_MemIntf_Chkbox_vars[i], onvalue=value, offvalue="")
            check_button.grid(row=i+1,column=0,sticky="w")
            check_button.select()
            self.mainGUI_MemIntf_Chkbox_Btn.append(check_button)

        def print_selected():
            for i in self.mainGUI_MemIntf_Chkbox_vars:
                print(i.get())

        button = Button(self.root, text="Print selected", command=print_selected)
        button.grid(row=len(self.mainGUI_check_options)+1, column=0, sticky="w")

    def run(self):
        self.root.mainloop()

check =CheckBox(Tk())
check.run()