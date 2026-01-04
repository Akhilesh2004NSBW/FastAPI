from fastapi import FastAPI
from app.service.products import (
    get_all_products,
    search_products_by_name,
    add_product
)

app = FastAPI()

# Root API
@app.get("/")
def root():
    return {"message": "APX!"}


# 🔍 SEARCH MUST COME FIRST
@app.get("/products/search")
def search_product(name: str):
    results = search_products_by_name(name)

    if not results:
        return {"message": "No product found with this name"}

    return results


# GET all products
@app.get("/products")
def get_products():
    return get_all_products()


# GET product by ID
@app.get("/products/{product_id}")
def get_product(product_id: int):
    products = get_all_products()

    for product in products:
        if product["id"] == product_id:
            return product

    return {"error": "Product not found"}


# ➕ POST API – Add new product
@app.post("/products")
def create_product(product: dict):
    return add_product(product)
