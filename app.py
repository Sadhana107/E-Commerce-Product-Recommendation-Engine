import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="ShopSmart AI",
    page_icon="🛒",
    layout="wide"
)

# ==========================================
# LOAD DATA
# ==========================================

products = pd.read_csv("data/products.csv")

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.hero {
    padding: 30px;
    border-radius: 20px;
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e293b,
        #2563eb
    );
    margin-bottom: 20px;
}

.hero-title {
    font-size: 48px;
    font-weight: 800;
    color: white;
}

.hero-subtitle {
    font-size: 18px;
    color: #e2e8f0;
}

.product-card {
    background:#1A1D29;
    padding:20px;
    border-radius:15px;
    margin-bottom:15px;
    border:1px solid #2d3748;
}

.insight-card {
    background:#1A1D29;
    padding:20px;
    border-radius:15px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("🛒 ShopSmart AI")

category_filter = st.sidebar.selectbox(
    "Category",
    ["All"] + list(products["category"].unique())
)

search_term = st.sidebar.text_input(
    "Search Product"
)

selected_user = st.sidebar.selectbox(
    "Select User",
    ["U001", "U002", "U003", "U004", "U005"]
)

# ==========================================
# FILTERING
# ==========================================

filtered_products = products.copy()

if category_filter != "All":
    filtered_products = filtered_products[
        filtered_products["category"] == category_filter
    ]

if search_term:
    filtered_products = filtered_products[
        filtered_products["name"].str.contains(
            search_term,
            case=False
        )
    ]

# ==========================================
# HERO SECTION
# ==========================================

st.markdown(f"""
<div class="hero">

<div class="hero-title">
🛒 ShopSmart AI
</div>

<div class="hero-subtitle">
Intelligent Product Recommendation Platform
<br><br>
Powered by Recommendation Algorithms,
Ranking Systems, Similarity Matching,
and Personalized Product Discovery
</div>

</div>
""", unsafe_allow_html=True)

# ==========================================
# KPI SECTION
# ==========================================

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric(
        "Products",
        len(filtered_products)
    )

with col2:
    st.metric(
        "Categories",
        filtered_products["category"].nunique()
    )

with col3:
    st.metric(
        "Average Rating",
        round(
            filtered_products["rating"].mean(),
            2
        )
    )

with col4:
    st.metric(
        "Highest Rating",
        filtered_products["rating"].max()
    )

st.divider()

# ==========================================
# ANALYTICS
# ==========================================

st.header("📊 Analytics Dashboard")

c1,c2 = st.columns(2)

with c1:

    fig1 = px.pie(
        filtered_products,
        names="category",
        hole=0.55,
        title="Category Distribution"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with c2:

    fig2 = px.histogram(
        filtered_products,
        x="rating",
        title="Rating Distribution"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# ==========================================
# PRICE ANALYTICS
# ==========================================

st.header("💰 Price Analytics")

price_chart = px.bar(
    filtered_products,
    x="name",
    y="price",
    color="category",
    title="Product Price Comparison"
)

st.plotly_chart(
    price_chart,
    use_container_width=True
)

# ==========================================
# RECOMMENDATION DEMO
# ==========================================

st.header("🎯 Recommendation Engine")

recommended = products.sort_values(
    "rating",
    ascending=False
).head(6)

st.success(
    f"Recommended For {selected_user}"
)

cols = st.columns(3)

for idx, (_, row) in enumerate(recommended.iterrows()):

    with cols[idx % 3]:

        st.markdown(
            f"""
            <div class='product-card'>
            <h4>{row['name']}</h4>
            <p>Category: {row['category']}</p>
            <p>Price: ₹{row['price']}</p>
            <p>⭐ {row['rating']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# ==========================================
# SIMILAR PRODUCTS
# ==========================================

st.header("🛍 Customers Also Viewed")

selected_product = st.selectbox(
    "Choose Product",
    products["name"]
)

selected_category = products[
    products["name"] == selected_product
]["category"].iloc[0]

similar = products[
    products["category"] ==
    selected_category
]

cols = st.columns(3)

for idx, (_, row) in enumerate(similar.iterrows()):

    with cols[idx % 3]:

        st.markdown(
            f"""
            <div class='product-card'>
            <h4>{row['name']}</h4>
            <p>{row['category']}</p>
            <p>₹{row['price']}</p>
            <p>⭐ {row['rating']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# ==========================================
# LEADERBOARD
# ==========================================

st.header("🏆 Top Rated Products Leaderboard")

leaderboard = products.sort_values(
    "rating",
    ascending=False
).head(10)

medals = [
    "🥇","🥈","🥉",
    "4️⃣","5️⃣",
    "6️⃣","7️⃣",
    "8️⃣","9️⃣","🔟"
]

for i, (_, row) in enumerate(
    leaderboard.iterrows()
):
    st.write(
        f"{medals[i]} "
        f"{row['name']} "
        f"({row['rating']})"
    )

# ==========================================
# EXECUTIVE INSIGHTS
# ==========================================

st.header("📈 Executive Insights")

top_product = products.loc[
    products["rating"].idxmax()
]

expensive_product = products.loc[
    products["price"].idxmax()
]

top_category = products[
    "category"
].value_counts().idxmax()

col1,col2 = st.columns(2)

with col1:

    st.info(
        f"""
Highest Rated Product

🏆 {top_product['name']}

⭐ Rating: {top_product['rating']}
"""
    )

with col2:

    st.info(
        f"""
Most Expensive Product

💰 {expensive_product['name']}

₹ {expensive_product['price']}
"""
    )

st.success(
    f"📦 Most Popular Category: {top_category}"
)

# ==========================================
# FULL CATALOG
# ==========================================

st.header("📦 Product Catalog")

st.dataframe(
    filtered_products,
    use_container_width=True,
    height=500
)