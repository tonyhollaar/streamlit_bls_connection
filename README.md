# Streamlit Connection API
The Streamlit Connection API is a custom-built Python package that allows you to easily interact with the U.S. Bureau of Labor Statistics (BLS) API and retrieve data as pandas dataframes.

## Installation

To install the Streamlit Connection API, simply run the following command:
```python
pip install streamlit-bls-connection
```

## Example Streamlit API:

```python
import streamlit as st
from streamlit_bls_connection import BLSConnection

# Step 1: Setup connection to US Bureau of Labor Statistics
connection = BLSConnection("bls_connection")

# Step 2: Define Input parameters for the API call
# Tip: one or multiple Series ID's* can be retrieved
seriesids_list = ['APU000074714', 'APU000072610']
start_year_str = '2014'  # start of date range
end_year_str = '2023'    # end of date range

# Step 3: Fetch data using the custom connection
dataframes_dict = connection.query(seriesids_list, start_year_str, end_year_str)

# Step 4: Create dataframes
gas_df = dataframes_dict['APU000074714']
electricity_df = dataframes_dict['APU000072610']

# Step 5: Show Dataframes in Streamlit
st.dataframe(gas_df, electricity_df)
```

## Requirements
- Python 3.8 and above

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions, suggestions, or contributions, please visit my [GitHub Profile](https://github.com/tonyhollaar).