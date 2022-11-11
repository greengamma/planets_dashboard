import streamlit as st
import pandas as pd
import numpy as np
import time
import seaborn as sns

st.title('Planets Dashboard')

def main():
    with st.sidebar:
        # 1st widget
        label1 = 'Select PLANETS to compare with Earth!'
        planets = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
        chosen_planets =  st.multiselect(label=label1, options=planets)

        # 2nd widget
        label2 = 'Select METRICS to compare!'
        metrics = ['Orbit Distance (km)', 'Equatorial Radius (km)', 'Volume (km³)', 'Mass (kg)', 'Density (g/cm³)', \
            'Escape Velocity (km/h)', 'Rotation Period (Earth Days)', 'Orbit Period (Earth Years)', 'Mean Orbit Velocity (km/h)', \
            'Orbit Eccentricity', 'Orbit Inclination', 'Equatorial Inclination', 'Mean Temperature (°C)', 'Atmospheric Constituents',  \
            'Moons', 'Rings']
        chosen_metrics = st.multiselect(label=label2, options=metrics)



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
st.success('Loading data... Done!', icon="✅")


# Create a subheader
st.subheader('Raw data')
st.write(df)

st.subheader('Distance from Earth')
#dist_values = sns.barplot(data=df, x='')



if __name__ == '__main__':
    main()
