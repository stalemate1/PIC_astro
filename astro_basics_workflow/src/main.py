# src/main.py
from libraries.luminosity import luminosity_function
from libraries.spectra import blackbody_spectrum_astropy, combined_blackbody_spectrum, agn_spectrum, add_emission_lines
from libraries.dust import apply_dust_extinction, dust_emission_spectrum
import numpy as np

def main():
    # Example usage of luminosity_function
    l = np.array([1, 2, 3])
    a, b, l_cen, A, alpha, beta = 1, 1, 1, 1, -1, 2
    num_sat = luminosity_function(l, a, b, l_cen, A, alpha, beta)
    print(f'Number of satellites: {num_sat}')
    
    # Example usage of blackbody_spectrum_astropy
    wavelengths = np.linspace(1000, 10000, 100)  # Angstroms
    temperature = 5000  # Kelvin
    bb_spectrum = blackbody_spectrum_astropy(wavelengths, temperature)
    print(f'Blackbody Spectrum: {bb_spectrum}')
    
    # Example usage of combined_blackbody_spectrum
    temperatures = [3000, 5000, 7000]
    weights = [0.5, 0.3, 0.2]
    combined_spectrum = combined_blackbody_spectrum(wavelengths, temperatures, weights)
    print(f'Combined Blackbody Spectrum: {combined_spectrum}')
    
    # Example usage of agn_spectrum
    norm, alpha = 1e-15, -1.5
    agn_spec = agn_spectrum(wavelengths, norm, alpha)
    print(f'AGN Spectrum: {agn_spec}')
    
    # Example usage of add_emission_lines
    lines = {6563: 1e-13, 4861: 5e-14}  # H-alpha and H-beta
    flux_with_lines = add_emission_lines(wavelengths, bb_spectrum, lines)
    print(f'Spectrum with Emission Lines: {flux_with_lines}')
    
    # Example usage of apply_dust_extinction
    Av = 1.0
    flux_extincted = apply_dust_extinction(wavelengths, bb_spectrum, Av)
    print(f'Flux with Dust Extinction: {flux_extincted}')
    
    # Example usage of dust_emission_spectrum
    mass = 1e-3  # Solar masses
    dust_spectrum = dust_emission_spectrum(wavelengths, temperature, mass)
    print(f'Dust Emission Spectrum: {dust_spectrum}')

if __name__ == '__main__':
    main()
