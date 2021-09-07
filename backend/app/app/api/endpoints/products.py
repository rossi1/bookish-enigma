from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.crud_product import product as crud
from app.api import deps

from app.schemas.product import Product, ProductCreate, ProductUpdate

router = APIRouter()

@router.get("/", response_model=List[Product])
def read_products(db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100) -> Any:
    """
    Retrieve products.
    """
    try:
        products = crud.get_multi(db, skip, limit)
    except Exception as e:
        
        raise HTTPException(status_code=500, detail="Server Side Error.")
    else:
        return products


@router.post("/", response_model=Product)
def create_product(*, db: Session = Depends(deps.get_db), product_in: ProductCreate) -> Any:
    """
    create product.
    """
    try:
        product = crud.create(db, product_in)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Server Side Error.")
    else:
        return product


@router.put("/{id}", response_model=Product)
def update_product(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    product_in: ProductUpdate
) -> Any:
    """
    Update a product.
    """
    product = crud.get(db=db, id=id)
    if not product:
        raise HTTPException(status_code=404, detail="product not found")
  
    try:
        product = crud.update(db=db, db_obj=product, obj_in=product_in)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Server Side Error.")
    else:
        return product


@router.get("/{id}", response_model=Product)
def read_product(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> Any:
    """
    Get product by ID.
    """
    try:
        product = crud.get(db=db, id=id)
    except Exception as e:
        raise 
    else:
        if not product:
            raise HTTPException(status_code=404, detail="product not found")
        return product


@router.delete("/{id}", response_model=Product)
def delete_item(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
   
) -> Any:
    """
    Delete a product.
    """
    product = crud.get(db=db, id=id)
    if not product:
        raise HTTPException(status_code=404, detail="product not found")
   
    product = crud.remove(db=db, id=id)
    return product

