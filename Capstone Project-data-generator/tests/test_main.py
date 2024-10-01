import os
import pytest
import json
from main import generate_random_data, write_file

# Test data schema
test_schema = {
    "date": "timestamp",
    "name": "str:rand",
    "type": "['client', 'partner', 'government']",
    "age": "int:rand(1, 90)"
}

def test_generate_random_data():
    lines = 10
    data = generate_random_data(test_schema, lines)
    
    assert len(data) == lines
    for row in data:
        assert "date" in row
        assert "name" in row
        assert "type" in row
        assert "age" in row
        assert isinstance(row['age'], int)
        assert row['type'] in ['client', 'partner', 'government']

def test_write_file(tmp_path):
    test_data = [
        {"date": "2024-09-24T10:00:00", "name": "John Doe", "type": "client", "age": 30},
        {"date": "2024-09-24T11:00:00", "name": "Jane Smith", "type": "partner", "age": 25}
    ]
    
    file_path = tmp_path / "test_output.json"
    write_file(file_path, test_data)
    
    assert file_path.exists()
    with open(file_path) as f:
        lines = f.readlines()
        assert len(lines) == 2
        for line in lines:
            data = json.loads(line)
            assert "date" in data
            assert "name" in data
            assert "type" in data
            assert "age" in data


@pytest.mark.parametrize("schema, lines", [
    (test_schema, 10),
    (test_schema, 100),
])
def test_generate_files(tmp_path, schema, lines):
    file_name = "test_data"
    prefix = "test"
    file_path = tmp_path / f"{prefix}_{file_name}_0.json"
    
    data = generate_random_data(schema, lines)
    write_file(file_path, data)

    assert file_path.exists()
    with open(file_path) as f:
        lines = f.readlines()
        assert len(lines) == len(data)
