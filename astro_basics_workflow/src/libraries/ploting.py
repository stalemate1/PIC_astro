import matplotlib.pyplot as plt

# Define a function for plotting and comparing results
def compare_results(mock_results, observed_results, title, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    plt.plot(mock_results, label='Mock Data')
    plt.plot(observed_results, label='Observed Data')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()