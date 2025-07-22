from sqlalchemy import inspect
from core.database import engine

class SchemaService:
    def get_table_info(self):
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        schema = {}
        for table in tables:
            columns = inspector.get_columns(table)
            schema[table] = [col['name'] for col in columns]
        return schema

    def build_context_string(self):
        schema = self.get_table_info()
        context_lines = []
        for table, cols in schema.items():
            context_lines.append(f"Table {table} has columns: {', '.join(cols)}")
        return "\n".join(context_lines)
