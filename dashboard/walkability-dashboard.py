import streamlit as st
import pandas as pd
import geopandas as gpd
import leafmap.foliumap as leafmap 

# Pre-processing
mohali_crossings_df = gpd.read_file('shps/secondary_mohali_pred_deeplab_shapefile.shp')
gurgaon_crossings_df = gpd.read_file('shps/secondary_gurgaon_pred_deeplab_shapefile.shp')
mohali_tree_df = gpd.read_file('shps/mohali_merged.shp')

m_g = leafmap.Map(center=[40, -100], zoom=4)
m_g.add_basemap('HYBRID')
m_g.add_gdf(gurgaon_crossings_df, spin=True)

m_m = leafmap.Map(center=[-40, 100], zoom=4)
m_m.add_basemap("HYBRID")
m_m.add_gdf(mohali_crossings_df, spin=True)

m_mt = leafmap.Map(center=[-40, 100], zoom=4)
m_mt.add_basemap("HYBRID")
m_mt.add_gdf(mohali_tree_df, spin=True)


milestones_df = pd.DataFrame({'Index Version': [0, 1, 2, 3, 4],
                   'What we want to capture': ["Crossing Density", 
                                               "Footpath Coverage, Tree Cover", 
                                               "Lighting, Land Use (what's nearby?)", 
                                               "Walkable Space, Active Frontage, Encroachment", 
                                               "Cleanliness, Scenery, Seating Space"]})


#Actual page layout
#st.set_page_config(layout='wide')
st.title("Walkability Index")

with st.sidebar:
    st.markdown("### You like walking? Us too! Hear us out.")

st.markdown("A city built for walking is efficient, healthy, and happy! But is your neighborhood walkable? We're trying to find out..")
st.dataframe(milestones_df, hide_index=True)

st.markdown("## What would the outcomes look like?")
col1, col2 = st.columns(2)
with col1:
    st.markdown("### Gurugram")
    st.metric("Crossings per km", 1.399)
    m_g.to_streamlit(height=300)
with col2:
    st.markdown("### Mohali")
    st.metric("Crossings per km", 2.132)
    m_m.to_streamlit(height=300)
    
st.markdown("## Tree C")
col3, col4 = st.columns(2)
with col3:
    st.markdown("### Mohali")
    m_mt.to_streamlit(height=300)

st.markdown("## How do we do this?")
st.image('pics/example-images.png')
st.markdown("We use satellite images and street view images \
            and run computer vision algorithms to detect various \
            developments of infrastructure. Our algorithms use these \
            modalities jointly to provide robust and up-to-date information.")

st.markdown("### Why is this a good approach?")
st.markdown("Manual surveys are costly and time-taking. \
            Through these algorithms we will be able to do a global analysis \
            which provides intelligent insights to decision makers on the \
            state of infrastructure and the needs of the users. The system \
            will provide for a data-driven decision making on where infrastructure \
            needs to be developed and it's cost-benefit analysis.")

st.markdown("## Great! Who's doing this?")
col1, col2 = st.columns(2)

with col1:
    st.image("pics/anupam.jpeg", width=300)
    st.markdown("### Pedestrian professor")
    st.markdown("Anupam Sobti")
    st.markdown("### Pedestrians in training")
    st.markdown("Vaishnavi Rathi")
    st.markdown("Prachi Parakh")

with col2:
    st.image("pics/varchita.jpeg", width=300)
    st.markdown("### Pedestrian Research Fellow")
    st.markdown("Varchita Lalwani")

st.markdown("## Partners on the walk")

col1, col2 = st.columns(2)
with col1:
    st.image("pics/nagarro-logo.png")

with col2:
    st.image("pics/raahgiri-logo.jpeg")
