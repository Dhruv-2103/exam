from sklearn import linear_model
features = [[2],[1],[5],[10]]
labels=[27,11,75,155]
clf = linear_model.LinearRegression()
clf=clf.fit(features,labels)
predicted=clf.predict([[5],[5],[2]])
print(predicted)
