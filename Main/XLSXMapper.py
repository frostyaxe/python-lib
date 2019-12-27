'''
Created on 24-Dec-2019

@author: Sangeeta-Laptop
'''

'''
    Importing required python libraries below
'''
from Utils.FileUtils import FileUtils

from Utils.ExcelUtils import ExcelUtils
'''
    Description: This class will create the dataset in the dictionary format by reading all the excel sheets present in the specified directory.
    Author: Abhishek Prajapati
'''

dictionary = {}
fileUtils = FileUtils();

class XLSXMapper:
       
    '''
        #will be removed    
        Description: This method will read all the excel files present in the specified directory.
        Author: Abhishek Prajapati
    '''
    def getAllExcelFiles(self):
        fileUtils = FileUtils();
        fileUtils.readAllExcels("D:\\Dataset")
    
    
    
    '''
        #will be removed
        Description: This method will create the parent keys based on the file name of the excel sheets present in the specified directory.
        Author: Abhishek Prajapati
    '''
    def createExcelWorkbookKeys(self, dir):
        fileUtils = FileUtils();
        filelist = fileUtils.getFileNamesFromDir("D:\\Dataset")
        print(filelist)
        return filelist
    
    
    '''
        Description: This method will create the dictionary based on the excelworkbook present in the specified directory.
        Param( Directory ): Path of the directory containing all the excel files.
        Author: Abhishek Prajapati
    '''
    def createDictionary(self, directory ):
        
        excelPaths = fileUtils.readAllExcels(directory)
        global dictionary
        '''  Iteration of sheet starts from here '''
        for path in excelPaths:
           
            excelwbname = fileUtils.path_leaf(path)
            sheets = ExcelUtils.retrievesExcelSheets(self, path)
            sheetDictionary = {}
            ''' Iteration of sheets starts from here '''
            for sheet in sheets:
                
                max_row = sheet.max_row
                max_column= sheet.max_column
                # Will print a particular row value 
                header_str = []
                xl_dict = {}
                for i in range(1, max_row + 1): 
                    # iterate over all columns
                    record_dict={}
                    dict_key=""
                    for j in range(1,max_column+1):
                        # get particular cell value    
                        cell_obj=sheet.cell(row=i,column=j)
        
                        # print cell value         
                        if( i == 1):
                            header_str.append(str(cell_obj.value))
                            continue

                        if(j==1):
                            dict_key = str(cell_obj.value)
                        else:
                            record_dict[header_str[j-1]]=str(cell_obj.value)
                        #column_data=column_data+str(cell_obj.value) + '|'
                        #print( header_str.split("|") a)
                    xl_dict[dict_key] = record_dict
                sheetDictionary[sheet.title] = xl_dict
   
                
                
                dictionary[excelwbname] = sheetDictionary
        print(dictionary)
    
    def retrieveValue(self, wbname, sheet, testcasename, key):
        return dictionary.get(wbname).get(sheet).get(testcasename).get(key)
        
        
XLSXMapper().createDictionary("D:\\Dataset")
print( XLSXMapper().retrieveValue("TestCase-pyDemo.xlsx", "Sheet1", "TestCase1", "Address") )
#sXLSXMapper().getAllExcelFiles()
#XLSXMapper().createExcelWorkbookKeys()