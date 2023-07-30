![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![PyPI](https://img.shields.io/pypi/v/streamlit-bls-connection)
![Python: 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PyPI Version](https://img.shields.io/pypi/v/streamlit-bls-connection.svg)

<div align="center">
  <img src="https://raw.githubusercontent.com/tonyhollaar/streamlit_bls_connection/main/logo.svg"><br>
</div>

## Description
The `streamlit-bls-connection` package allows you to easily interact with the U.S. Bureau of Labor Statistics (BLS) API and retrieve data as pandas dataframes and display them in [`Streamlit`](https://docs.streamlit.io/) !

## How to use `streamlit-bls-connection`
To run the Streamlit app locally on your machine, follow these steps:

### Installation
1. Install the `streamlit-bls-connection` package and its dependencies by running the following command in your terminal or command prompt:

```bash
pip install streamlit-bls-connection
```

### Create .py file
2. Create a new Python script  with your favorite text editor (e.g., VSCode, Spyder, Notepad++), name it `app.py` and copy/paste below code and save changes.
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

## Use in Google Colab
If you want to try it out in the cloud, to see the `streamlit-bls-connection` with a Streamlit app in action, you can click the link below!

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tonyhollaar/streamlit_bls_connection/blob/main/example_googlecolab_streamlit_bls_connection.ipynb)