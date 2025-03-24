import yaml
import random
import string


def generate_random_email():
    # Define valid characters for the email username
    username_chars = string.ascii_letters + string.digits + "._-"
    domain_chars = string.ascii_lowercase + string.digits + "-"

    # Generate a random username (3 to 15 characters long)
    username_length = random.randint(3, 15)
    username = ''.join(random.choices(username_chars, k=username_length))

    # Ensure the username starts and ends with an alphanumeric character
    if username[0] in "._-" or username[-1] in "._-":
        username = username.strip("._-")  # Trim invalid starting/ending characters

    # Generate a random domain name (3 to 10 characters long)
    domain_length = random.randint(3, 10)
    domain = ''.join(random.choices(domain_chars, k=domain_length))

    # Ensure the domain does not start or end with a hyphen
    if domain[0] == '-' or domain[-1] == '-':
        domain = domain.strip('-')  # Trim invalid starting/ending characters

    # Define a list of common top-level domains (TLDs)
    tlds = [".com", ".org", ".net", ".edu", ".info"]

    # Randomly select a TLD
    tld = random.choice(tlds)

    # Combine parts to create the email
    email = f"{username}@{domain}{tld}"
    return email


def generate_random_data(data_type):
    """Generate random data based on the given data type."""
    if data_type == "string":
        return ''.join(random.choices(string.ascii_letters, k=8))
    elif data_type == "integer":
        return random.randint(18, 65)
    elif data_type == "email":
        return generate_random_email()
    elif data_type == "phone_number":
        return f"+91-{random.randint(6000000000, 9999999999)}"  # US phone number format
    else:
        return None

def generate_data_from_schema(schema_file):
    """Generate data based on the schema defined in a YAML file."""
    with open(schema_file, "r") as file:
        schema = yaml.safe_load(file)

    generated_data = {}
    for key, fields in schema.items():
        generated_data[key] = []
        for field in fields:
            generated_data[key].append({k: generate_random_data(v) for k, v in field.items()})
    return generated_data

# print(generate_data_from_schema("/Users/amitsingh/Documents/projects/schema_data_generator/schema_data_generator/schema.yaml"))
 