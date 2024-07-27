import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.libraries.basic_validation_plots import (
    density_profile, concentration_mass_relation
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

# Density Profiles
r = np.linspace(0.1, 10, 100)  # Example radial distances
dp_mock = density_profile(r, mass_mock.mean(), concentration_mass_relation(mass_mock.mean(), redshift_mock.mean()))
dp_euclid = density_profile(r, mass_euclid.mean(), concentration_mass_relation(mass_euclid.mean(), redshift_euclid.mean()))
compare_results(dp_mock, dp_euclid, 'Density Profiles', 'Radius', 'Density')