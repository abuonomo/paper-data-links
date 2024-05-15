# This script was generated by an AI model and has not been reviewed by a human expert. Please use with caution.

from sunpy.net import Fido, attrs as a
from astropy import units as u

# Define the observation period as mentioned in the context
start_date = '1998-01-01'
end_date = '2017-12-31'
time_range = a.Time(start_date, end_date)

# SOHO/EIT: Used for initial identification of CME source regions
eit_query = Fido.search(time_range, a.Instrument("EIT"), a.Wavelength(171*u.angstrom, 304*u.angstrom))

# SDO/AIA: Provides high-resolution images for detailed analysis of CME source regions
aia_query = Fido.search(time_range, a.Instrument("AIA"), a.Wavelength(171*u.angstrom, 304*u.angstrom))

# STEREO/SECCHI (COR-1, COR-2, EUVI): Multi-viewpoint observation of CMEs and their source regions
cor1_query = Fido.search(time_range, a.Instrument("COR1"))
cor2_query = Fido.search(time_range, a.Instrument("COR2"))
euvi_query = Fido.search(time_range, a.Instrument("EUVI"))

# Display the query results for each instrument
print("Query for SOHO/EIT data:")
print(eit_query)
print("Query for SDO/AIA data:")
print(aia_query)
print("Query for STEREO/COR-1 data:")
print(cor1_query)
print("Query for STEREO/COR-2 data:")
print(cor2_query)
print("Query for STEREO/EUVI data:")
print(euvi_query)

# Uncomment the lines below to download the data
# eit_files = Fido.fetch(eit_query)
# aia_files = Fido.fetch(aia_query)
# cor1_files = Fido.fetch(cor1_query)
# cor2_files = Fido.fetch(cor2_query)
# euvi_files = Fido.fetch(euvi_query)
