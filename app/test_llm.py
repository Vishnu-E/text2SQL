from services.llm_service import LLMService
from services.schema_service import SchemaService
from core.database import engine
from sqlalchemy import text

# Build schema context
schema = SchemaService().build_context_string()

# Set user question (natural language)
question = "List all albums with artist names"

# Generate SQL using LLM
sql = LLMService().generate_sql(question, schema)
print("Generated SQL:\n", sql)

# Execute SQL on MySQL using SQLAlchemy
with engine.connect() as conn:
    result = conn.execute(text(sql))
    #rows = [dict(row) for row in result.fetchall()]
    rows = result.mappings().all()


# Print results
print("\nQuery Results:")
for row in rows:
    print(row)
