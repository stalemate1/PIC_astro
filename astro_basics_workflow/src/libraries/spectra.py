# src/libraries/spectra.py
import numpy as np
from astropy.modeling import blackbody_lambda
from astropy import units as u

def blackbody_spectrum_astropy(wavelengths, temperature):
    wavelengths_m = wavelengths * 1e-10  # Convert to meters
    flux = blackbody_lambda(wavelengths_m, temperature).to('erg / (cm^2 s Å)').value
    return flux

def combined_blackbody_spectrum(wavelengths, temperatures, weights):
    flux = np.zeros_like(wavelengths)
    for temp, weight in zip(temperatures, weights):
        flux += weight * blackbody_spectrum_astropy(wavelengths, temp)
    return flux

def agn_spectrum(wavelengths, norm, alpha):
    return norm * (wavelengths / 1000.0) ** (-alpha)

def add_emission_lines(wavelengths, flux, lines):
    flux_with_lines = np.copy(flux)
    for line_wavelength, strength in lines.items():
        idx = np.argmin(np.abs(wavelengths - line_wavelength))
        flux_with_lines[idx] += strength
    return flux_with_lines
