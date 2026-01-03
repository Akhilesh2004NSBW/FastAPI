---

# FastAPI E-Commerce Backend (Learning Project)

This project is a **beginner-to-intermediate FastAPI backend** built step by step to understand how real APIs work.
It focuses on **core concepts**, not shortcuts.

---

## 📌 What This Project Does

* Runs a FastAPI backend server
* Serves APIs using HTTP GET requests
* Reads product data from a JSON file
* Returns data as JSON responses
* Demonstrates real backend routing and structure

---

## 📂 Project Structure

```
fastapi-ecommerce/
│
├── app/
│   └── main.py          # Main FastAPI application
│
├── data/
│   └── products.json    # Product data source
│
└── README.md
```

---

## 🚀 How to Run the Project

### 1️⃣ Install dependencies

```bash
python -m pip install fastapi uvicorn
```

---

### 2️⃣ Start the server

Run this command **from the `fastapi-ecommerce` folder**:

```bash
python -m uvicorn app.main:app --reload
```

---

### 3️⃣ Open in browser

* Home:
  [http://127.0.0.1:8000](http://127.0.0.1:8000)

* Products API:
  [http://127.0.0.1:8000/products](http://127.0.0.1:8000/products)

* Swagger UI (API Docs):
  [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧠 Concepts Covered So Far

### ✅ FastAPI Basics

* Creating a FastAPI app using `FastAPI()`
* Running server with `uvicorn`
* Understanding module paths (`app.main:app`)
* Fixing import and path errors

---

### ✅ API Development

* Creating GET APIs
* Using decorators like `@app.get()`
* Returning JSON responses
* Handling multiple routes

---

### ✅ File-Based Data Handling

* Reading data from a JSON file
* Using Python’s `json` module
* Sending file data as API response

---

### ✅ Dynamic Routing

* Path parameters (`/products/{id}`)
* Fetching a single product by ID
* Handling “not found” cases

---

## 📌 APIs Implemented

### 🔹 Home API

```
GET /
```

Response:

```json
{
  "message": "Welome to FastAPI!"
}
```

---

### 🔹 Get All Products

```
GET /products
```

Response:

```json
[
  {
    "id": 1,
    "name": "Laptop",
    "price": 55000
  }
]
```

---

### 🔹 Get Product by ID

```
GET /products/{id}
```

Example:

```
/products/1
```

Response:

```json
{
  "id": 1,
  "name": "Laptop",
  "price": 55000
}
```

If product not found:

```json
{
  "error": "Product not found"
}
```

---

## 🧩 What This Project Teaches

* How backend APIs actually work
* How URLs map to Python functions
* How data flows from file → server → client
* How FastAPI simplifies API development
* How real backend project structure looks

---

## 📈 Current Progress

* ✅ ~35% of core FastAPI covered
* ✅ Strong foundation built
* 🚀 Ready for POST, validation, and databases

---

## 🔜 Next Planned Features

* POST `/products` (add new product)
* Pydantic models for validation
* Proper HTTP status codes
* Error handling using `HTTPException`

---

## ✍️ Author Note

This project is built **for learning and understanding**, not copy-paste.
Each step focuses on **clarity, structure, and backend fundamentals**.

---

If you want, next I can:

* Improve this README to **GitHub-quality**
* Add **POST API notes**
* Convert this into a **resume-ready project description**

Just say **next** 👍
Perfect 👍
Below is a **clean, simple, professional README-style notes file** based **only on what you have done till now**.
You can directly paste this into `README.md`.

---

# FastAPI E-Commerce Backend (Learning Project)

This project is a **beginner-to-intermediate FastAPI backend** built step by step to understand how real APIs work.
It focuses on **core concepts**, not shortcuts.

---

## 📌 What This Project Does

* Runs a FastAPI backend server
* Serves APIs using HTTP GET requests
* Reads product data from a JSON file
* Returns data as JSON responses
* Demonstrates real backend routing and structure

---

## 📂 Project Structure

```
fastapi-ecommerce/
│
├── app/
│   └── main.py          # Main FastAPI application
│
├── data/
│   └── products.json    # Product data source
│
└── README.md
```

---

## 🚀 How to Run the Project

### 1️⃣ Install dependencies

```bash
python -m pip install fastapi uvicorn
```

---

### 2️⃣ Start the server

Run this command **from the `fastapi-ecommerce` folder**:

```bash
python -m uvicorn app.main:app --reload
```

---

### 3️⃣ Open in browser

* Home:
  [http://127.0.0.1:8000](http://127.0.0.1:8000)

* Products API:
  [http://127.0.0.1:8000/products](http://127.0.0.1:8000/products)

* Swagger UI (API Docs):
  [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧠 Concepts Covered So Far

### ✅ FastAPI Basics

* Creating a FastAPI app using `FastAPI()`
* Running server with `uvicorn`
* Understanding module paths (`app.main:app`)
* Fixing import and path errors

---

### ✅ API Development

* Creating GET APIs
* Using decorators like `@app.get()`
* Returning JSON responses
* Handling multiple routes

---

### ✅ File-Based Data Handling

* Reading data from a JSON file
* Using Python’s `json` module
* Sending file data as API response

---

### ✅ Dynamic Routing

* Path parameters (`/products/{id}`)
* Fetching a single product by ID
* Handling “not found” cases

---

## 📌 APIs Implemented

### 🔹 Home API

```
GET /
```

Response:

```json
{
  "message": "Meri Chetna Kesi Haiii!"
}
```

---

### 🔹 Get All Products

```
GET /products
```

Response:

```json
[
  {
    "id": 1,
    "name": "Laptop",
    "price": 55000
  }
]
```

---

### 🔹 Get Product by ID

```
GET /products/{id}
```

Example:

```
/products/1
```

Response:

```json
{
  "id": 1,
  "name": "Laptop",
  "price": 55000
}
```

If product not found:

```json
{
  "error": "Product not found"
}
```

---

## 🧩 What This Project Teaches

* How backend APIs actually work
* How URLs map to Python functions
* How data flows from file → server → client
* How FastAPI simplifies API development
* How real backend project structure looks

---

## 📈 Current Progress

* ✅ ~35% of core FastAPI covered
* ✅ Strong foundation built
* 🚀 Ready for POST, validation, and databases

---

## 🔜 Next Planned Features

* POST `/products` (add new product)
* Pydantic models for validation
* Proper HTTP status codes
* Error handling using `HTTPException`

---

## ✍️ Author Note

This project is built **for learning and understanding**, not copy-paste.
Each step focuses on **clarity, structure, and backend fundamentals**.

---
