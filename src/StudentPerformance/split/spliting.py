import pandas as pd

def split(df):
    x = df.iloc[:,:3]
    y = df.iloc[:,3:]

    return x,y

# df = pd.read_csv("H:\\Student_Performance\\new_data\\data.csv")
# x,y = split(df)
# print(y)