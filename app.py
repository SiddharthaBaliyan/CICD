import pandas as pd
import numpy
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#data preprocessing
path = "data/data.csv"
data=pd.read_csv(path)
X=data.drop(columns=["Outcome"])
y=data['Outcome']


X_train,X_test,y_train,y_test=train_test_split(X,y, test_size=0.2, random_state=42)

model=RandomForestClassifier(n_estimators=100,random_state=42)

model.fit(X_train,y_train)
y_pred=model.predict(X_test)

accuracy=accuracy_score(y_test,y_pred)

print(f"Few of the predicted classes are {y_pred[1]}, {y_pred[2]}")
print(f"We got -- {accuracy} as accuracy score")
