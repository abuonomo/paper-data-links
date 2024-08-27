# This script was generated by an AI model and has not been reviewed by a human expert. Please use with caution.

```python
from sunpy.net import Fido, attrs as a
from astropy import units as u

# SOHO/EIT: Observing the source region and initial CME trajectory
soho_eit_time_range = a.Time('2008-04-08T00:00:00', '2008-04-09T23:59:59')
soho_eit_instrument = a.Instrument("EIT")
soho_eit_wavelength = a.Wavelength(195 * u.angstrom)

# STEREO/EUVI: High-resolution imaging of the CME
stereo_euvi_time_range = a.Time('2008-04-09T00:00:00', '2008-04-09T23:59:59')
stereo_euvi_instrument = a.Instrument("EUVI")
stereo_euvi_wavelengths = a.Wavelength(171 * u.angstrom) | a.Wavelength(195 * u.angstrom) | a.Wavelength(304 * u.angstrom)

# SOHO/LASCO: Observing the CME in the outer corona
lasco_time_range = a.Time('2008-04-09T00:00:00', '2008-04-09T23:59:59')
lasco_instrument = a.Instrument("LASCO")

# Performing the queries
soho_eit_query = Fido.search(soho_eit_time_range, soho_eit_instrument, soho_eit_wavelength)
stereo_euvi_query = Fido.search(stereo_euvi_time_range, stereo_euvi_instrument, stereo_euvi_wavelengths)
lasco_query = Fido.search(lasco_time_range, lasco_instrument)

# Display the query results
print("Query for SOHO/EIT observations:")
print(soho_eit_query)
print("Query for STEREO/EUVI observations:")
print(stereo_euvi_query)
print("Query for SOHO/LASCO observations:")
print(lasco_query)

# Uncomment the lines below to download the data
# soho_eit_files = Fido.fetch(soho_eit_query)
# stereo_euvi_files = Fido.fetch(stereo_euvi_query)
# lasco_files = Fido.fetch(lasco_query)
```

This script is tailored to the specific requirements of the context provided, focusing on the instruments and their capabilities as described in the scientific observation details. The queries are constructed to match the exact time ranges and wavelengths needed to study the 'Cartwheel CME' as detailed in the paper.