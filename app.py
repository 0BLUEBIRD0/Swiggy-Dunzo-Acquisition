# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Swiggy-Dunzo Acquisition", layout="wide")
st.title("Swiggy-Dunzo Acquisition Simulator")

# Load charts
charts = {
    "Market Growth": "01_market_growth.png",
    "GMV Forecast": "02_gmv_forecast.png",
    "Consumer Segment": "03_consumer_segment.png",
    "Word Cloud": "05_sentiment_wordcloud.png"
}

cols = st.columns(2)
for i, (title, img) in enumerate(charts.items()):
    with cols[i % 2]:
        try:
            st.image(f"visualizations/{img}", caption=title, use_column_width=True)
        except:
            st.write(f"*{title} not found*")

# --- Simulator ---
st.sidebar.header("Acquisition Parameters")
price = st.sidebar.slider("Dunzo Price (USD M)", 100, 500, 200)
synergy = st.sidebar.slider("Synergy Lift (%)", 10, 50, 25)
wacc = st.sidebar.slider("WACC (%)", 12, 25, 18) / 100

npv = synergy * 5 - price
roi = (npv / price) * 100

col1, col2 = st.columns(2)
col1.metric("NPV", f"${npv:.0f}M")
col2.metric("ROI", f"{roi:+.1f}%")

if npv > 0:
    st.success("ACQUISITION RECOMMENDED")
else:
    st.error("VALUE DESTRUCTION")