''' 
    Description: This parser allows you to parse the properties file. It helps you to get the value of the specified key from the properties file.
    Version: 1.0
    Author: Abhishek Prajapati
'''

#Import the required libraries here
import os

'''
    @Description: This method allows you to get reader object containing the properties file content.
    @Param filepath: Path of the properties file.
    @Author: Abhishek Prajapati
    @Email: prajapatiabhishek1996@gmail.com
'''
def getReader( filepath ):
    verifyFilePath( filepath )
    reader = open( filepath, 'r' )
    return reader

''' 
    @Description: This method verifies the existence of specifed file. 
    @Param filepath: Path of the properties file.
    @Author: Abhishek Prajapati
    @Email: prajapatiabhishek1996@gmail.com
    @FileNotFoundError: This exception is thrown when file is not present at the specified location.
'''
def verifyFilePath( filepath ):
    if os.path.exists( filepath ):
        print("File: " + str( filepath ) + " exists at the specified location.")
    else:
        try:
            raise FileNotFoundError("File: " + str( filepath ) + " does not exist at the specified location.")
        except FileNotFoundError as fnfexception:
            print("[Exception FNF]\t" + str( fnfexception ))
            exit()
            
''' 
    @Description: This method prints the content of the properties file in the output console.
    @Param reader: Reader object containing the content of properties file.
    @Author: Abhishek Prajapati
    @Email: prajapatiabhishek1996@gmail.com
    @TypeError: When reader is None then it will throw the TypeError.
'''
def printFileContent( reader ):
    if reader is not None:
        for line in reader:
            print( line.rstrip() )
    else:
        try:
            raise TypeError("Reader does not have any value!!!")
        except TypeError as typeerror:
            print( "[Exception TypeError]\t" + str( typeerror ) )
            


''' 
    @Description: This method generates map by reading the content of the properties file.
    @Param reader: Reader object containing the properties file content.
    @Author: Abhishek Prajapati
    @Email: prajapatiabhishek1996@gmail.com
    @Return: Converted properties file content into map.
'''
def generateMap( reader ):

    props_dict = {}
    
    for line in reader:
    
        line = line.rstrip() 

        if "=" not in line: 
            continue 
        if line.startswith("#"): 
            continue 

        key, value = line.split("=", 1)
        props_dict[key] = value
        
    return props_dict
    

''' 
    @Description: This method will return the value present for the specified key in the properties file.
    @Param filepath: Path of the properties file.
    @param key: key of which value needs to be fetched from the properties file.
    @Author: Abhishek Prajapati
    @Email: prajapatiabhishek1996@gmail.com
    @Return: Value of the specified key present in the properties file.
'''
def get( filepath, key ):
    props_dict = generateMap( getReader( filepath ) )
    for dict_key, dict_value in props_dict.items(): 
         if dict_key.rstrip() == key.rstrip(): 
             return dict_value 
  
    try:
        raise KeyError( "Key: " + key + " does not exist in the specified properties file: " + filepath ) 
    except KeyError as keyerror:
        print( "[Exception KeyError]\t" + str( keyerror ) )
        exit()
    

print("Name:" + get( "details.properties", "state" ))

#printFileContent(getReader("details.properties"))