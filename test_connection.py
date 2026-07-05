from database import engine

try:
    connection = engine.connect()
    print("✅ Connected to PostgreSQL Successfully!")
    connection.close()
except Exception as e:
    print("❌ Error:", e)