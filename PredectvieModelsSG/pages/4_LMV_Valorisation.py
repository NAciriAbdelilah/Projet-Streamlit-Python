# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import data


# Config
st.set_page_config(page_title='Swaps - Cross Chain Monitoring', page_icon=':bar_chart:', layout='wide')

# Title
st.title('Modéle Valorisation LMV')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# Data Sources
swaps_overview = data.get_data('Swaps Overview')
swaps_daily = data.get_data('Swaps Daily')
swaps_heatmap = data.get_data('Swaps Heatmap')
