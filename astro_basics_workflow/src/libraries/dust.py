# src/libraries/dust.py
import numpy as np
from astropy.modeling import blackbody_lambda
from extinction import Fitzpatrick99

def apply_dust_extinction(wavelengths, flux, Av, Rv=3.1):
    extinction_curve = Fitzpatrick99(wavelengths, Av, Rv)
    flux_extincted = flux * 10**(-0.4 * extinction_curve)
    return flux_extincted

def dust_emission_spectrum(wavelengths, temperature, mass):
    wavelengths_m = wavelengths * 1e-10  # Convert to meters
    flux = mass * blackbody_lambda(wavelengths_m, temperature).to('erg / (cm^2 s Å)').value
    return flux
