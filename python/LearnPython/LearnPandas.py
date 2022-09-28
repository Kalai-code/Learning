import pandas as pd
import os

print(os.path.dirname(os.path.abspath(__file__)))
#path to the csv document
docpath = os.path.dirname(os.path.abspath(__file__)) + "/Documents/"
# Read CSV file
def readCSVFileWithHeader():
    df = pd.read_csv(docpath+"employees.csv",delimiter=',')
    print(df.to_string())

# Read CSV file and add header
def readCSVFileWithoutHeader():
    listHeader = ["EMPLOYEE_ID","FIRST_NAME","LAST_NAME","EMAIL","PHONE_NUMBER","HIRE_DATE","JOB_ID","SALARY","COMMISSION_PCT","MANAGER_ID","DEPARTMENT_ID"]
    df = pd.read_csv(docpath+"employees_noheader.csv",delimiter=',',names=listHeader)
    print(df["FIRST_NAME"] + ' ' + df["LAST_NAME"])
    print('Length of Dataframe is', len(df))


# Remove a column from the dataframe

def readCSVFileAndDropColumn():
    df = pd.read_csv(docpath+"employees_drop.csv",delimiter=',')
    df.drop("COMMISSION_PCT", axis = 1, inplace=True)
    print("Results after dropping a column")
    print(df)
    

# Sort the records based on a column. Order by ascending
def readCSVFileAndSortRecords():
    df = pd.read_csv(docpath+"employees_drop.csv",delimiter=',')
    df.sort_values(by=["FIRST_NAME"],ascending=True,inplace=True)
    print("Results after sorting the records by first name")
    print(df)

"""
Show records using head() --> returns 5 records by default from the beginning. head(n) --> returns n number of records from beginning
Show records using tail() --> returns last 4 records by default from the end. tail(n) --> returns n number of records from end
"""
def readCSVFileAndUseHeadTail():
    df = pd.read_csv(docpath+"employees.csv",delimiter=',')
    print("Results after using head()")
    print(df.head())
    print("Results after using head(n)")
    print(df.head(10))
    print("Results after using tail()")
    print(df.tail())
    print("Results after using tail(n)")
    print(df.tail(10))

def readEachRecord():
    df = pd.read_csv(docpath+"employees.csv",delimiter=',')
    print(df.columns.values)
    for row in df.itertuples():
        print(list(row[1:]))



readEachRecord()