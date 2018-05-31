import json
from hussh.utils.constants import home

class JsonFile(object):
    def __init__(self, path):
        self.path = path
    def read(self):
        data_dict = {}
        try:
            f = open(self.path, 'r')
            data = f.read()
            data_dict = json.loads(data)
            f.close()
        except:
            return {}
        return data_dict

    def write(self, data_dict):
        data = json.dumps(data_dict)
        f = open(self.path, 'w')
        f.write(data)
        f.close()

class Config(object):
    file_paths = {
        'Linux': '.husshconf',
    }
    def __init__(self, os):
        self.file_name = home + '/' +self.file_paths[os]
        self.f = JsonFile(self.file_name)
        self.config = self.f.read()
    def update_key(self, key, value):
        self.config[key] = value
        self.f.write(self.config)
    def read_key(self, key):
        return self.config.get(key, None)
