import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import seaborn as sns

st.title('Planets Dashboard')


with st.sidebar:
    # 1st widget
    label1 = 'Select PLANETS to compare with Earth!'
    planets = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    selected_planets =  st.multiselect(label=label1, options=planets)

    # 2nd widget
    label2 = 'Select METRICS to compare!'
    metrics = ['Orbit Distance(km)', 'Equatorial Radius(km)', 'Volume(km3)', 'Mass(kg)', 'Density(g/cm3)', \
        'Escape Velocity(km/h)', 'Rotation Period(Earth Days)', 'Orbit Period(Earth Years)', 'Mean Orbit Velocity(km/h)', \
        'Orbit Eccentricity', 'Orbit Inclination(degrees)', 'Equatorial Inclination(degrees)', 'Mean Temperature(°C)', 'Atmospheric Constituents',  \
        'Moons', 'Rings']
    selected_metrics = st.multiselect(label=label2, options=metrics)

    # test
    #selected_planets = ['Venus', 'Mercury']
    #selected_metrics = ['Equatorial Radius(km)', 'Density(g/cm3)']



# Load function
#@st.cache
def load_data(selected_planets):
    df = pd.read_csv('../data/data.csv')
    df.set_index('Planet', inplace=True)
    df_T = df.T
    combo_df = df_T[selected_planets]
    new_combo_df = combo_df.T
    new_combo_df.reset_index(inplace=True)

    return new_combo_df


# Load data
with st.spinner('Loading data...'):
    df = load_data(selected_planets)
st.success('Loading data... Done!', icon="✅")


# Create a subheader
st.subheader('Selected planets')
st.write(df)

# Print selected metrics
#st.subheader('Selected metrics')
for metric in selected_metrics:
    if metric in ['Orbit Distance(km)', 'Equatorial Radius(km)', 'Volume(km3)', 'Mass(kg)', 'Density(g/cm3)', \
        'Escape Velocity(km/h)', 'Rotation Period(Earth Days)', 'Orbit Period(Earth Years)', 'Mean Orbit Velocity(km/h)', \
        'Orbit Eccentricity', 'Orbit Inclination(degrees)', 'Equatorial Inclination(degrees)', 'Mean Temperature(°C)',  \
        'Moons']:
        st.subheader(f'{metric}')
        fig = plt.figure(figsize=(8, 4))
        ax = sns.barplot(data=df, x=df['Planet'], y=df[metric])
        #ax.set_title(f'{metric.upper()}')
        ax.bar_label(ax.containers[0])
        st.pyplot(fig)
    elif metric == 'Rings':
        st.subheader('Rings')
        st.write(df.Rings)
    else:
        st.subheader('Atmospheric Constituents')
        st.write(df['Atmospheric Constituents'])




#if __name__ == '__main__':
 #   main()
