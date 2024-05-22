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

highwaymiles = 1173
bikelanemiles = 0.01*highwaymiles

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


st.write("## Current state of bike routes")

st.metric("Highway miles", highwaymiles)

st.metric("Seperated bike lane miles", int(bikelanemiles))

st.write("## Equity")

st.write("""
The CalTrans D7 CAT plan sets a goal of establishing equity in
transportation.  Currently, there are 100X  as many miles of highways for
cars as there are safe bike routes.  This is clearly not an equitable system!
Equity in transportation requires that CalTrans build as many miles
of high quality bike routes as they currently maintain for cars.
""")


fig = px.bar(x=['Highways for cars', 'Seperated Bike Lanes'], y=[1170, 11])
fig.update_layout(yaxis_title = "Miles in D7")
st.plotly_chart(fig)








# -- Plot target for bike lanes vs time
fig = px.line(df, x='Year', y=['Bike Lane Miles', 'Target'])
st.plotly_chart(fig)




