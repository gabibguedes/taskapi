from fastapi import FastAPI
from routes import router
import os
from fastapi_sqlalchemy import DBSessionMiddleware

app = FastAPI(routes=router.routes)

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])
