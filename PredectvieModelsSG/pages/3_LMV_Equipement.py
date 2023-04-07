# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import data


# Config
st.set_page_config(page_title='Modéle Equipement LMV', page_icon=':bar_chart:', layout='wide')

# Title
st.title('Modéle Equipement LMV')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# Data Sources
transfers_overview = data.get_data('Transfers Overview')
transfers_daily = data.get_data('Transfers Daily')
transfers_heatmap = data.get_data('Transfers Heatmap')
transfers_distribution = data.get_data('Transfers Distribution')
transfers_transferring_users = data.get_data('Transfers Transferring Users')
transfers_wallet_types = data.get_data('Transfers Wallet Types')
