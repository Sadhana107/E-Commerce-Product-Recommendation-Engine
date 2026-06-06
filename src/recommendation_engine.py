import pandas as pd
import heapq


class RecommendationEngine:

    def __init__(self):
        self.products = {}
        self.users = {}

    # ============================
    # LOAD PRODUCTS
    # ============================

    def load_products(self, filepath):

        df = pd.read_csv(filepath)

        for _, row in df.iterrows():

            self.products[row["product_id"]] = {
                "name": row["name"],
                "category": row["category"],
                "price": row["price"],
                "rating": row["rating"]
            }

    # ============================
    # LOAD USERS
    # ============================

    def load_users(self, filepath):

        df = pd.read_csv(filepath)

        for _, row in df.iterrows():

            self.users[row["user_id"]] = {
                "name": row["name"],
                "purchase_history": [],
                "search_history": [],
                "cart_items": []
            }

    # ============================
    # USER ACTIVITY
    # ============================

    def add_purchase(self, user_id, product_id):
        self.users[user_id]["purchase_history"].append(product_id)

    def add_search(self, user_id, keyword):
        self.users[user_id]["search_history"].append(keyword)

    def add_cart(self, user_id, product_id):
        self.users[user_id]["cart_items"].append(product_id)

    # ============================
    # DISPLAY USER
    # ============================

    def display_user(self, user_id):

        print("\nUSER DETAILS\n")
        print(self.users[user_id])

    # ============================
    # SIMILARITY SCORE
    # ============================

    def calculate_similarity_score(
        self,
        user_id,
        product_id
    ):

        score = 0

        product = self.products[product_id]

        user = self.users[user_id]

        # Purchase History

        for purchased_product in user["purchase_history"]:

            purchased_category = self.products[
                purchased_product
            ]["category"]

            if purchased_category == product["category"]:
                score += 5

        # Cart History

        for cart_product in user["cart_items"]:

            cart_category = self.products[
                cart_product
            ]["category"]

            if cart_category == product["category"]:
                score += 3

        # Product Rating

        score += product["rating"]

        return score

    # ============================
    # HEAP BASED RECOMMENDATIONS
    # ============================

    def recommend_products(
        self,
        user_id,
        top_n=5
    ):

        heap = []

        purchased_products = set(
            self.users[user_id][
                "purchase_history"
            ]
        )

        for product_id in self.products:

            if product_id in purchased_products:
                continue

            score = self.calculate_similarity_score(
                user_id,
                product_id
            )

            heapq.heappush(
                heap,
                (-score, product_id)
            )

        recommendations = []

        while heap and len(recommendations) < top_n:

            score, product_id = heapq.heappop(heap)

            recommendations.append(
                (
                    product_id,
                    -score
                )
            )

        return recommendations

    # ============================
    # DISPLAY RECOMMENDATIONS
    # ============================

    def display_recommendations(
        self,
        user_id
    ):

        recommendations = self.recommend_products(
            user_id
        )

        print("\nTOP RECOMMENDATIONS\n")

        for product_id, score in recommendations:

            product = self.products[
                product_id
            ]

            print(
                f"{product['name']} | "
                f"{product['category']} | "
                f"Rating: {product['rating']} | "
                f"Score: {round(score,2)}"
            )

    # ============================
    # SIMILAR PRODUCTS
    # ============================

    def get_similar_products(
        self,
        product_id,
        top_n=5
    ):

        category = self.products[
            product_id
        ]["category"]

        similar_products = []

        for pid, product in self.products.items():

            if pid == product_id:
                continue

            if product["category"] == category:

                similar_products.append(
                    (
                        pid,
                        product["rating"]
                    )
                )

        similar_products.sort(
            key=lambda x: x[1],
            reverse=True
        )

        return similar_products[:top_n]

    # ============================
    # CATEGORY RECOMMENDATIONS
    # ============================

    def recommend_by_category(
        self,
        category,
        top_n=5
    ):

        products = []

        for pid, product in self.products.items():

            if product["category"] == category:

                products.append(
                    (
                        pid,
                        product["rating"]
                    )
                )

        products.sort(
            key=lambda x: x[1],
            reverse=True
        )

        return products[:top_n]