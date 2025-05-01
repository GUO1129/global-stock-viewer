
import streamlit as st
import yfinance as yf
import mplfinance as mpf
import pandas as pd

st.set_page_config(page_title="全球股市預測", page_icon="💹")

st.title("全球股市資料與 K 線圖展示")

# 使用者輸入股票代碼
ticker = st.text_input("輸入股票代碼（例如：2330.TW、AAPL、0700.HK）", value="2330.TW")
period = st.selectbox("選擇資料區間", options=["1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"], index=1)

if st.button("顯示股票 K 線圖"):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period=period)
        if data.empty:
            st.error("查無資料，請確認代碼是否正確")
        else:
            st.success(f"成功取得 {ticker} 資料，共 {len(data)} 筆")
            fig, _ = mpf.plot(data, type='candle', style='charles', title=f"{ticker} K 線圖", volume=True, returnfig=True)
            st.pyplot(fig)
    except Exception as e:
        st.error(f"發生錯誤：{str(e)}")
