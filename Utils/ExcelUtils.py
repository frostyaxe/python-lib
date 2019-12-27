'''
Created on 24-Dec-2019

@author: Sangeeta-Laptop
'''


from openpyxl import load_workbook
 
class ExcelUtils:
    
    def retrievesExcelSheets(self,excel):
        wb = load_workbook(filename = excel)
        return wb