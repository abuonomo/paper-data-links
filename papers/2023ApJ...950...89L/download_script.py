# This script was generated by an AI model and has not been reviewed by a human expert. Please use with caution.

from sunpy.net import Fido, attrs as a

# Define the time range for GME on IMP-8
gme_time_range = a.Time('1973-11-01', '2001-10-31')

# Since the specific instrument and detector are not available in VSO via SunPy, we note this:
print("GME data from IMP-8 needs to be accessed from specialized IMP-8 data archives.")

# Example of how it would look if it were available:
# gme_query = Fido.search(gme_time_range, a.Instrument('GME'))

# Print the query result (if it were possible)
# print("Query for GME on IMP-8:")
# print(gme_query)

# Uncomment the line below to download the data if it were available
# gme_files = Fido.fetch(gme_query)

# Define the time range for ERNE on SOHO
erne_time_range = a.Time('2001-10-01', '2006-12-31')

# Query for ERNE data
erne_query = Fido.search(erne_time_range, a.Instrument('ERNE'))

# Print the query result
print("Query for ERNE on SOHO:")
print(erne_query)

# Uncomment the line below to download the data
# erne_files = Fido.fetch(erne_query)

# Define the time range for SEPEM on GOES
sepem_time_range = a.Time('2001-01-01', '2016-12-31')  # Adjusted to cover the study period

# Since SEPEM is not directly queryable via SunPy's Fido, we note this:
print("SEPEM data from GOES needs to be accessed from specialized GOES data archives or SEPEM reference datasets.")

# Example of how it would look if it were available:
# sepem_query = Fido.search(sepem_time_range, a.Instrument('SEPEM'))

# Print the query result (if it were possible)
# print("Query for SEPEM on GOES:")
# print(sepem_query)

# Uncomment the line below to download the data if it were available
# sepem_files = Fido.fetch(sepem_query)