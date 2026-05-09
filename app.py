import streamlit as st
import pandas as pd
import sqlite3

st.title("🚀 TikTok Automation Dashboard")

# إدخال بيانات الـ API
with st.sidebar:
    st.header("Settings")
    client_id = st.text_input("TikTok Client ID")
    client_secret = st.text_input("TikTok Secret", type="password")

# عرض الفيديوهات المنتجة
st.subheader("Recent Videos")
if os.path.exists("output.mp4"):
    st.video("output.mp4")

# سجل العمليات
st.subheader("Upload History")
conn = sqlite3.connect('database.db')
df = pd.read_sql_query("SELECT * FROM uploads", conn)
st.table(df)
