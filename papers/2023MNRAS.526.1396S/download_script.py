# This script was generated by an AI model and has not been reviewed by a human expert. Please use with caution.

from sunpy.net import Fido, attrs as a
from astropy import units as u

# Define the observation dates and details for SUMER on SOHO as mentioned in the study
sumer_dates = ['1997-04-20', '1999-10-09']
sumer_instrument = a.Instrument("SUMER")
sumer_wavelength_range = a.Wavelength(660 * u.angstrom, 1610 * u.angstrom)

# Create queries for each specific observation date
for date in sumer_dates:
    start_time = f"{date}T00:00:00"
    end_time = f"{date}T23:59:59"
    time_range = a.Time(start_time, end_time)
    
    # Construct the query
    query = Fido.search(time_range, sumer_instrument, sumer_wavelength_range)
    
    # Display the query results
    print(f"Query for SUMER observations on {date}:")
    print(query)

    # Uncomment the line below to download the data
    # files = Fido.fetch(query)