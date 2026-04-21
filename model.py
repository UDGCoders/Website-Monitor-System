import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

data=pd.read_csv("data/qoutes_ml.csv")

vectoriezer=CountVectorizer()
model = MultinomialNB()
# print(data.columns)

X=vectoriezer.fit_transform(data['quote'])
y=data["category"]

X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.2,random_state=42)

model.fit(X_train,y_train)
accuracy = model.score(X_test,y_test)
print("Accuracy:", accuracy)
# print(data.head())
# print(X.shape)
# print(y.head())


