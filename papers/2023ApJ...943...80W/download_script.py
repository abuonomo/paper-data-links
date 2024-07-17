# This script was generated by an AI model and has not been reviewed by a human expert. Please use with caution.

from sunpy.net import Fido, attrs as a
from astropy import units as u

# Define the observation period as per the context
start_date = '2010-01-01'
end_date = '2015-12-31'
time_range = a.Time(start_date, end_date)

# Define the instrument and the type of data we are interested in
instrument = a.Instrument("HMI")
physobs = a.Physobs("vector_magnetic_field")
wavelength = a.Wavelength(6173 * u.angstrom, 6174 * u.angstrom)  # Approximate operational range

# Construct the query
query = Fido.search(time_range, instrument, physobs, wavelength)

# Display the query results
print("Query for HMI vector magnetic field data:")
print(query)

# Uncomment the line below to download the data
# files = Fido.fetch(query)
