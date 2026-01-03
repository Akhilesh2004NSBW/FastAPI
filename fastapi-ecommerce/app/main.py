from fastapi import FastAPI
import json

app = FastAPI()

# Home API
@app.get("/")
def root():
    return {"message": "Meri Chetna Kesi Haiii!"}

# Products API
@app.get("/products")
def get_products():
    with open("data/products.json", "r") as file:
        products = json.load(file)
    return products

# Single Product API

@app.get("/products/{product_id}")
def get_product(product_id: int):
    with open("data/products.json", "r") as file:
        products = json.load(file)

    for product in products:
        if product["id"] == product_id:
            return product

    return {"error": "Product not found"}
