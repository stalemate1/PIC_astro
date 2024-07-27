import numpy as np
from scipy.special import erf

def halo_mass_function(mass, redshift, rho_m=2.775e11, delta_c=1.686):
    """
    Calculate the halo mass function using the Sheth-Tormen mass function.
    
    Parameters:
    - mass: array-like, halo masses in solar masses
    - redshift: float, redshift
    - rho_m: float, mean matter density of the universe (default is critical density in M_sun/Mpc^3)
    - delta_c: float, critical density for collapse
    
    Returns:
    - dn/dm: array-like, number density of halos per unit mass
    """
    # Parameters for Sheth-Tormen mass function
    A = 0.3222
    a = 0.707
    p = 0.3
    q = 1.0
    
    # Define variables
    sigma = np.sqrt(np.var(mass))  # Placeholder for actual sigma(mass) calculation
    nu = delta_c / sigma
    
    # Sheth-Tormen mass function
    f_nu = A * (1 + (1 / (a * nu ** 2)) ** p) * np.sqrt(a * nu ** 2 / (2 * np.pi)) * np.exp(-a * nu ** 2 / 2)
    dn_dm = f_nu * rho_m / mass ** 2 * np.abs(np.gradient(sigma, mass))
    
    return dn_dm


def halo_bias_function(mass, redshift):
    """
    Calculate the halo bias as a function of mass and redshift.
    
    Parameters:
    - mass: array-like, halo masses in solar masses
    - redshift: float, redshift
    
    Returns:
    - bias: array-like, halo bias
    """
    bias = 1 + (mass / 1e13 / (1 + redshift)) ** 0.15
    return bias

def density_profile(r, mass, concentration):
    """
    Calculate the density profile using the NFW profile.
    
    Parameters:
    - r: array-like, radial distances in kpc
    - mass: float, halo mass in solar masses
    - concentration: float, concentration parameter
    
    Returns:
    - density: array-like, density profile in M_sun/kpc^3
    """
    rho_crit = 2.775e2  # Critical density in M_sun/kpc^3
    delta_c = 200 / 3 * concentration ** 3 / (np.log(1 + concentration) - concentration / (1 + concentration))
    r_s = (3 * mass / (4 * np.pi * 200 * rho_crit)) ** (1 / 3) / concentration
    density = delta_c * rho_crit / ((r / r_s) * (1 + r / r_s) ** 2)
    
    return density

def concentration_mass_relation(mass, redshift):
    """
    Calculate the concentration-mass relation.
    
    Parameters:
    - mass: array-like, halo masses in solar masses
    - redshift: float, redshift
    
    Returns:
    - concentration: array-like, concentration parameter
    """
    concentration = 9 / (1 + redshift) * (mass / 1e12) ** (-0.13)
    return concentration

def power_spectrum(k, redshift):
    """
    Calculate the power spectrum.
    
    Parameters:
    - k: array-like, wavenumbers in h/Mpc
    - redshift: float, redshift
    
    Returns:
    - P(k): array-like, power spectrum
    """
    P_k = k ** -3 * np.exp(-k / (0.1 * (1 + redshift)))
    return P_k

def correlation_function(r, redshift):
    """
    Calculate the correlation function.
    
    Parameters:
    - r: array-like, separations in Mpc
    - redshift: float, redshift
    
    Returns:
    - xi(r): array-like, correlation function
    """
    xi_r = r ** -1.8 * np.exp(-r / (10 * (1 + redshift)))
    return xi_r

def weak_lensing_shear_map(mass_distribution, redshift):
    """
    Calculate the weak lensing shear map.
    
    Parameters:
    - mass_distribution: array-like, mass distribution
    - redshift: float, redshift
    
    Returns:
    - shear_map: array-like, weak lensing shear map
    """
    shear_map = np.cumsum(mass_distribution) / (1 + redshift)
    return shear_map
