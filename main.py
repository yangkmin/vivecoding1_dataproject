import streamlit as st
import folium
from streamlit_folium import st_folium

# 스트림릿 앱 제목
st.title("나만의 북마크 지도 📍")

# 장소 데이터 입력
bookmark_places = [
    {'name': '서울시청', 'lat': 37.5665, 'lng': 126.9780, 'desc': '서울의 중심!'},
    {'name': '경복궁', 'lat': 37.5796, 'lng': 126.9770, 'desc': '조선의 궁궐'},
    {'name': '남산타워', 'lat': 37.5512, 'lng': 126.9882, 'desc': '서울 전망 명소'},
    {'name': '명동', 'lat': 37.5636, 'lng': 126.9827, 'desc': '쇼핑과 맛집의 거리'},
    {'name': '홍대입구', 'lat': 37.5572, 'lng': 126.9245, 'desc': '젊음의 거리'}
]

# folium 지도 생성
center = [bookmark_places[0]['lat'], bookmark_places[0]['lng']]
m = folium.Map(location=center, zoom_start=12)

# 마커 추가
for place in bookmark_places:
    folium.Marker(
        [place['lat'], place['lng']],
        popup=f"<b>{place['name']}</b><br>{place['desc']}",
        tooltip=place['name'],
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

# folium 지도를 streamlit에 표시
st_data = st_folium(m, width=700, height=500)
