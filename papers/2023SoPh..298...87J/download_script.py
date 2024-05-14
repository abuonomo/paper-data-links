# This script was generated by an AI model and has not been reviewed by a human expert. Please use with caution.

from sunpy.net import Fido, attrs as a
from astropy import units as u

# SDO/HMI Query
hmi_time_range = a.Time('2010-05-01', '2017-12-31')
hmi_instrument = a.Instrument("HMI")
hmi_wavelength = a.Wavelength(6173 * u.Angstrom)
hmi_observables = a.Physobs("LOS_magnetic_field") | a.Physobs("intensity") | a.Physobs("LOS_velocity")

# SOHO/MDI Query
mdi_time_range = a.Time('2010-05-01', '2011-04-11')
mdi_instrument = a.Instrument("MDI")
mdi_wavelength = a.Wavelength(6768 * u.Angstrom)  # Assuming the wavelength for LOS magnetograms
mdi_observables = a.Physobs("LOS_magnetic_field")

# BBSO Hα Observations Query
# Note: SunPy's Fido might not directly support BBSO Hα data retrieval. This is a placeholder for how one might structure the query if it were supported.
bbso_time_range = a.Time('2010-05-01', '2017-12-31')
bbso_wavelength = a.Wavelength(6563 * u.Angstrom)
# This is a hypothetical query, as Fido does not support BBSO directly.
# bbso_query = Fido.search(bbso_time_range, bbso_wavelength)

# Performing the queries for SDO/HMI and SOHO/MDI
hmi_query = Fido.search(hmi_time_range, hmi_instrument, hmi_wavelength, hmi_observables)
mdi_query = Fido.search(mdi_time_range, mdi_instrument, mdi_wavelength, mdi_observables)

# Display the query results for each instrument
print("Query for SDO/HMI observations:")
print(hmi_query)
print("Query for SOHO/MDI observations:")
print(mdi_query)
# print("Query for BBSO Hα observations:")  # Hypothetical, not executable
# print(bbso_query)

# Uncomment the lines below to download the data
# hmi_files = Fido.fetch(hmi_query)
# mdi_files = Fido.fetch(mdi_query)
# bbso_files = Fido.fetch(bbso_query)  # Hypothetical, not executable
