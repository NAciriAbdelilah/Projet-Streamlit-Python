# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import data



# Config
st.set_page_config(page_title='Modéle Risque Corpo', page_icon=':bar_chart:', layout='wide')

# Title
st.title('💰 Modéle Risque Corpo')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# Data Sources
swaps_types_overview = data.get_data('Swaps Types Overview')
swaps_types_daily = data.get_data('Swaps Types Daily')
swaps_assets_overview = data.get_data('Swaps Assets Overview')
swaps_assets_daily = data.get_data('Swaps Assets Daily')
