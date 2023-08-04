![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python: 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PyPI Version](https://img.shields.io/pypi/v/streamlit-bls-connection.svg)

<div align="center">
  <img src="https://raw.githubusercontent.com/tonyhollaar/streamlit_bls_connection/main/logo.svg"><br>
</div>

# Table of Contents
- [Description](#description)
- [How to use streamlit-bls-connection](#how-to-use-streamlit-bls-connection)
    - [Installation](#installation)
    - [Create .py file](#create-py-file)
    - [In terminal set file path of folder containing .py file](#in-terminal-set-file-path-of-folder-containing-py-file)
    - [Run Streamlit App](#run-streamlit-app)
- [Documentation](#documentation)
- [Requirements](#requirements)
- [License](#license)
- [Contact](#contact)
- [Reporting Issues](#reporting-issues)
- [Acknowledgements](#acknowledgements)
- [Use in Google Colab](#use-in-google-colab)
- [Streamlit Demo](#streamlit-demo)

## Description
The `streamlit-bls-connection` Python package allows you to easily interact with the U.S. Bureau of Labor Statistics (BLS) API and retrieve data as pandas dataframes and display them in [`Streamlit`](https://docs.streamlit.io/) !

## How to use `streamlit-bls-connection`
To run the Streamlit app locally on your machine, follow these steps:

### Installation
1. Install the `streamlit-bls-connection` package and its dependencies by running the following command in your terminal or command prompt:

```bash
pip install streamlit_bls_connection
```

### Create .py file
2. Create a new Python script  with your favorite text editor (e.g., VSCode, Spyder, Notepad++), name it `app.py` and copy/paste below code and save changes.
```python
import streamlit as st
from streamlit_bls_connection import BLSConnection

# Step 1: Setup connection to US Bureau of Labor Statistics
conn = st.experimental_connection('bls', type=BLSConnection)

# Step 2: Define input parameters
# Tip: one or multiple Series ID's* can be retrieved
# find Series ID's on www.bls.gov > DATA TOOLS
seriesids_list = ['APU000074714', 'APU000072610']
start_year_str = '2014' # start of date range
end_year_str = '2023'   # end of date range

# Step 3: Fetch data using the custom connection
dataframes_dict = connection.query(seriesids_list,
                                   start_year_str, 
                                   end_year_str,
                                   api_key = None)

# Step 4: Create dataframes
gas_df = dataframes_dict['APU000074714']
electricity_df = dataframes_dict['APU000072610']

# Step 5: Show Dataframes in Streamlit
st.dataframe(gas_df)
st.dataframe(electricity_df)
```

### In terminal set file path of folder containing .py file
3. In your terminal or command prompt, navigate to the directory where your Python script is located.
```bash
cd /path/to/your/python/script
```
### Run Streamlit App
4. Run the Streamlit app using the following command:
```bash
streamlit run app.py
```
5. See your results in the browser of your Streamlit App!

### Documentation
`connection.query(seriesids: List[str], start_year: str, end_year: str, api_key: Optional[str] = None, catalog: bool = False, calculations: bool = False, annualaverage: bool = False, aspects: bool = False) -> Dict[str, pd.DataFrame]`

The `query` method of the `BLSConnection` class allows you to fetch data from the BLS API. Before using this method, you need to create a `BLSConnection` object using the `st.experimental_connection` function and import the `BLSConnection` class.

**Parameters:**

- `seriesids` (list of str):
    - **Description:** A list of strings representing the BLS time series data to fetch.
    - **Example:** `['APU000074714', 'APU000072610']`
    - **Note:** The Series IDs are unique identifiers for specific datasets or statistical measures available from the Bureau of Labor Statistics. You can find Series IDs on the BLS website's DATA TOOLS section.

- `start_year` (str):
    - **Description:** The start year for the data retrieval (inclusive), represented as a string.
    - **Example:** `'2014'`
    - **Note:** The data retrieval will begin from this year onwards.

- `end_year` (str):
    - **Description:** The end year for the data retrieval (inclusive), represented as a string.
    - **Example:** `'2023'`
    - **Note:** The data retrieval will include data up to and including this year.

- `api_key` (str, optional):
    - **Description:** The API key for accessing the BLS API. If provided, it enhances the data access capabilities, allowing for a larger number of requests.
    - **Example:** `'YOUR_API_KEY_HERE'`
    - **Note:** Without an API key, you might be subject to limitations on the number of requests you can make. To obtain an API key, you can register on the BLS website.

- `catalog`, `calculations`, `annualaverage`, `aspects` (bool, optional):
    - **Description:** Optional boolean parameters to include additional data fields for each time series.
    - **Default:** `False`
    - `catalog`: Whether to include catalog data for the series. Catalog data provides information about the series, such as the title and survey name. (Accessible only with an API key)
    - `calculations`: Whether to include calculated data for the series. Calculated data refers to additional statistics derived from the primary data series. (Accessible only with an API key)
    - `annualaverage`: Whether to include annual average data for the series. This field will be relevant if the series has data computed as annual averages. (Accessible only with an API key)
    - `aspects`: Whether to include additional aspects data for the series. Aspects data includes additional metadata or contextual information about the series. (Accessible only with an API key)
    - **Note:** Enabling any of these parameters with an API key will include the corresponding data fields in the returned DataFrames. This additional information can be useful for more detailed analysis and visualization of the data.

**Returns:** A dictionary with Series IDs as keys and DataFrames as values, containing the fetched BLS data for each series. Each DataFrame includes columns for 'date', 'value', '%_change_value', 'year', 'month', 'period'. If the API key is provided, 'seriesID', 'series_title', and 'survey_name' columns are also included in the DataFrames. Empty or all-None columns are excluded from the DataFrames.

## Requirements
- Python version 3.8 and above

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions, suggestions, or contributions, please visit my [GitHub Profile](https://github.com/tonyhollaar).

## Reporting Issues

If you encounter any problems, have questions, or want to request a new feature, please feel free to open an issue on [GitHub](https://github.com/tonyhollaar/streamlit_bls_connection/issues). I appreciate your feedback and will do our best to address any concerns promptly.

When reporting an issue, please provide as much detail as possible, including the version of the package, the Python version, and a clear description of the problem or feature request. This will help me better understand and resolve the issue quickly.

Thank you for your contributions to making this package better!

## Acknowledgments
Special thanks 👏 to the Streamlit team for creating an amazing framework for building interactive web apps with Python.

## Use in Google Colab
If you want to try it out in the cloud, to see the `streamlit-bls-connection` with a Streamlit app in action, you can click the link below!

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tonyhollaar/streamlit_bls_connection/blob/main/example_googlecolab_streamlit_bls_connection.ipynb)

## Streamlit Demo
If you want to see a showcase demo in Streamlit, click the link below!

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://bls-connection-demo.streamlit.app/)

