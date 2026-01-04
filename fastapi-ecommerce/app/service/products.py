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
    result = []

    for product in products:
        if product.get("name") == name:   # case-sensitive
            result.append(product)

    return result


def add_product(product: Dict):
    products = load_products()
    products.append(product)
    save_products(products)

    return {
        "message": "Product added successfully",
        "product": product
    }
