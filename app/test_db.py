from core.database import engine
from sqlalchemy import text  # required for SQL execution

with engine.connect() as conn:
    result = conn.execute(text("SHOW TABLES;"))  # wrap with text()
    for row in result:
        print(row)
