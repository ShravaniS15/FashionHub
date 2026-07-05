from database import SessionLocal
from models import Product

db = SessionLocal()

products = [

# -------------------- MEN --------------------
Product(
    name="Nike Hoodie",
    description="Premium cotton hoodie",
    category="Men",
    brand="Nike",
    price=1999,
    stock=25,
    rating=4.8,
    image="images/men/nike_hoodie.jpg"
),

Product(
    name="Levi's Jeans",
    description="Slim fit blue jeans",
    category="Men",
    brand="Levi's",
    price=2499,
    stock=20,
    rating=4.7,
    image="images/men/levis_jeans.jpg"
),

Product(
    name="Puma T-Shirt",
    description="Comfort fit t-shirt",
    category="Men",
    brand="Puma",
    price=999,
    stock=30,
    rating=4.6,
    image="images/men/puma_tshirt.jpg"
),

# -------------------- WOMEN --------------------
Product(
    name="Zara Dress",
    description="Elegant floral dress",
    category="Women",
    brand="Zara",
    price=2499,
    stock=15,
    rating=4.9,
    image="images/women/zara_dress.jpg"
),

Product(
    name="H&M Top",
    description="Casual summer top",
    category="Women",
    brand="H&M",
    price=899,
    stock=40,
    rating=4.5,
    image="images/women/hm_top.jpg"
),

Product(
    name="Forever21 Skirt",
    description="Stylish mini skirt",
    category="Women",
    brand="Forever21",
    price=1299,
    stock=18,
    rating=4.6,
    image="images/women/skirt.jpg"
),

# -------------------- KIDS --------------------
Product(
    name="Kids Cartoon T-Shirt",
    description="Soft cotton t-shirt",
    category="Kids",
    brand="MiniClub",
    price=699,
    stock=40,
    rating=4.7,
    image="images/kids/cartoon_tshirt.jpg"
),

Product(
    name="Kids Denim Shorts",
    description="Comfortable denim shorts",
    category="Kids",
    brand="Hopscotch",
    price=899,
    stock=35,
    rating=4.6,
    image="images/kids/shorts.jpg"
),

# -------------------- FOOTWEAR --------------------
Product(
    name="Adidas Sneakers",
    description="Running shoes",
    category="Footwear",
    brand="Adidas",
    price=3499,
    stock=18,
    rating=4.8,
    image="images/footwear/adidas.jpg"
),

Product(
    name="Nike Air Max",
    description="Premium sneakers",
    category="Footwear",
    brand="Nike",
    price=5999,
    stock=12,
    rating=4.9,
    image="images/footwear/airmax.jpg"
),

Product(
    name="Puma Sports Shoes",
    description="Training shoes",
    category="Footwear",
    brand="Puma",
    price=2999,
    stock=20,
    rating=4.6,
    image="images/footwear/puma.jpg"
),

# -------------------- ACCESSORIES --------------------
Product(
    name="Leather Wallet",
    description="Premium leather wallet",
    category="Accessories",
    brand="WildHorn",
    price=999,
    stock=25,
    rating=4.7,
    image="images/accessories/wallet.jpg"
),

Product(
    name="Smart Watch",
    description="Bluetooth Smart Watch",
    category="Accessories",
    brand="Noise",
    price=3499,
    stock=15,
    rating=4.8,
    image="images/accessories/watch.jpg"
),

Product(
    name="Sunglasses",
    description="UV Protected Sunglasses",
    category="Accessories",
    brand="RayBan",
    price=1999,
    stock=20,
    rating=4.7,
    image="images/accessories/sunglasses.jpg"
),

# -------------------- SUMMER --------------------
Product(
    name="Summer Cotton Shirt",
    description="Breathable cotton shirt",
    category="Summer",
    brand="Allen Solly",
    price=1499,
    stock=22,
    rating=4.6,
    image="images/summer/shirt.jpg"
),

Product(
    name="Beach Shorts",
    description="Quick dry shorts",
    category="Summer",
    brand="Roadster",
    price=999,
    stock=30,
    rating=4.5,
    image="images/summer/shorts.jpg"
),

# -------------------- WINTER --------------------
Product(
    name="Winter Jacket",
    description="Warm padded jacket",
    category="Winter",
    brand="Woodland",
    price=3999,
    stock=14,
    rating=4.9,
    image="images/winter/jacket.jpg"
),

Product(
    name="Wool Sweater",
    description="Soft wool sweater",
    category="Winter",
    brand="Monte Carlo",
    price=2499,
    stock=18,
    rating=4.8,
    image="images/winter/sweater.jpg"
),

# -------------------- SALE --------------------
Product(
    name="Casual Shirt",
    description="Discounted shirt",
    category="Sale",
    brand="Peter England",
    price=799,
    stock=40,
    rating=4.4,
    image="images/sale/shirt.jpg"
),

Product(
    name="Running Shoes",
    description="Limited time offer",
    category="Sale",
    brand="Reebok",
    price=1999,
    stock=20,
    rating=4.5,
    image="images/sale/shoes.jpg"
),

# -------------------- NEW ARRIVALS --------------------
Product(
    name="Oversized Hoodie",
    description="Latest fashion hoodie",
    category="New Arrivals",
    brand="H&M",
    price=2299,
    stock=20,
    rating=4.9,
    image="images/new/hoodie.jpg"
),

Product(
    name="Cargo Pants",
    description="Trending cargo pants",
    category="New Arrivals",
    brand="Zara",
    price=2599,
    stock=15,
    rating=4.8,
    image="images/new/cargo.jpg"
)

]

db.add_all(products)
db.commit()

print("✅ Products Inserted Successfully!")

db.close()