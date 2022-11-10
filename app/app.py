import streamlit as st
import pandas as pd
import numpy as np
import time
import seaborn as snss


def main():
    with st.sidebar:
        # 1st widget
        label1 = 'Select planets to compare with Earth!'
        planets = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
        chosen_planets =  st.multiselect(label=label1, options=planets)

        # 2nd widget
        label2 = 'Select metrics to compare!'
        metrics = ['Orbit Distance (km)', 'Equatorial Radius (km)', 'Volume (km³)', 'Mass (kg)', 'Density (g/cm³)', \
            'Escape Velocity (km/h)', 'Rotation Period (Earth Days)', 'Orbit Period (Earth Years)', 'Mean Orbit Velocity (km/h)', \
            'Orbit Eccentricity', 'Orbit Inclination', 'Equatorial Inclination', 'Mean Temperature (°C)', 'Atmospheric Constituents',  \
            'Moons', 'Rings']
        chosen_metrics = st.multiselect(label=label2, options=metrics)





    # st.title('Planets Dashboard')
    # menu1 = ['All', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    # label1 = 'Select planets to compare with Earth!'
    # choice1 = st.sidebar.multiselect(label1, menu1)

    # menu2  = ['All', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    # label2 = 'Select planets to compare with Earth!'
    # choice2 = st.sidebar.multiselect(label2, menu2)


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
