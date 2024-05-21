import streamlit as st
import pandas as pd
import numpy as np
import plotly
import plotly.express as px

apptitle = 'CalTrans D7 Active Transportation Dashboard'

st.write("## CalTrans D7 Active Transportation Dashboard")


# -- Input Data

year = np.arange(2023, 2040)
carmiles = 1173*np.ones(len(year))
bikemiles = 0.01*carmiles
bikegoal = 30*(year-year[0]) + bikemiles[0]

# -- Header
st.image('img/vision-caltrans.png')


# -- Format data frame
data = {
    'Year': year,
    'Highway Miles': carmiles,
    'Bike Lane Miles': bikemiles,
    'Target': bikegoal
    }

df = pd.DataFrame(data=data)


fig = px.line(df, x='Year', y=['Bike Lane Miles', 'Target'])

st.plotly_chart(fig)


