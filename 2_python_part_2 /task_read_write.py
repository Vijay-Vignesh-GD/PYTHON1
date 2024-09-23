import os

def read_files_and_write_result(directory: str, output_file: str):
    values = []
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read().strip()
                if content:
                    values.append(content)
                    
    with open(output_file, 'w', encoding='utf-8') as result_file:
        result_file.write(', '.join(values))

if __name__ == "__main__":
    directory = 'Documents/PYTHON/PYTHON-BASIC/practice/2_python_part_2/files'
    output_file = 'result.txt'
    read_files_and_write_result(directory, output_file)
