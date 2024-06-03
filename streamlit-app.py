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
The CalTrans D7 currently supports 100X as many miles of highways for cars as
protected bike lanes.
""")


fig = px.bar(x=['Highways for cars', 'Seperated Bike Lanes'], y=[1170, 11])
fig.update_layout(yaxis_title = "Miles in D7")
st.plotly_chart(fig)


# -- Plot target for bike lanes vs time
#fig = px.line(df, x='Year', y=['Bike Lane Miles', 'Target'])
#st.plotly_chart(fig)

st.write("# Progress")

st.write("""In order to achieve the CalTrans CAT plan vision, the
CalTrans D7 CSAC has recommended a target of building 50 miles of protected
bike lanes per year.  This would be similar to targets set by other major
U.S. cities, such as New York City.""")


st.write("""
 * Protected bike lanes built in 2022: 0 Miles (Target: N/A)
 * Protected bike lanes buitl in 2023: 0 Miles (Target: N/A)
 * Protected bike lanes built in 2024: 0 Miles (Target: 50 miles)
""")

# -- Plot bike lanes built per year
fig = px.bar(x=['Year 2022', 'Year 2023', 'Year 2024'], y=[0, 0, 0])
fig.update_layout(yaxis_title = "Miles of protected bike lanes built")
fig.add_hline(y=50)
st.plotly_chart(fig)


# Community Partnerships

st.write("""
## COORDINATION WITH ACTIVE AND ONGOING LOCAL AND REGIONAL PLANS

Local and regional public agencies provided active transportation
infrastructure and planning data from completed and ongoing plans,
as well as other input that was used to identify the location-based
needs that are included in the Plan. Caltrans continues to collect
information from stakeholders and the public about local needs through
its online surveys and other efforts. Caltrans continues to partner
with agencies and communities to ensure that where possible, projects
within the state, local, and regional transportation systems improve
connectivity to existing and planned bicycle, pedestrian, and transit
facilities.
""")

st.write("""
### Status
* Los Angeles Mobility Plan: CalTrans D7 has provided $0 of support for this plan, helping to construct 0 miles of protected bike lanes.
* Los Angeles County Bicycle Plan: CalTrans has provided $0 of support for this plan, helping to construct 0 miles of protected bike lanes.
* Emerald Necklace: CalTrans has provided $0 of support for this plan, helping
to construct 0 miles of protected bike lanes.
""")


st.write("# CalTrans D7 Current Projects")

st.write("""

[D7 Current Project Page](https://dot.ca.gov/caltrans-near-me/district-7/district-7-projects)

## Projects for cars

 * The Tramonto Slide State Route 1 at Porto Marina Way
 * State Route 27 Topanga Canyon Slide Update
 * Pacific Coast Highway South Bay to Santa Monica Pavement Rehabilitation
 * State Route 39 Emergency Repairs
 * State Route 33 Emergency Repairs
 * Pacific Coast Highway LA County Line to Torrance Pavement Rehabilitation
 * State Route 2 Emergency Highway Repairs
 * State Route 150 Recovery Plan
 * Interstate 5 Pavement Preservation Project
 * State Route 134 Pioneers/Arroyo Seco Bridge Barrier Upgrade Project
 * U.S. 101 Water Repair Project in Ventura
 * I-605 Freeway Enhancements Project: $285 million to help cars move on I-605
 * I-405 Western Avenue to Crenshaw Blvd Auxiliary Lanes Project: $62 million to add lanes to I-405
 * SR-71 Expressway to Freeway Conversion Project: $174 million to move cars slightly faster on the SR-71 freeway
 * SR-57 Pavement Replacement Project
 * I-405 Sepulveda Pass ExpressLanes: $260 million to move cars slightly faster on the I-405
 * State Route 1 (SR-1) Permanent Slope Restoration
 * I-210 Connected Corridors Pilot Project
 * Pearblossom Highway Pavement Rehabilitation and Pedestrian Upgrade Project
 * Comprehensive Multimodal Corridor Planning (CMCP) Project
 * US 101 Pavement Rehabilitation Project
 * US 101 Wallis Annenberg Wildlife Crossing at Liberty Canyon
 * Mugu Secant Walls Project
 * Topanga Canyon Repaving Project

 * Additional freeway expansions in District 7 are tracked at: https://www.destructionfornada.com

## Projects for bikes

 * Santa Monica Blvd. Bike Lane Project: This project would add 0.2 miles of bike lane, which may or may not be protected

 * Pacific Coast Highway Safety Projects: This project includes some
protected bike lanes in Long Beach.  Details are not available at this time.
""")

st.write("""
## Project Summary

To help car mobility, CalTrans D7 currently has
24 projects in progress, with expected costs 
of ***billions*** of dollars.

To help cyclist mobility, there are currently two projects
planned, with the potential to add
an estimated 0.2 miles of protected bike lanes.  

""")
