import pandas as pd
from src.StudentPerformance.split.spliting import split
from sklearn.model_selection import train_test_split

def train_model(df):
    x,y = split(df)
    
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

    return x_train, x_test, y_train, y_test 

# df = pd.read_csv("H:\\Student_Performance\\new_data\\data.csv")
# x_train, x_test, y_train, y_test = train_model(df)
# print(x_train)