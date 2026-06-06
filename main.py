from src.recommendation_engine import RecommendationEngine
from src.report_generator import ReportGenerator

engine = RecommendationEngine()

engine.load_products(
    "data/products.csv"
)

engine.load_users(
    "data/users.csv"
)

# USER ACTIVITY

engine.add_purchase(
    "U001",
    "P111"
)

engine.add_purchase(
    "U001",
    "P112"
)

engine.add_cart(
    "U001",
    "P113"
)

# ==========================
# RECOMMENDATIONS
# ==========================

engine.display_recommendations(
    "U001"
)

recommendations = (
    engine.recommend_products(
        "U001"
    )
)

# SAVE REPORT

ReportGenerator.save_recommendations(
    recommendations,
    engine.products
)

print(
    "\nProject executed successfully."
)