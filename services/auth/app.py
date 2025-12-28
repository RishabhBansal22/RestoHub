from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/health/")
def getHealth():
    try:
       return JSONResponse(content="health check successfull, auth is running", status_code=200)
    except Exception as e:
        return JSONResponse(content="health check failed with exception(check logs)", status_code=400)