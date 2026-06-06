import pandas as pd

products = pd.read_csv(
    "data/products.csv"
)

users = pd.read_csv(
    "data/users.csv"
)

print("\nPRODUCT DATASET\n")
print(products.head())

print("\nUSER DATASET\n")
print(users.head())