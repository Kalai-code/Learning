import pandas as pd
import os
import json

#path to the csv document
docpath = os.path.dirname(os.path.abspath(__file__)) + "/Documents/"


def CSVToJSONOption1():
    df = pd.read_csv(docpath+"employees.csv",delimiter=',')
    df = df.head(2)
    header_list = list(df.columns.values)
    data_dict = []
    for row in df.itertuples():
        data_dict.append(dict(zip(header_list,list(row[1:]))))
    print(data_dict)
    with open(docpath+"CSVToJSONOption1.json","w") as file:
        file.write(str(data_dict))

def CSVToJSONOption2():
    df = pd.read_csv(docpath+"employees.csv",delimiter=',')
    df = df.head(2)
    data_list = [df.loc[x].to_json() for x in df.index]
    print(data_list)
    

def CSVToJSONOption3():
    df = pd.read_csv(docpath+"employees.csv",delimiter=',')
    df = df.head(2)
    result = df.to_json(orient="records")
    parsed = json.loads(result)
    print(json.dumps(parsed))  


CSVToJSONOption1()
