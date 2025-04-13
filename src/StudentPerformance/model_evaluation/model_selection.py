import pandas as pd
from src.StudentPerformance.train_test.train_model import train_model
from sklearn.linear_model import LogisticRegression

def model_selection(df):
    x_train,x_test,y_train,y_test = train_model(df)

    model = LogisticRegression()

    model.fit(x_train,y_train)

    y_pred = model.predict(x_test)

    return y_pred

def actual_model(df):
    x_train,x_test,y_train,y_test = train_model(df)

    model = LogisticRegression()

    model.fit(x_train,y_train)

    model_name = model.__class__.__name__

    return model_name,model

    

# df = pd.read_csv("H:\\Student_Performance\\new_data\\data.csv")