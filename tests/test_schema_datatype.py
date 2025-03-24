from schema_data_generator.generator import generate_random_data

def test_generate_random_data():
    assert isinstance(generate_random_data("string"), str)
    assert isinstance(generate_random_data("integer"), int)
