import streamlit as st
from PIL import Image
import time
import requests
from pathlib import Path
from streamlit_lottie import st_lottie
import os

# Load Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Setup page
st.set_page_config(page_title="Man_Analytics Portfolio Blog", layout="wide")
lottie_animation = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json")

# Header layout
col1, col2 = st.columns([1, 3])
with col1:
    profile_path = "assets/usman_profile.jpg"
    if os.path.exists(profile_path):
        profile_image = Image.open(profile_path)
        st.image(
            profile_image,
            caption="Usman Idris Abdulrahman\n\nSenior Analyst and Team Lead,\nDomestic Settlement and Reconciliation",
            use_container_width=True
        )
    else:
        st.warning("⚠️ Profile image not found.")

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
Gold has historically functioned as a financial anchor — an asset that investors turn to in times of uncertainty...

This trend reinforces the idea that gold is not just a commodity — it's a signal of market sentiment.
""")

# Hybrid logic: Try local file, fallback to GitHub URL
from PIL import UnidentifiedImageError

local_image_path = "assets/gold_price_trend_clean.png"
fallback_image_url = "https://raw.githubusercontent.com/Usmile85/Porfolio-Blog/master/assets/gold_price_trend_clean.png"

try:
    # Try loading locally first
    if os.path.exists(local_image_path):
        local_image = Image.open(local_image_path)
        st.image(local_image, caption="Gold Price Per Ounce (2005–2025)", use_container_width=True)
    else:
        raise FileNotFoundError
except (FileNotFoundError, UnidentifiedImageError):
    # Fallback to online GitHub image
    try:
        st.image(fallback_image_url, caption="Gold Price Per Ounce (2005–2025)", use_container_width=True)
    except Exception as e:
        st.warning("⚠️ Could not load gold chart image from GitHub.")
        st.error(f"Error: {e}")
# Blog section
st.markdown("## 📝 Latest Blog Post")
blog_folder = Path("blog_posts")
posts = sorted(blog_folder.glob("*.md"), reverse=True)
if posts:
    latest_post = posts[0]
    st.markdown(open(latest_post, "r", encoding="utf-8").read(), unsafe_allow_html=True)

# Footer loading effect
with st.spinner("Loading dashboard..."):
    time.sleep(2)
st.success("Portfolio & blog ready to roll! 🎯")

