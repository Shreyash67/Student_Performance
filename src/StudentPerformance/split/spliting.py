import pandas as pd

def split(df):
    x = df.iloc[:,:3]
    y = df.iloc[:,3:]

    return x,y

