import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="ShopMind AI",
    page_icon="🛒",
    layout="wide"
)

products = pd.read_csv("data/products.csv")

st.markdown("""
# 🛒 ShopMind AI

### Intelligent E-Commerce Recommendation Platform

AI-Powered Product Discovery & Recommendation Engine
""")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Products",
        len(products)
    )

with col2:
    st.metric(
        "Categories",
        products["category"].nunique()
    )

with col3:
    st.metric(
        "Avg Rating",
        round(products["rating"].mean(), 2)
    )

st.divider()

st.subheader("📦 Product Catalog")

st.dataframe(
    products,
    use_container_width=True
)

st.divider()

st.subheader("📊 Category Distribution")

fig = px.pie(
    products,
    names="category",
    title="Products by Category"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.subheader("⭐ Top Rated Products")

top_products = products.sort_values(
    "rating",
    ascending=False
)

st.dataframe(
    top_products,
    use_container_width=True
)