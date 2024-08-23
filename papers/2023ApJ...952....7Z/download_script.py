# This script was generated by an AI model and has not been reviewed by a human expert. Please use with caution.

from sunpy.net import Fido, attrs as a
from astropy import units as u

# Define the observation period for the study of CMEs
# Time range: 2010 to 2013
start_date = '2010-01-01'
end_date = '2013-12-31'
time_range = a.Time(start_date, end_date)

# LASCO on SOHO: Key instrument for studying Coronal Mass Ejections (CMEs)
lasco_instrument = a.Instrument("LASCO")
lasco_query = Fido.search(time_range, lasco_instrument)

# COR1 and COR2 on STEREO-A: Provides additional viewpoints for CME observations
cor1_a_instrument = a.Instrument("COR1")
cor2_a_instrument = a.Instrument("COR2")
stereo_a_time_range = a.Time(start_date, end_date)
cor1_a_query = Fido.search(stereo_a_time_range, cor1_a_instrument)
cor2_a_query = Fido.search(stereo_a_time_range, cor2_a_instrument)

# COR1 and COR2 on STEREO-B: Provides additional viewpoints for CME observations
cor1_b_instrument = a.Instrument("COR1")
cor2_b_instrument = a.Instrument("COR2")
stereo_b_time_range = a.Time(start_date, end_date)
cor1_b_query = Fido.search(stereo_b_time_range, cor1_b_instrument)
cor2_b_query = Fido.search(stereo_b_time_range, cor2_b_instrument)

# Display the query results for each instrument
print("Query for LASCO Data:")
print(lasco_query)
print("Query for STEREO-A COR1 Data:")
print(cor1_a_query)
print("Query for STEREO-A COR2 Data:")
print(cor2_a_query)
print("Query for STEREO-B COR1 Data:")
print(cor1_b_query)
print("Query for STEREO-B COR2 Data:")
print(cor2_b_query)

# Uncomment the lines below to download the data
# lasco_files = Fido.fetch(lasco_query)
# cor1_a_files = Fido.fetch(cor1_a_query)
# cor2_a_files = Fido.fetch(cor2_a_query)
# cor1_b_files = Fido.fetch(cor1_b_query)
# cor2_b_files = Fido.fetch(cor2_b_query)
