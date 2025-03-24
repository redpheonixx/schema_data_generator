from .generator import generate_data_from_schema

if __name__ == "__main__":
    schema_file = "schema.yaml"
    data = generate_data_from_schema(schema_file)
    print(data)

