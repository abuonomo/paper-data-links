# This script was generated by an AI model and has not been reviewed by a human expert. Please use with caution.

from sunpy.net import Fido, attrs as a
from astropy import units as u

# Define the observation date for the SEP event
event_date = '2021-10-09'

# EPD on Solar Orbiter: Observations of energetic particles
epd_instrument = a.Instrument("EPD")
epd_time_range = a.Time(event_date + "T00:00:00", event_date + "T23:59:59")
epd_query = Fido.search(epd_time_range, epd_instrument)

# STIX on Solar Orbiter: Observation of hard X-ray emissions
stix_instrument = a.Instrument("STIX")
stix_time_range = a.Time(event_date + "T00:00:00", event_date + "T23:59:59")
stix_query = Fido.search(stix_time_range, stix_instrument)

# Display the query results for EPD and STIX instruments
print("Query for EPD observations on Solar Orbiter:")
print(epd_query)
print("Query for STIX observations on Solar Orbiter:")
print(stix_query)

# Uncomment the lines below to download the data
# epd_files = Fido.fetch(epd_query)
# stix_files = Fido.fetch(stix_query)
