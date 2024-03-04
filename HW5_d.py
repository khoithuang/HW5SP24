# I got help from ChatGPT
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Function definitions for linear and cubic models
def linear_model(x, a, b):
    return a * x + b

def cubic_model(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

# Generate some synthetic data for fitting (replace this with actual x-y data)
np.random.seed(0)  # Seed for reproducibility
x_data = np.linspace(-10, 10, 100)
y_data_linear = 2.5 * x_data + 6  # True underlying linear relationship
y_data_cubic = 0.1 * x_data**3 - 0.5 * x_data**2 + 2.5 * x_data + 6  # True underlying cubic relationship
y_data = y_data_cubic + np.random.normal(size=x_data.size)  # Add some noise

# Perform the curve fitting for both models
linear_params, _ = curve_fit(linear_model, x_data, y_data)
cubic_params, _ = curve_fit(cubic_model, x_data, y_data)

# Generate y-values from the fitted models
y_fit_linear = linear_model(x_data, *linear_params)
y_fit_cubic = cubic_model(x_data, *cubic_params)

# Plot the data and the fits
plt.figure(figsize=(12, 6))
plt.scatter(x_data, y_data, label='Data', color='black')
plt.plot(x_data, y_fit_linear, label='Linear Fit', color='red')
plt.plot(x_data, y_fit_cubic, label='Cubic Fit', color='blue')

plt.title('Curve Fitting with Linear and Cubic Models')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
