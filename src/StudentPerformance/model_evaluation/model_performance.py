from src.StudentPerformance.model_evaluation.model_selection import model_selection,actual_model
from sklearn.metrics import accuracy_score
from src.StudentPerformance.train_test.train_model import train_model
import pickle
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

def model_save(df):

    x_train, x_test, y_train, y_test = train_model(df)
    y_pred = model_selection(df)

    result = accuracy_score(y_pred,y_test)
    model_name,model = actual_model(df)

    print(f"Model Name : {model_name}")
    print(f"Accuracy : {result}")

    # Saving the model
    with open("my_model\Logistic_model.pkl","wb") as file:
        pickle.dump(model,file)
        print("Successfully Save the Model!")

df = pd.read_csv("H:\\Student_Performance\\new_data\\data.csv")
model_save(df)