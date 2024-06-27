# This script was generated by an AI model and has not been reviewed by a human expert. Please use with caution.

from sunpy.net import Fido, attrs as a
from astropy import units as u

# Define the observation periods and instruments
eis_time_range = a.Time('2007-11-16T07:26:00', '2007-11-16T08:01:00')
sumer_time_range = a.Time('2007-11-16T09:01:00', '2007-11-16T10:03:00')

eis_instrument = a.Instrument("EIS")
sumer_instrument = a.Instrument("SUMER")

# Define the wavelength ranges
eis_wavelength = a.Wavelength(170 * u.angstrom, 290 * u.angstrom)  # Covering both SW and LW bands
sumer_wavelength = a.Wavelength(672 * u.angstrom, 1255 * u.angstrom)  # Covering all SUMER bands

# Perform the queries
eis_query = Fido.search(eis_time_range, eis_instrument, eis_wavelength)
sumer_query = Fido.search(sumer_time_range, sumer_instrument, sumer_wavelength)

# Display the query results
print("Query for Hinode/EIS observations:")
print(eis_query)
print("Query for SOHO/SUMER observations:")
print(sumer_query)

# Uncomment the lines below to download the data
# eis_files = Fido.fetch(eis_query)
# sumer_files = Fido.fetch(sumer_query)
