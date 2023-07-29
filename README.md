<div align="center">
  <img src="https://raw.githubusercontent.com/tonyhollaar/streamlit_bls_connection/main/logo.svg"><br>
</div>

## Description
The Streamlit Connection API is a custom-built Python package that allows you to easily interact with the U.S. Bureau of Labor Statistics (BLS) API and retrieve data as pandas dataframes and display them in Streamlit!

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
st.dataframe(gas_df)
st.dataframe(electricity_df)
```
## Running the Streamlit App with streamlit-bls-connection

To run the Streamlit app locally on your machine, follow these steps:

1. Install the Streamlit Connection API package and its dependencies by running the following command in your terminal or command prompt:

```bash
pip install streamlit-bls-connection
```

2. Create a new Python script  with your favorite text editor (e.g., VSCode, Spyder, Notepad++), name it app.py and copy/paste below code and save changes.
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
st.dataframe(gas_df)
st.dataframe(electricity_df)
```

3. In your terminal or command prompt, navigate to the directory where your Python script is located.
```bash
cd /path/to/your/python/script
```
4. Run the Streamlit app using the following command:
```bash
streamlit run app.py
```
5. See your results in the browser of your Streamlit App!


## Requirements
- Python version 3.8 and above
- Streamlit version 1.25.0

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions, suggestions, or contributions, please visit my [GitHub Profile](https://github.com/tonyhollaar).

## Reporting Issues

If you encounter any problems, have questions, or want to request a new feature, please feel free to open an issue on [GitHub](https://github.com/tonyhollaar/streamlit_bls_connection/issues). I appreciate your feedback and will do our best to address any concerns promptly.

When reporting an issue, please provide as much detail as possible, including the version of the package, the Python version, and a clear description of the problem or feature request. This will help me better understand and resolve the issue quickly.

Thank you for your contributions to making this package better!