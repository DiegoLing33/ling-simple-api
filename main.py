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

from database.database import engine, Base
from middleware import use_content_type
from routers import users, groups, auth

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

# Adding routes
app.include_router(
    users.router,
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

# Entry point
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
