import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.libraries.basic_validation_plots import (
    correlation_function
)
from src.libraries.ploting import *

# Load your mock and observed data
mock_data = pd.read_csv('path_to_mock_data.csv')
euclid_data = pd.read_csv('path_to_euclid_data.csv')
sdss_data = pd.read_csv('path_to_sdss_data.csv')

# Extract necessary columns for analysis
mass_mock = mock_data['mass'].values
redshift_mock = mock_data['redshift'].values
mass_euclid = euclid_data['mass'].values
redshift_euclid = euclid_data['redshift'].values

# Correlation Function
r = np.linspace(0.1, 10, 100)  # Example radial distances
cf_mock = correlation_function(r, redshift_mock.mean())
cf_euclid = correlation_function(r, redshift_euclid.mean())
compare_results(cf_mock, cf_euclid, 'Correlation Function', 'Radius', 'Correlation')