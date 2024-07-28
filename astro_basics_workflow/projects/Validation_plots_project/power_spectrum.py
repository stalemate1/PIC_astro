import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.libraries.basic_validation_plots import (
    power_spectrum
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

# Power Spectrum
k = np.linspace(0.1, 10, 100)  # Example wavenumbers
ps_mock = power_spectrum(k, redshift_mock.mean())
ps_euclid = power_spectrum(k, redshift_euclid.mean())
compare_results(ps_mock, ps_euclid, 'Power Spectrum', 'Wavenumber', 'Power')