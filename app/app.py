import streamlit as st
import pandas as pd
import numpy as np
import time
import seaborn as sns



st.title('Planets Dashboard')


# Load function
#@st.cache
def load_data():
    df = pd.read_csv('../data/data.csv')
    # df = df1.T
    # header = df.iloc[0]
    # df = df[1:]
    # df.columns = header
    return df


# Load data
with st.spinner('Loading data...'):
    df = load_data()
st.success('Loading data... Done!')


# Create a subheader
st.subheader('Raw data')
st.write(df)

st.subheader('Distance from Earth')
dist_values = sns.barplot(data=df, x='')
