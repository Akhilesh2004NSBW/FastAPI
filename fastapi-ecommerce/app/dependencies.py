from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from app.jwt import SECRET_KEY, ALGORITHM

def get_current_user(token: str = Depends()):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from app.jwt import SECRET_KEY, ALGORITHM

def get_current_user(token: str = Depends()):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

@app.post("/products")
def create_product_api(
    product: Product,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    return create_product(db, product)

