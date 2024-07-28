import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.libraries.basic_validation_plots import *
from src.libraries.ploting import *

# Load your mock and observed data
mock_data = pd.read_csv('data/lm_halo_vs_n_sats_halo.csv')
euclid_data = pd.read_csv('data/lm_halo_vs_n_sats_halo.csv')
#sdss_data = pd.read_csv('path_to_sdss_data.csv')

# Extract necessary columns for analysis
mass_mock = mock_data['lm_halo'].values
print(mass_mock)
redshift_mock = mock_data['n_sats_halo'].values
mass_euclid = euclid_data['lm_halo'].values
redshift_euclid = euclid_data['n_sats_halo'].values

# Halo Mass Function
hmf_mock = sheth_Tormen_HMF(mass_mock, redshift_mock.mean(), rho_m=2.775e11, delta_c=1.686)
hmf_euclid = sheth_Tormen_HMF(mass_euclid, redshift_euclid.mean(), rho_m=2.775e11, delta_c=1.686)
compare_results(hmf_mock, hmf_euclid, 'Halo Mass Function', 'Mass', 'Number Density')
