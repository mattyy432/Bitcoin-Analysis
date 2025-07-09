# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd # data pre-processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np # import it for numerical computation on data 
import matplotlib.pyplot as plt ## data viz libraries 
import seaborn as sns
import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.express as px
from plotly.offline import download_plotlyjs , init_notebook_mode , plot , iplot




df = pd.read_csv(r'C:\Users\USER\Downloads\Bitcoin/bitcoin_price_Training - Training.csv')
df['Date'] = df['Date'].astype('datetime64[ns]')
df.sort_values(by = 'Date')
data = df.sort_index(ascending=False).reset_index()
data.drop('index', axis=1, inplace=True)
data.set_index('Date', inplace = True)
data['Close_price_pct_change'] = data['Close'].pct_change()*100
bitcoin_sample2 = data[0:31]






st.set_page_config(page_title= "Bitcoin Dashboard",
                   layout = 'wide')
st.title('Comprehensive Bitcoin Price Analysis Dashboard')


#First plot:
st.subheader("Bitcoin Candlestick Chart (July 2017)")


trace = go.Candlestick(x=bitcoin_sample2.index,
              high = bitcoin_sample2['High'],
               open = bitcoin_sample2['Open'],
               close = bitcoin_sample2['Close'],
              low = bitcoin_sample2['Low'])

candle_data = [trace]
layout = {'title':'Bitcoin Price(July 2017)',
          'xaxis': {'title':'Date'},
          'height':500
          }

fig_candle = go.Figure(data = candle_data, layout=layout)

st.plotly_chart(fig_candle , user_container_width = True)


## 2nd plot:
st.subheader('Daily Percentage Change in Closing Price')

fig_pct = go.Figure([
    go.Scatter(x= data.index,
               y = data['Close_price_pct_change'],
               mode = 'lines')
    ])


fig_pct.update_layout(
    xaxis_title = 'Date',
    yaxis_title = 'Percentage Change',
    template = 'plotly_white'
    )

st.plotly_chart(fig_pct , use_container_width = True)





## 3rd plot:
st.subheader('Bicoin Price Trends Over Time')
price_type = st.selectbox('Select Price Type:', options = ['Open', 'High', 'Low', 'Close'], index = 3
             )


fig_trend = go.Figure([
    go.Scatter(x= data.index,
               y = data[price_type],
               mode = 'lines')
    ])


fig_trend.update_layout(
    title = price_type + 'Price Over Time',
    xaxis_title = 'Date',
    yaxis_title = 'Price(USD)',
    template = 'plotly_white'
    )

st.plotly_chart(fig_trend , use_container_width = True)

## 4th plot:

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader('Yearly Average Close Price')
    yearly_avg = data['Close'].resample('YE').mean()
    fig_year = px.bar(
        x = yearly_avg.index.strftime('%Y'),
        y = yearly_avg.values ,
        labels = {'x':'Year', 'y':'Average value'},
        title = 'Yearly avg trend'
        )
    
    st.plotly_chart(fig_year , use_container_width = True)

    
with col2:
    st.subheader('Quarterly Average Close Price')
    quarterly_avg = data['Close'].resample('QE').mean()
    fig_quarterly = px.bar(
        x = quarterly_avg.index.strftime('%Y'),
        y = quarterly_avg.values ,
        labels = {'x':'Quarter', 'y':'Average value'},
        title = 'Quarterly avg trend'
        )
    
    st.plotly_chart(fig_quarterly, use_container_width = True)



with col3:
    st.subheader('Quarterly Average Close Price')
    monthly_avg = data['Close'].resample('ME').mean()
    fig_month = px.line(
        x = monthly_avg.index ,
        y = monthly_avg ,
        labels = {'x':'Month', 'y':'Average value'},
        title = 'Monthly avg trend'
        )
    
    st.plotly_chart(fig_month, use_container_width = True)
    
    
    
    
## 5th plot:
    
col4, col5 = st.columns(2)

with col4:
    st.subheader('Closing Price (Normal Scale)')
    
    fig_normal = px.line(
        data_frame = data,
        x = data.index,
        y = 'Close' ,
        labels = {'x':'Date', 'y':'Closing price'},
        title = 'Bitcoin Closing Price Trend (Normal Scale) '
        )
    
    st.plotly_chart(fig_normal , use_container_width = True)
    

with col5:
    st.subheader('Closing Price (Log Scale)')
    
    fig_log = px.line(
        data_frame = data,
        x = data.index,
        y =np.log1p(data['Close'] ),
        labels = {'x':'Date', 'y':'log(Closing price + 1)'},
        title = 'Bitcoin Closing Price Trend (Log Scale) '
        )
    
    st.plotly_chart(fig_log , use_container_width = True)
    
    
    
    