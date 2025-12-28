from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, Field
from src.base_auth import new_client

app = FastAPI()

class RestoSignup(BaseModel):
    first_name : str = Field(...)
    last_name : str = Field(...)
    email : EmailStr = Field(...)
    phone : str = Field(..., max_length=10)
    password : str = Field(..., min_length=5, max_length=15)

@app.get("/health/")
def getHealth():
    try:
       return JSONResponse(content="health check successfull, auth is running", status_code=200)
    except Exception as e:
        return JSONResponse(content="health check failed with exception(check logs)", status_code=400)

@app.post("/signup")
def signup(request:RestoSignup):
    try:
        result = new_client(
            first_name=request.first_name,
            last_name=request.last_name,
            email=request.email,
            phone=request.phone,
            password=request.password
        )
        
        if isinstance(result, dict):
            return JSONResponse(content=result, status_code=400)
        
        return JSONResponse(content={
            "message": "User created successfully", 
            "user": {
                "id": result.id,
                "email": result.email,
                "first_name": result.first_name,
                "last_name": result.last_name
            }
        }, status_code=201)
    except Exception as e:
        return JSONResponse(content={"message": f"Internal server error: {str(e)}"}, status_code=500)
