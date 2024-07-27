import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.libraries.basic_validation_plots import (
    halo_mass_function
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

# Halo Mass Function
hmf_mock = halo_mass_function(mass_mock, redshift_mock.mean())
hmf_euclid = halo_mass_function(mass_euclid, redshift_euclid.mean())
compare_results(hmf_mock, hmf_euclid, 'Halo Mass Function', 'Mass', 'Number Density')
