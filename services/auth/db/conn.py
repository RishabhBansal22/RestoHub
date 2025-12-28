from config.base_config import Vars
from sqlalchemy import create_engine

settings = Vars()
DB_CONNECTION_URL = f"{settings.DRIVER}://{settings.USER}:{settings.PASSWORD}@{settings.HOST}:{settings.PORT}/{settings.DATABASE}"

engine = create_engine(url=DB_CONNECTION_URL, echo=True)

