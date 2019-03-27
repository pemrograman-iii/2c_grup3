import pandas as pnd

def ListModePandas():
    df = pnd.read_csv('hrdata.csv')
    print(df)

def DictModePandas():
    df = pnd.read_csv('hrdata.csv')
    dct = pnd.DataFrame.from_dict(df)
    print(dct)
    
def DateFormatStandardDataFrame():
    df = pnd.read_csv('hrdata.csv', 
                parse_dates=['Hire Date'])
    print(df)

def IndexColumn():
    df = pnd.read_csv('hrdata.csv', 
                index_col='Name')
    print(df)
    
def ChangeAttribute():
    df = pnd.read_csv('hrdata.csv', 
                header=0, 
                names=['Employee', 'Hired','Salary', 'Sick Days'])
    print(df)

def WritePandas():
    df = pnd.read_csv('hrdata.csv', 
            index_col='Employee', 
            parse_dates=['Hired'],
            header=0, 
            names=['Employee', 'Hired', 'Salary', 'Sick Days'])
    df.to_csv('hrdata_modified.csv')
    
