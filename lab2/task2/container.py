import json
import os
import re


class Container:
    _username: str
    _storage: set[str] = set()
    _filename: str

    def __init__(self, username: str):
        self._username = username
        self._filename = f'./data/{username}.json'
        self.load(self._filename)

    def add(self, key):
        self._storage.add(key)

    def remove(self, key):
        if key in self._storage:
            self._storage.remove(key)

    def find(self, key) -> bool:
        return key in self._storage

    def list(self):
        return list(self._storage)

    def grep(self, regex):
        return list(filter(lambda key: re.match(regex, key), self._storage))

    def save(self, files):
        os.makedirs(os.path.dirname(f'./data/{files}.json'), exist_ok=True)
        with open(f'./data/{files}.json', "w") as outfile:
            json.dump(list(self._storage), outfile)

    def load(self, files):
        if os.path.exists(f'./data/{files}.json'):
            with open(f'./data/{files}.json', 'r') as infile:
                self._storage = set(json.load(infile))

    def switch(self, username: str):
        self._username = username
        self._filename = f'./data/{username}.json'
        self._storage.clear()
        self.load(self._filename)
