# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import data

# Global Variables
theme_plotly = None # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Config
st.set_page_config(page_title='Modéle Upgrade Carte', page_icon=':bar_chart:', layout='wide')

# Title
st.title('Modéle Upgrade Carte')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# Data Sources
transactions_overview = data.get_data('Transactions Overview')
transactions_daily = data.get_data('Transactions Daily')
transactions_heatmap = data.get_data('Transactions Heatmap')
transactions_fee_payers = data.get_data('Fee Payers')
