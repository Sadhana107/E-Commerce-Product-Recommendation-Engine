import csv


class ReportGenerator:

    @staticmethod
    def save_recommendations(
        recommendations,
        products,
        filename="outputs/recommendations.csv"
    ):

        with open(
            filename,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow(
                [
                    "Product ID",
                    "Product Name",
                    "Category",
                    "Rating",
                    "Score"
                ]
            )

            for product_id, score in recommendations:

                product = products[product_id]

                writer.writerow(
                    [
                        product_id,
                        product["name"],
                        product["category"],
                        product["rating"],
                        round(score, 2)
                    ]
                )

        print(
            f"\nReport saved successfully -> {filename}"
        )