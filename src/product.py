class Product:

    def __init__(
        self,
        product_id,
        name,
        category,
        price,
        rating
    ):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.rating = rating

    def display(self):
        return (
            f"{self.product_id} | "
            f"{self.name} | "
            f"{self.category} | "
            f"₹{self.price} | "
            f"{self.rating}"
        )