# load libraries
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

print("All libraries were correctly loaded")

# import libs
import pandas as pd

# Load data
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)

print('The data is available on the environment')

# Summarize data

## Dimensions of dataset
print(dataset.shape)

## View data
print(dataset.head(20))

## Statistical summary
print(dataset.describe())

## Class distribution
print(dataset.groupby('class').size()

#print('All summaries are computed.')


# Univariate plots

## boxplots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

## histograms
dataset.hist()
plt.show()

# Multivariate plots

## scatter plot matrix
scatter_matrix(dataset)
plt.show()

# Build model

## Split-out validation dataset
array = dataset.values
x = array[:,0:4]
y = array[:,4]
validation_size = 0.20
seed = 7
x_train, x_validation, y_train, y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

## Test options to evaluation metric
seed = 7
scoring = 'accuracy'

## Spot check algorithms
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append((''KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))

# Evaluate each model
results = []
names = []

for name, model in models:
    kfold: model_selection.KFold(n_split=10, random_state=seed)
    cv_results = model_selection.cross_val_score(model, x_train, y_train, cv=kfold, scoring=scorind)
    results.append(cv_results)
    names.append(name)
    msg = "%s: f (%f)" % (names, cv_results.mean(), cv_results.std())
    print(msg)

## Compare algorithms
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()

# Make predictions on validation data
knn = KNeighborsClassifier()
knn.fit(x_train, y_train)
predictions = knn.predict(x_validation)
print(accuracy_score(y_validation, predictions))
print(confusiion_matrix(y_validation, predictions))
print(classification_report(y_validation, predictions))

