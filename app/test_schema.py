from services.schema_service import SchemaService

schema = SchemaService().build_context_string()
print(schema)
