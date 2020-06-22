from fastapi import FastAPI, WebSocket, Request, File, Form, UploadFile, Depends, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import importlib
import DefinitionTools
from pathlib import Path
from pydantic import BaseModel
import add_new_text
import uvicorn
import secrets
from fastapi.responses import RedirectResponse
from typing import Optional
from routers.ToolsApp import lemmatize
from routers.sql_app import account
from routers import oracle, select
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
app = FastAPI()

app.include_router(lemmatize.router, prefix="/lemmatize", tags=["lemmatize"])
app.include_router(account.router, prefix = "/account", tags=["account"])
app.include_router(oracle.router, prefix = "/oracle", tags=["oracle"])
app.include_router(select.router, prefix = "/select", tags=["select"])
#sql_app is not on github intentionally

templates = Jinja2Templates(directory="templates")
app_path = Path.cwd()
static_path = app_path / "static" / "assets"
app.mount("/assets", StaticFiles(directory=static_path), name="assets")




@app.get("/")
async def index(request : Request):
    return templates.TemplateResponse("index.html", {"request": request})
    #buttons clicked on this page will take us to /select/{language}


 #End of select (or main?) code

if __name__ == "__main__":
    uvicorn.run("main:app", host="64.227.97.179", port=8000, forwarded_allow_ips= "107.204.214.0" , log_level="info")
