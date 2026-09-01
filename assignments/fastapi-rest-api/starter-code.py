"""
FastAPI REST API Starter Code
Build a REST API for managing items with full CRUD operations.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Items API", version="1.0.0")

# TODO: Define your Pydantic model here
# Example structure:
# class Item(BaseModel):
#     id: int
#     name: str
#     price: float
#     description: Optional[str] = None


# TODO: Initialize an empty list to store items
# items = []


# TODO: Implement GET /items endpoint
# Should return all items or filtered items based on query parameters
@app.get("/items")
def get_items():
    pass


# TODO: Implement GET /items/{item_id} endpoint
# Should return a single item by ID, or raise 404 if not found
@app.get("/items/{item_id}")
def get_item(item_id: int):
    pass


# TODO: Implement POST /items endpoint
# Should accept an Item model and add it to the list
@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item):
    pass


# TODO: Implement PUT /items/{item_id} endpoint
# Should update an existing item, or raise 404 if not found
@app.put("/items/{item_id}")
def update_item(item_id: int, item):
    pass


# TODO: Implement DELETE /items/{item_id} endpoint
# Should remove an item by ID, or raise 404 if not found
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
