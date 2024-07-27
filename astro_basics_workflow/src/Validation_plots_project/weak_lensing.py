import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.libraries.basic_validation_plots import (
    weak_lensing_shear_map
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

# Weak Lensing Shear Maps
mass_distribution_mock = mock_data['mass_distribution'].values
mass_distribution_euclid = euclid_data['mass_distribution'].values
wl_mock = weak_lensing_shear_map(mass_distribution_mock, redshift_mock.mean())
wl_euclid = weak_lensing_shear_map(mass_distribution_euclid, redshift_euclid.mean())
compare_results(wl_mock, wl_euclid, 'Weak Lensing Shear Maps', 'Position', 'Shear')