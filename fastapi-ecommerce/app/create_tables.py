from app.database import engine
from app.models.db_product import ProductDB
from app.models.db_user import UserDB

ProductDB.metadata.create_all(bind=engine)
UserDB.metadata.create_all(bind=engine)

print("✅ Tables created")
