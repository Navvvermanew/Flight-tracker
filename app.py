
import streamlit as st
import pandas as pd
from db import get_flights, get_delays

st.title("\nFlight Booking & Delay Tracker")

menu = st.sidebar.selectbox("Choose Option", ["All Flights", "Delay Reports"])

if menu == "All Flights":
    st.subheader("📋 Flight Schedule")
    flights = pd.DataFrame(get_flights())
    st.dataframe(flights)

elif menu == "Delay Reports":
    st.subheader("🕑 Flight Delays")
    delays = pd.DataFrame(get_delays())
    avg_delay = delays["delay_minutes"].mean() if not delays.empty else 0
    st.metric("Average Delay (mins)", round(avg_delay, 2))
    st.dataframe(delays)

    if not delays.empty:
        st.bar_chart(delays.groupby("airline")["delay_minutes"].sum())
