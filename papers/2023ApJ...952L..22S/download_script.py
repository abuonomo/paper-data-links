# This script was generated by an AI model and has not been reviewed by a human expert. Please use with caution.

from sunpy.net import Fido, attrs as a
from astropy import units as u

# Define the observation period as mentioned in the context
start_date = '2013-09-01'
end_date = '2022-11-27'

# Time range for the entire observation period
time_range = a.Time(start_date, end_date)

# AIA on SDO: Observations of hot channels and prominences
aia_instrument = a.Instrument("AIA")
aia_wavelengths = a.Wavelength(131 * u.angstrom) | a.Wavelength(304 * u.angstrom)
aia_query = Fido.search(time_range, aia_instrument, aia_wavelengths)

# K-COR at MLSO: Observations of polarization brightness in the lower corona
kcor_instrument = a.Instrument("K-COR")
kcor_wavelength = a.Wavelength(7200 * u.angstrom, 7500 * u.angstrom)
kcor_query = Fido.search(time_range, kcor_instrument, kcor_wavelength)

# LASCO on SOHO: Observations of CME structures in the outer corona
lasco_instrument = a.Instrument("LASCO")
lasco_detector = a.Detector("C2")
lasco_query = Fido.search(time_range, lasco_instrument, lasco_detector)

# Display the query results
print("Query for AIA observations of hot channels and prominences:")
print(aia_query)
print("Query for K-COR observations of polarization brightness:")
print(kcor_query)
print("Query for LASCO C2 observations of CME structures in the outer corona:")
print(lasco_query)

# Uncomment the lines below to download the data
# aia_files = Fido.fetch(aia_query)
# kcor_files = Fido.fetch(kcor_query)
# lasco_files = Fido.fetch(lasco_query)
