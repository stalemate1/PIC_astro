# src/libraries/regression.py
import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from scipy.optimize import curve_fit

def LR_model_fitting(x, y, degree, fun_display=True):
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    model.fit(x, y)
    
    if fun_display:
        poly_features = model.named_steps['polynomialfeatures']
        linear_regression = model.named_steps['linearregression']

        coefficients = linear_regression.coef_
        intercept = linear_regression.intercept_

        feature_names = poly_features.get_feature_names_out(['lm_halo'])

        function_terms = []
        for coef, name in zip(coefficients[0], feature_names):
            function_terms.append(f"{coef:.3f} * {name}")

        polynomial_function = f"{intercept[0]:.3f} + " + " + ".join(function_terms)
        print(polynomial_function)

        return function_terms, intercept[0]
    else:
        return model

def plot_fit_function(x, y, function_terms, intercept):
    function = np.full_like(x, intercept, dtype=float)

    for term in function_terms:
        coef, variable = term.split(' * ')
        coef = float(coef)
        if variable == '1':
            function += coef
        else:
            power = int(variable.split('^')[-1]) if '^' in variable else 1
            function += coef * np.power(x, power)

    plt.scatter(x, y, s=1, color='blue', label='Data Points')
    plt.scatter(x, function, s=0.7, color='red', label='Polynomial Fit')
    plt.title('Polynomial Fit of lm_halo vs n_sats_halo')
    plt.legend()
    plt.show()

    return function

def exponential_function(x, a, b, c):
    return a * np.exp(x / b) + c

def find_param(function, x_data, y_data):
    popt, pcov = curve_fit(function, x_data, y_data, maxfev=5000)
    a, b, c = popt
    print(f"Fitted parameters: a = {a}, b = {b}, c = {c}")
    print(f"{a:.3f} * np.exp(x /{b:.3f}) + {c:.3f} ")

    return popt
