from sklearn import linear_model

reg = linear_model.LinearRegression()

reg.fit([[0,0,0,0], [1, 0,0,0], [0, 2,0,0]], [0, 1, 1])

print(reg)