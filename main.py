import streamlit as st
import pandas as pd
import numpy as np

dataloc = '../../graduation_project/the_project/Classification/output/regions/north_america_australia/genral_labeled_data_with_relative_traffic_rates/Entertainment/USA_with_relative_traffic_rates.csv'
data = pd.read_csv(dataloc)

st.write("# Simple placeholder streamlit app")

st.write("## Data table")
st.write(data)


chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=["X","Y","Z"]
)

st.write("## Visulaizing random data in differnet styles")

st.bar_chart(chart_data)
st.area_chart(chart_data)
st.line_chart(chart_data)

st.link_button("Back to smilai", "#")
