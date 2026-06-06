class User:

    def __init__(
        self,
        user_id,
        name
    ):
        self.user_id = user_id
        self.name = name

        self.purchase_history = []
        self.search_history = []
        self.cart_items = []

    def add_purchase(self, product_id):
        self.purchase_history.append(product_id)

    def add_search(self, keyword):
        self.search_history.append(keyword)

    def add_cart(self, product_id):
        self.cart_items.append(product_id)