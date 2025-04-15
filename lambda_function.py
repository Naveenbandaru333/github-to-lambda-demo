import pandas as pd

def lambda_handler(event, context):
    data={'ID':[1,2],'Name':['Naveen','Kumar']}
    df=pd.DataFrame(data)
    print(df)
    Print('Done 1.0')

