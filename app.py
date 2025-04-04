from flask import Flask, jsonify
import yaml
import random
from faker import Faker

app = Flask(__name__)
fake = Faker()

def load_schema():
    with open('schema.yaml', 'r') as file:
        schema = yaml.safe_load(file)
    return schema


def generate_clickstream_data(schema):
    data = {}

    for field in schema["clickstream_data"]:
        field_name = list(field.keys())[0]
        field_type = list(field.values())[0]

        if isinstance(field_type, str):  
            if field_type == "string":
                data[field_name] = fake.word() if "event_id" not in field_name else fake.uuid4()
            elif field_type == "timestamp":
                data[field_name] = fake.iso8601()
            elif field_type == "int":
                data[field_name] = random.randint(1, 100)
            elif field_type == "float":
                data[field_name] = round(random.uniform(0.1, 100.0), 2)
        elif isinstance(field_type, dict):  
            nested_data = {}
            for nested_field, nested_type in field_type.items():
                if nested_type == "string":
                    nested_data[nested_field] = fake.city() if nested_field == "city" else fake.country()
                elif nested_type == "float":
                    nested_data[nested_field] = round(random.uniform(-90.0, 90.0), 6) if nested_field == "latitude" else round(random.uniform(-180.0, 180.0), 6)
            data[field_name] = nested_data

        elif isinstance(field_type, list):  
            array_data = []
            for _ in range(random.randint(1, 5)):
                nested_structure = {}
                for nested_field in field_type[0].keys():
                    nested_type = field_type[0][nested_field]
                    if nested_type == "string":
                        nested_structure[nested_field] = fake.word()
                    elif nested_type == "int":
                        nested_structure[nested_field] = random.randint(1, 10)
                    elif nested_type == "float":
                        nested_structure[nested_field] = round(random.uniform(0.1, 100.0), 2)
                array_data.append(nested_structure)
            data[field_name] = array_data

    return data

@app.route('/generate', methods=['GET'])
def generate():
    schema = load_schema()
    random_data=[]
    for i in range(random.randint(100, 1000)):
        random_data.append(generate_clickstream_data(schema))
    
    return jsonify(random_data)

if __name__ == '__main__':
    app.run(debug=True)
