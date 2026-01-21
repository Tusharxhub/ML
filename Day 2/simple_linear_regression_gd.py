# implement simple linear regression using gradient decent to estimate the slope and intercept .use a learning rate of 0.01 and run for 1000 iteration.

# Simple Linear Regression using Gradient Descent
# Learning rate = 0.01
# Iterations = 1000

# Dataset
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

n = len(x)

# Initialize parameters
m = 0.0
c = 0.0

learning_rate = 0.01
iterations = 1000

for i in range(iterations):

    dm = 0.0
    dc = 0.0

    for j in range(n):
        y_pred = m * x[j] + c
        error = y[j] - y_pred

        dm += -2 * x[j] * error
        dc += -2 * error

    dm = dm / n
    dc = dc / n

    m = m - learning_rate * dm
    c = c - learning_rate * dc

print("Estimated Slope (m):", m)
print("Estimated Intercept (c):", c)
