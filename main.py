from typing import Union

from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app=FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates=Jinja2Templates(directory="templates")

class Item(BaseModel):
    name:str
    price:float
    is_offer: Union[bool, None]= None

@app.get("/")
async def read_root():
    return{"message":"Hello World"}

@app.get("/items/{item_id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("index.html", {"request": request, "id": id})


@app.put("/items/{item_id}")
def update_item(item_id: int, item:Item):
    return{"item_name":item.name, "item_id":item_id}


@app.get("/index")
def index():
    return Jinja2Templates('app/index.html')