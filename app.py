import streamlit as st
from PIL import Image
import time
import requests
from pathlib import Path
from streamlit_lottie import st_lottie

# Load Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Setup
st.set_page_config(page_title="Man_Analytics Portfolio Blog", layout="wide")
lottie_animation = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json")

# Header layout
col1, col2 = st.columns([1, 3])
with col1:
    image = Image.open("assets/usman_profile.jpg")
    st.image(
        image,
        caption="Usman Idris Abdulrahman\n\nSenior Analyst and Team Lead,\nDomestic Settlement and Reconciliation",
        use_container_width=True
    )
with col2:
    st.markdown("## About Me")
    st.write("""
Usman Idris Abdulrahman is a multifaceted professional combining a decade of banking experience with cutting-edge data science expertise. As a Senior Analyst and Team Lead at Jaiz Bank Plc, he has led national-level ATM and POS reconciliation initiatives, designed intelligent GL proofing workflows, and implemented fraud monitoring systems using predictive analytics.

With formal training in statistics, SQL, Power BI, and Python, Usman has mastered tools that allow for both traditional business intelligence reporting and modern AI application development. He has deployed multiple end-to-end projects — from reconciliation engines to personal finance trackers — using frameworks like Flask and Streamlit, hosted on AWS.

Usman is the visionary behind the Man_Analytics brand, which aims to empower African SMEs with intuitive, low-cost data and automation tools. His core passion lies in solving local financial problems with smart, transparent technology that builds trust and drives decision-making.

🔗 [LinkedIn](https://www.linkedin.com/in/abdulrahman-idris-usman-98588b2b8/)  
🔗 [GitHub](https://github.com/Usmile85)  
📄 [Resume](https://usman2-bucket.s3-website.eu-north-1.amazonaws.com/)
    """)

# Lottie animation
st_lottie(lottie_animation, height=300, key="analytics")

# Gold price chart section
st.markdown("## 🪙 Gold Price Trend (2005–2025)")
st.write("""
Gold has historically functioned as a financial anchor — an asset that investors turn to in times of uncertainty, inflation, or currency instability. Between 2005 and 2025, the price of gold rose from roughly $445 per ounce to over $3,300 per ounce, driven by key global events.

The 2008 financial crisis marked the first major surge, followed by another rally during the COVID-19 pandemic in 2020. More recently, concerns about inflation, fiat currency debasement, and geopolitical tensions have fueled gold’s continued appreciation.

This trend reinforces the idea that gold is not just a commodity — it's a signal of market sentiment. For data scientists and fintech professionals, tracking assets like gold provides deeper context when modeling risk, predicting inflation, or assessing macroeconomic impacts.
""")

st.image("assets/gold_price_trend_2005_2025.png", caption="Gold Price Per Ounce (2005–2025)", use_container_width=True)

# Blog section
st.markdown("## 📝 Latest Blog Post")
blog_folder = Path("blog_posts")
posts = sorted(blog_folder.glob("*.md"), reverse=True)
if posts:
    latest_post = posts[0]
    st.markdown(open(latest_post, "r", encoding="utf-8").read(), unsafe_allow_html=True)

# Footer
with st.spinner("Loading dashboard..."):
    time.sleep(2)
st.success("Portfolio & blog ready to roll! 🎯")