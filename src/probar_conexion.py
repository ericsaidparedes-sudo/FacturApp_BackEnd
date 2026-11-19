from sqlalchemy import text
from models import engine

with engine.connect() as conn:
    print("Conexión exitosa:", conn.execute(text("SELECT 1")).scalar())
    