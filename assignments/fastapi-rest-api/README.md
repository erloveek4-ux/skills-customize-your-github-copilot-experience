# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build modern, production-ready REST APIs using the FastAPI framework. You'll practice creating HTTP endpoints, handling request/response data, working with path and query parameters, and implementing data validation using Pydantic models.

## 📝 Tasks

### 🛠️ Create a Basic API with FastAPI

#### Description
Set up a FastAPI application and create basic HTTP endpoints (GET and POST) for managing a simple resource.

#### Requirements
Completed program should:

- Import and initialize a FastAPI application
- Create a GET endpoint that returns a list of items in JSON format
- Create a GET endpoint with a path parameter to retrieve a single item by ID
- Create a POST endpoint to add a new item
- Run the application and verify endpoints work using the interactive API documentation (Swagger UI at `/docs`)

#### Example
```python
from fastapi import FastAPI

app = FastAPI()

items = [
    {"id": 1, "name": "Item 1", "price": 10.0},
    {"id": 2, "name": "Item 2", "price": 20.0}
]

@app.get("/items")
def get_items():
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return next((item for item in items if item["id"] == item_id), None)

@app.post("/items")
def create_item(name: str, price: float):
    new_item = {"id": len(items) + 1, "name": name, "price": price}
    items.append(new_item)
    return new_item
```

### 🛠️ Implement Pydantic Models for Data Validation

#### Description
Create Pydantic models to define the structure of request and response data with automatic validation.

#### Requirements
Completed program should:

- Define a Pydantic model for the item data structure (with fields: id, name, price, description)
- Use the model in POST endpoint to accept and validate request body data
- Ensure that the API returns proper error responses for invalid data
- Add type hints to all function parameters and return values

#### Example
```python
from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str] = None

@app.post("/items")
def create_item(item: Item):
    items.append(item.dict())
    return item
```

### 🛠️ Add Query Parameters and Update/Delete Operations

#### Description
Extend the API with advanced features including query parameters, update (PUT) operations, and delete (DELETE) operations.

#### Requirements
Completed program should:

- Add a GET endpoint that accepts optional query parameters (e.g., `min_price`, `max_price`) to filter items
- Implement a PUT endpoint to update an existing item by ID
- Implement a DELETE endpoint to remove an item by ID
- Return appropriate HTTP status codes (200 for success, 404 for not found, 422 for invalid data)
- Test all endpoints using the Swagger UI or a tool like Postman

#### Example
```python
from fastapi import HTTPException, status

@app.get("/items")
def get_items(min_price: float = 0, max_price: float = 1000):
    return [item for item in items if min_price <= item["price"] <= max_price]

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    existing = next((i for i in items if i["id"] == item_id), None)
    if not existing:
        raise HTTPException(status_code=404, detail="Item not found")
    existing.update(item.dict())
    return existing

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    global items
    items = [i for i in items if i["id"] != item_id]
    return {"message": "Item deleted"}
```
