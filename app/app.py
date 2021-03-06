import streamlit as st
import pandas as pd
import numpy as np

"""
# James Bond
Here's our first attempt at using data to create a table:
"""

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000,2) / [5,9] + [37.76, -122.4],
    columns=['lat', 'lon']
)

st.map(map_data)