import streamlit as st
import yfinance as yf
import pandas as pd
import datetime
import matplotlib.pyplot as plt

st.title("글로벌 시가총액 Top 10 기업 1년 주가 정보")

# Top 10 시가총액 기업 (2024년 기준, 티커와 기업명)
companies = {
    'AAPL': 'Apple',
    'MSFT': 'Microsoft',
    'NVDA': 'Nvidia',
    'GOOGL': 'Alphabet (Google)',
    'AMZN': 'Amazon',
    'META': 'Meta Platforms',
    'BRK-B': 'Berkshire Hathaway',
    'LLY': 'Eli Lilly',
    'TSLA': 'Tesla',
    'AVGO': 'Broadcom'
}

# 날짜 범위 설정
end_date = datetime.datetime.today()
start_date = end_date - datetime.timedelta(days=365)

# 선택 박스(기업 선택)
selected = st.multiselect("기업을 선택하세요 (복수 선택 가능)", list(companies.keys()), default=list(companies.keys()))

# 데이터 가져오기 및 시각화
for ticker in selected:
    st.subheader(f"{companies[ticker]} ({ticker})")
    df = yf.download(ticker, start=start_date, end=end_date)
    if df.empty:
        st.warning(f"{companies[ticker]}의 데이터가 없습니다.")
        continue

    st.write(f"최근 5개 거래일 정보:")
    st.dataframe(df.tail())

    # 주가 그래프 (종가)
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.plot(df.index, df['Close'], label="Close Price")
    ax.set_title(f"{companies[ticker]} 1년 주가 추이")
    ax.set_xlabel("날짜")
    ax.set_ylabel("종가(USD)")
    ax.legend()
    st.pyplot(fig)
