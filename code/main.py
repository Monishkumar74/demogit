from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def read_root():
	return {"message": "GET method called"}

@app.post("/")
async def create_item(request: Request):
	data = await request.json()
	return {"message": "POST method called", "data": data}

@app.put("/")
async def update_item(request: Request):
	data = await request.json()
	return {"message": "PUT method called", "data": data}

@app.delete("/")
async def delete_item():
	return {"message": "DELETE method called"}

@app.patch("/")
async def patch_item(request: Request):
	data = await request.json()
	return {"message": "PATCH method called", "data": data}

@app.options("/")
async def options_item():
	return JSONResponse(content=None, headers={"Allow": "GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD"})

@app.head("/")
async def head_item():
	return JSONResponse(content=None)
