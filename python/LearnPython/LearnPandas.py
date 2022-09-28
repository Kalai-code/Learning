import pandas as pd

docpath = "/home/kalai/Learning/python/LearnPython/Documents/"
def readCSVFileWithHeader():
    df = pd.read_csv(docpath+"employees.csv",delimiter=',')
    print(df.to_string())


def readCSVFileWithoutHeader():
    listHeader = ["EMPLOYEE_ID","FIRST_NAME","LAST_NAME","EMAIL","PHONE_NUMBER","HIRE_DATE","JOB_ID","SALARY","COMMISSION_PCT","MANAGER_ID","DEPARTMENT_ID"]
    df = pd.read_csv(docpath+"employees_noheader.csv",delimiter=',',names=listHeader)
    print(df.to_string())


def readCSVFileAndDropColumn():
    df = pd.read_csv(docpath+"employees_drop.csv",delimiter=',')
    df.drop("COMMISSION_PCT", axis = 1, inplace=True)
    df.sort_values(by=["FIRST_NAME"],ascending=True,inplace=True)
    print(df.to_string())

readCSVFileAndDropColumn()