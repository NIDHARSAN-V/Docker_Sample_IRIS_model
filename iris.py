import joblib
from sklearn.datasets import load_iris  # Corrected import statement
from sklearn.ensemble import RandomForestClassifier


iris = load_iris()
X, Y = iris.data, iris.target


model = RandomForestClassifier()
model.fit(X, Y)
print(iris.target_names)



joblib.dump(model, 'iris_model.joblib')
