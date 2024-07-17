# This script was generated by an AI model and has not been reviewed by a human expert. Please use with caution.

from sunpy.net import Fido, attrs as a
from astropy import units as u

# Define the observation period for the solar flares
start_time = '2014-03-28T00:00:00'
end_time = '2014-03-29T23:59:59'
time_range = a.Time(start_time, end_time)

# SDO/AIA for EUV imaging
aia_instrument = a.Instrument("AIA")
aia_wavelengths = a.Wavelength(304 * u.Angstrom) | a.Wavelength(193 * u.Angstrom)
aia_query = Fido.search(time_range, aia_instrument, aia_wavelengths)

# SDO/HMI for photospheric magnetic fields
hmi_instrument = a.Instrument("HMI")
hmi_physobs = a.Physobs("LOS_magnetic_field")
hmi_query = Fido.search(time_range, hmi_instrument, hmi_physobs)

# RHESSI for X-ray imaging and spectroscopy
rhessi_instrument = a.Instrument("RHESSI")
rhessi_wavelength = a.Wavelength(3 * u.keV, 17000 * u.keV)  # X-ray range
rhessi_query = Fido.search(time_range, rhessi_instrument, rhessi_wavelength)

# Display the query results for each instrument
print("Query for SDO/AIA EUV observations:")
print(aia_query)
print("Query for SDO/HMI LOS magnetic field observations:")
print(hmi_query)
print("Query for RHESSI X-ray observations:")
print(rhessi_query)

# Uncomment the lines below to download the data
# aia_files = Fido.fetch(aia_query)
# hmi_files = Fido.fetch(hmi_query)
# rhessi_files = Fido.fetch(rhessi_query)
