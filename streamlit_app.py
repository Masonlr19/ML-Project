import streamlit as st
from services.tradier_client import get_historical_data

st.set_page_config(page_title="Financial Assistant", layout="wide")
st.title("📈 ML Financial Assistant")

symbol = st.text_input("Enter a stock symbol (e.g., AAPL)", value="AAPL")

if st.button("Fetch Historical Data"):
    try:
        data = get_historical_data(symbol)
        st.json(data)
    except Exception as e:
        st.error(f"Error fetching data: {e}")
