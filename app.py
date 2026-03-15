import streamlit as st
from streamlit_folium import st_folium
import folium

st.title("CellScouter - 基地局探索")

# 地図の初期設定（東京付近）
m = folium.Map(location=[35.6812, 139.7671], zoom_start=15)

# 地図を画面に表示
st_folium(m, width=700)