import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample data (replace with your actual data)
np.random.seed(0)
dates = pd.date_range('2023-01-01', periods=100)
prices = pd.DataFrame(np.random.randn(100, 3), index=dates, columns=['Stock1', 'Stock2', 'Stock3'])

# Set page title
st.set_page_config(page_title="QUANT HARP", layout="wide")

# Sidebar
st.sidebar.title('QUANT HARP')
selected_tool = st.sidebar.selectbox('Select Tool', ['Stock Price Analysis', 'Tool 1', 'Tool 2', 'Tool 3'])

# Main content
st.title('QUANT HARP Investment Dashboard')

if selected_tool == 'Stock Price Analysis':
    st.subheader('Stock Price Analysis')
    selected_stock = st.sidebar.selectbox('Select Stock', prices.columns)
    
    st.write(prices)

    st.subheader('Stock Price Line Chart')
    st.line_chart(prices[selected_stock])

    # Daily returns
    returns = prices.pct_change(1)
    st.subheader('Daily Returns')
    st.write(returns)

    # Histogram of daily returns
    st.subheader('Histogram of Daily Returns')
    plt.figure(figsize=(10, 6))
    plt.hist(returns[selected_stock].dropna(), bins=20, edgecolor='black')
    plt.xlabel('Return')
    plt.ylabel('Frequency')
    st.pyplot(plt)

    # Cumulative returns
    cum_returns = (1 + returns).cumprod()
    st.subheader('Cumulative Returns')
    st.write(cum_returns)

elif selected_tool == 'Tool 1':
    st.subheader('Tool 1')
    st.write('Tool 1 content will go here.')
    # Placeholder for Tool 1 implementation

elif selected_tool == 'Tool 2':
    st.subheader('Tool 2')
    st.write('Tool 2 content will go here.')
    # Placeholder for Tool 2 implementation

elif selected_tool == 'Tool 3':
    st.subheader('Tool 3')
    st.write('Tool 3 content will go here.')
    # Placeholder for Tool 3 implementation

# Closing remarks
st.markdown("""
    *Note: This is a demo investment dashboard. Replace sample data and analysis with your own.*
""")
