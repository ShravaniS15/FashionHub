import pandas as pd
from database import SessionLocal
from models import Product

db = SessionLocal()

# Read CSV
df = pd.read_csv(
    "fashionhubproducts.csv",
    header=None,
    names=[
        "id",
        "name",
        "description",
        "category",
        "brand",
        "price",
        "stock",
        "rating",
        "image",
    ],
)

# Prevent duplicate imports
if db.query(Product).count() > 0:
    print("⚠ Products already exist.")
    db.close()
    exit()

for _, row in df.iterrows():

    product = Product(
        name=row["name"],
        description=row["description"],
        category=row["category"],
        brand=row["brand"],
        price=float(row["price"]),
        stock=int(row["stock"]),
        rating=float(row["rating"]),
        image=str(row["image"]).replace("\\", "/"),
    )

    db.add(product)

db.commit()

print(f"✅ Imported {len(df)} products successfully!")

db.close()