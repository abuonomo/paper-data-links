# This script was generated by an AI model and has not been reviewed by a human expert. Please use with caution.

from sunpy.net import Fido, attrs as a
from astropy import units as u

# Define the observation period for SUVI on GOES
suv_time_range = a.Time('2018-08-07', '2018-09-13')
suv_instrument = a.Instrument("SUVI")
suv_wavelength = a.Wavelength(195 * u.Angstrom)

# Define the observation period for LASCO on SOHO
lasco_time_range = a.Time('2018-08-07', '2018-09-13')
lasco_instrument = a.Instrument("LASCO")
# LASCO observes in white-light, which typically does not require a specific wavelength query in VSO

# Define the observation period for SDO
sdo_time_range = a.Time('2018-08-08', '2018-09-09')
sdo_instrument = a.Instrument("AIA")
sdo_wavelengths = a.Wavelength(171 * u.Angstrom) | a.Wavelength(193 * u.Angstrom) | a.Wavelength(211 * u.Angstrom)

# Perform the queries for each instrument
suv_query = Fido.search(suv_time_range, suv_instrument, suv_wavelength)
lasco_query = Fido.search(lasco_time_range, lasco_instrument)
sdo_query = Fido.search(sdo_time_range, sdo_instrument, sdo_wavelengths)

# Display the query results for each instrument
print("Query for GOES/SUVI EUV observations:")
print(suv_query)
print("Query for SOHO/LASCO white-light observations:")
print(lasco_query)
print("Query for SDO/AIA EUV observations:")
print(sdo_query)

# Uncomment the lines below to download the data
# suv_files = Fido.fetch(suv_query)
# lasco_files = Fido.fetch(lasco_query)
# sdo_files = Fido.fetch(sdo_query)
