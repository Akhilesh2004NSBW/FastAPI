from fastapi import FastAPI, HTTPException, status
from app.models.product import Product, ProductUpdate
from app.service.products import patch_product
from app.service.products import filter_products_by_price
from app.service.products import filter_products_by_name_contains
from app.service.products import filter_products
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.jwt import create_access_token
from app.service.auth import create_user, authenticate_user

from app.service.products import (
    get_all_products,
    search_products_by_name,
    add_product,
    update_product,
    delete_product
)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "APX and His - !"}


# 🔍 SEARCH MUST COME FIRST
@app.get("/products/search")
def search_product(name: str):
    results = search_products_by_name(name)

    if not results:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No product found with this name"
        )

    return results


@app.get("/products")
def get_products():
    return get_all_products()


@app.get("/products/{product_id}")
def get_product(product_id: int):
    products = get_all_products()

    for product in products:
        if product["id"] == product_id:
            return product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )


@app.post("/products", status_code=status.HTTP_201_CREATED)
def create_product(product: Product):
    result = add_product(product.dict())

    if "error" in result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=result["error"]
        )

    return result


# 🔄 PUT API – Update product
@app.put("/products/{product_id}")
def update_product_api(product_id: int, product: ProductUpdate):
    updated = update_product(product_id, product.dict())

    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

    return {
        "message": "Product updated successfully",
        "product": updated
    }



# 🗑 DELETE API – Remove product
@app.delete("/products/{product_id}")
def delete_product_api(product_id: int):
    deleted = delete_product(product_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

    return {
        "message": "Product deleted successfully",
        "product": deleted
    }


@app.patch("/products/{product_id}")
def patch_product_api(product_id: int, product: ProductUpdate):
    updated = patch_product(product_id, product.dict())

    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

    return {
        "message": "Product updated successfully",
        "product": updated
    }
    
    

@app.get("/products/filter/price")
def filter_by_price(min_price: float, max_price: float):
    results = filter_products_by_price(min_price, max_price)

    if not results:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No products found in this price range"
        )

    return results


@app.get("/products/filter/name")
def filter_by_name(keyword: str):
    results = filter_products_by_name_contains(keyword)

    if not results:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No products found with this keyword"
        )

    return results


@app.get("/products/filter")
def combined_filter(keyword: str, min_price: float, max_price: float):
    results = filter_products(keyword, min_price, max_price)

    if not results:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No products match the given filters"
        )

    return results

@app.post("/signup")
def signup(username: str, password: str, db: Session = Depends(get_db)):
    user = create_user(db, username, password)
    return {"message": "User created", "user": user.username}

@app.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = authenticate_user(db, username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}



