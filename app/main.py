from fastapi import FastAPI, Response, File, UploadFile, Form, Request
from fastapi.middleware.cors import CORSMiddleware
from lib import extract_info_Func
from typing import Union, Annotated
from lib.server import *
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


''' 
    This Project is intend to scan and interpret contents on receipt of any kind as long as the following parameter is found on it:
    1. Bank Name
    2. Account Name
    3. Transaction Amount
    4. & Transaction date-time

'''

app = FastAPI()

app.add_middleware(CORSMiddleware, 
                    allow_origins = allow_origins,
                    allow_methods = allow_methods,
                    allow_headers = allow_headers,
                    allow_credentials = True
                )

# app.mount("templates", StaticFiles(directory='templates'), name="templates")
template = Jinja2Templates(directory='templates')

@app.get("/")
async def index(request: Request):
    return template.TemplateResponse(
        'index.html', {
            "request": request, 
            "baseURL": request.base_url
            })

# create process instance. give instruction and use

@app.post("/extract_info")
async def extract_info(
    file: Annotated[UploadFile, File()], 
    name: Annotated[str, Form()], 
    bank: Annotated[str, Form()]
    ):

    try:
        if file:
            response = await extract_info_Func(file, name, bank)
            return response

    except Exception as error:
        return {"name": "Error", "bank": "Error", "amount": "Error", "date": error, "status": False}

    return {"name": "None", "bank": "None", "amount": "0", "date": "None", "status": False}





