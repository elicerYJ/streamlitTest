import streamlit as st
import pandas as pd
import numpy as np

st.write("# Hello, world!")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.write("## Random data")
st.dataframe(chart_data)

st.write("## Line chart")
st.line_chart(chart_data)