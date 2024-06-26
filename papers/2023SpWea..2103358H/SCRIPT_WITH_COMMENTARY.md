# This script was generated by an AI model and has not been reviewed by a human expert. Please use with caution.

```python
from sunpy.net import Fido, attrs as a
from astropy import units as u

# Define the observation period for the study of CMEs in 2011
start_date = '2011-01-01'
end_date = '2011-12-31'
time_range = a.Time(start_date, end_date)

# LASCO on SOHO: Key instrument for studying Coronal Mass Ejections (CMEs)
# Detectors: C2 and C3 for capturing different stages of CME propagation
lasco_instrument = a.Instrument("LASCO")
detector_c2 = a.Detector("C2")  # C2 detector for LASCO
detector_c3 = a.Detector("C3")  # C3 detector for LASCO

# Construct queries for LASCO C2 and C3 detectors
lasco_c2_query = Fido.search(time_range, lasco_instrument, detector_c2)
lasco_c3_query = Fido.search(time_range, lasco_instrument, detector_c3)

# SECCHI instruments on STEREO spacecraft
# COR-2 and HI (Heliospheric Imagers) for observing CMEs from different vantage points
secchi_instrument = a.Instrument("SECCHI")
cor2_detector = a.Detector("COR2")  # COR-2 detector for SECCHI
hi1_detector = a.Detector("HI1")  # HI-1 detector for SECCHI
hi2_detector = a.Detector("HI2")  # HI-2 detector for SECCHI

# Construct queries for SECCHI COR-2, HI-1, and HI-2 on both STEREO A and B
stereo_a = a.Source("STEREO_A")
stereo_b = a.Source("STEREO_B")
cor2_query_a = Fido.search(time_range, secchi_instrument, cor2_detector, stereo_a)
cor2_query_b = Fido.search(time_range, secchi_instrument, cor2_detector, stereo_b)
hi1_query_a = Fido.search(time_range, secchi_instrument, hi1_detector, stereo_a)
hi1_query_b = Fido.search(time_range, secchi_instrument, hi1_detector, stereo_b)
hi2_query_a = Fido.search(time_range, secchi_instrument, hi2_detector, stereo_a)
hi2_query_b = Fido.search(time_range, secchi_instrument, hi2_detector, stereo_b)

# Display the query results for LASCO and SECCHI instruments
print("Query for LASCO C2 Detector Data:")
print(lasco_c2_query)
print("Query for LASCO C3 Detector Data:")
print(lasco_c3_query)
print("Query for SECCHI COR-2 Detector Data (STEREO A):")
print(cor2_query_a)
print("Query for SECCHI COR-2 Detector Data (STEREO B):")
print(cor2_query_b)
print("Query for SECCHI HI-1 Detector Data (STEREO A):")
print(hi1_query_a)
print("Query for SECCHI HI-1 Detector Data (STEREO B):")
print(hi1_query_b)
print("Query for SECCHI HI-2 Detector Data (STEREO A):")
print(hi2_query_a)
print("Query for SECCHI HI-2 Detector Data (STEREO B):")
print(hi2_query_b)

# Uncomment the lines below to download the data
# lasco_c2_files = Fido.fetch(lasco_c2_query)
# lasco_c3_files = Fido.fetch(lasco_c3_query)
# cor2_files_a = Fido.fetch(cor2_query_a)
# cor2_files_b = Fido.fetch(cor2_query_b)
# hi1_files_a = Fido.fetch(hi1_query_a)
# hi1_files_b = Fido.fetch(hi1_query_b)
# hi2_files_a = Fido.fetch(hi2_query_a)
# hi2_files_b = Fido.fetch(hi2_query_b)
```

This script is designed to query and potentially download data for the specified instruments and time range, focusing on the observation of CMEs as described in the context. The queries are structured to reflect the data used in the context, adhering strictly to the directive provided.
