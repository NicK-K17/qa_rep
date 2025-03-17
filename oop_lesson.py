import json

class CountryData:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.read_file()
        self.country = self.data['Country']
        self.avf_temp = self.data['avg_temp']
    def read_file(self):
        file_data = open(self.file_path, 'r')
        data = json.load(file_data)
        file_data.close()
        return data

class CountryDataWithMinTemp(CountryData):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.min_temp = self.data['min_temp']

data1 = CountryData('data/data1.txt')
print(data1.country)


