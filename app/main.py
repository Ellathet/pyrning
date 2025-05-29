from fastapi import FastAPI
from app.api.main import api_router
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)

app = FastAPI(
  title="Pyring",
)

app.include_router(api_router)