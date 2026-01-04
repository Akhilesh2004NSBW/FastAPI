import json
from pathlib import Path
from typing import List, Dict

DATA_FILE = Path(__file__).parent.parent / "data" / "products.json"


def load_products() -> List[Dict]:
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_products(products: List[Dict]):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(products, file, indent=2)


def get_all_products() -> List[Dict]:
    return load_products()


def search_products_by_name(name: str) -> List[Dict]:
    products = load_products()
    return [p for p in products if p.get("name") == name]


def add_product(product: Dict):
    products = load_products()

    # duplicate ID check
    for p in products:
        if p["id"] == product["id"]:
            return {"error": "Product with this ID already exists"}

    products.append(product)
    save_products(products)

    return {
        "message": "Product added successfully",
        "product": product
    }


def update_product(product_id: int, updated_data: Dict):
    products = load_products()

    for index, product in enumerate(products):
        if product["id"] == product_id:
            products[index]["name"] = updated_data["name"]
            products[index]["price"] = updated_data["price"]
            save_products(products)

            return products[index]

    return None

def delete_product(product_id: int):
    products = load_products()

    for index, product in enumerate(products):
        if product["id"] == product_id:
            deleted_product = products.pop(index)
            save_products(products)
            return deleted_product

    return None

def patch_product(product_id: int, updated_data: Dict):
    products = load_products()

    for index, product in enumerate(products):
        if product["id"] == product_id:

            if updated_data.get("name") is not None:
                products[index]["name"] = updated_data["name"]

            if updated_data.get("price") is not None:
                products[index]["price"] = updated_data["price"]

            save_products(products)
            return products[index]

    return None


def filter_products_by_price(min_price: float, max_price: float):
    products = load_products()
    return [
        p for p in products
        if min_price <= p.get("price", 0) <= max_price
    ]


def filter_products_by_name_contains(keyword: str):
    products = load_products()
    return [
        p for p in products
        if keyword.lower() in p.get("name", "").lower()
    ]


def filter_products(keyword: str, min_price: float, max_price: float):
    products = load_products()
    return [
        p for p in products
        if keyword.lower() in p.get("name", "").lower()
        and min_price <= p.get("price", 0) <= max_price
    ]



