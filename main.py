import json
import hashlib

FILE = 'countries.json'
FILE_WIKI_LINKS = 'generators_hash.txt'
URL = 'https://simple.wikipedia.org/wiki/'


class WikiLinks:
    """класс итератора, который по каждой стране из файла countries.json ищет страницу из википедии"""
    def __iter__(self):
        return self

    def __init__(self, file):
        try:
            self.file = open(file)
            self.file_json = json.load(self.file)
            self.count = 0
        except FileNotFoundError:
            print(f'Имя файла {file} указано не верно')
            exit()

    def __next__(self):
        if self.count < len(self.file_json[:]):
            self.value = self.file_json[self.count]['name']['common']
            self.count += 1
        else:
            self.file.close()
            raise StopIteration
        return self.value


for value_country in iter(WikiLinks(FILE)):
    with open(FILE_WIKI_LINKS, 'a', encoding='utf-8') as f:
        f.write(f"{value_country} - {URL}{value_country}\n")


def simple_generator(file):
    """Генератор, который принимает путь к файлу. При каждой итерации возвращает md5 хеш каждой строки файла."""
    count = 0
    with open(file, 'r', encoding='utf-8') as fw:
        while count < len(open(file).readlines()):
            hash_object = hashlib.md5(fw.readline().encode())
            count += 1
            yield hash_object.hexdigest()


for value_hash in simple_generator(FILE_WIKI_LINKS):
    print(value_hash)
