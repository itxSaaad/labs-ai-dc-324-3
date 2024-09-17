import pandas as pd
import matplotlib.pyplot as plt
from scikit-learn.tree import plot_tree
from scikit-learn.tree import DecisionTreeClassifier
from scikit-learn.metrics import accuracy_score,classification_report
from scikit-learn.model_selection import train_test_split

column_names = ['Alternate', 'Bar', 'Fri/Sat', 'Hungry', 'Patrons', 'Price','Raining', 'Reservation', 'Type', 'WaitEstimate', 'Wait']

data = pd.read_csv('restaurant.csv',header=None, names=column_names)

print(data.head())

X = data.drop('Wait',axis=1)
y = data['Wait']

X = pd.get_dummies(X)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train,y_train)

y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)

print(f"Accuracy: {accuracy * 100:.2f}%")

print("Classification Report:")
print(classification_report(y_test,y_pred))

plt.figure(figsize=(20,10))
plot_tree(clf,feature_names=X.columns, class_names=True,filled=True)
plt.show()

feature_importances = clf.feature_importances_

X.columns = X.columns.str.replace(r'[A-Za-z0-9_]','',regex=True)

feature_db = pd.DataFrame({'Features': X.columns, 'Importance': feature_importances} )
feature_db = feature_db.sort_values(by='Importances',ascending=False)

plt.figure(figsize=(10,6))
plt.barh(feature_db['Feature'],feature_db['Importance'],color='skyblue')
plt.xlabel("Feature")
plt.ylabel("Important")
plt.title("Feature Importance in Decision Tree")
plt.gca().invert_yaxis()
plt.show()
