import os
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'data')
print(file_path)

def read_file():
    # менеджер контекста
    with open(os.path.join(file_path, 'data.txt')) as data_file:
        for line in data_file.readlines():
            yield line


for data_line in read_file():
    with open(os.path.join(file_path, 'new_data.txt'), 'a') as new_file:
        data_line = data_line.replace('.', '').replace(',', '')
        new_file.write(data_line)
