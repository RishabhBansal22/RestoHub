from pydantic_settings import BaseSettings, SettingsConfigDict

class Vars(BaseSettings):
    # JWT_SECRET_KEY: str
    # ACCESS_TOKEN_EXPIRE_MINUTES: int

    DRIVER:str
    HOST:str
    PORT:int
    USER:str
    PASSWORD:str
    DATABASE:str 

    #redis
    # REDIS_HOST:str
    # REDIS_PORT:int

    model_config = SettingsConfigDict(env_file=r"D:\restohub\services\auth\.env")





