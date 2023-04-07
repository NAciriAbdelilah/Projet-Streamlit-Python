# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import data

# Config
st.set_page_config(page_title='Modéle Dépôt Client', page_icon=':bar_chart:', layout='wide')

# Title
st.title('Modéle Dépôt Client')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# Data Sources
swaps_dexs_overview = data.get_data('Swaps DEXs Overview')
swaps_dexs_daily = data.get_data('Swaps DEXs Daily')

