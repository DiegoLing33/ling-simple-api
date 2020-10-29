#  ██╗░░░░░██╗███╗░░██╗░██████╗░░░░██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
#  ██║░░░░░██║████╗░██║██╔════╝░░░░██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
#  ██║░░░░░██║██╔██╗██║██║░░██╗░░░░██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
#  ██║░░░░░██║██║╚████║██║░░╚██╗░░░██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
#  ███████╗██║██║░╚███║╚██████╔╝░░░██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
#  ╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
#
#  Developed by Yakov V. Panov (C) Ling • Black 2020
#  @site http://ling.black

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from wow.router import character, guild
from database.database import engine, Base
from middleware import use_content_type
from routers import users, groups, auth, users_meta, data

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Ling API Service",
    description="This is example of the Ling API Service",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "users",
            "description": "User API methods"
        },
        {
            "name": "groups",
            "description": "User role groups API methods"
        },
        {
            "name": "auth",
            "description": "Authorization API methods"
        }
    ]
)
# Middlewares
use_content_type(app)

origins = [
    "http://localhost:3000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Adding routes
app.include_router(
    users.router,
    prefix="/users",
    tags=["users"]
)

app.include_router(
    users_meta.router,
    prefix="/users",
    tags=["users"]
)

app.include_router(
    groups.router,
    prefix="/groups",
    tags=["groups"]
)

app.include_router(
    auth.router,
    prefix="/auth",
    tags=["auth"]
)

app.include_router(
    data.router,
    prefix="/data",
    tags=["data"]
)

app.include_router(
    character.router,
    prefix="/characters",
    tags=['wow']
)

app.include_router(
    guild.router,
    prefix="/guild",
    tags=['wow']
)

app.mount("/static", StaticFiles(directory="static"))

# Entry point
if __name__ == "__main__":
    uvicorn.run("main:app", host="server.prestij.xyz", port=80, reload=True)
