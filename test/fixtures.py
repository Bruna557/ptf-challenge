class CacheFixture():
    def __init__(self):
        self.cache = {}

    def get_data(self, key):
        return self.cache.get(key)

    def set_data(self, key, data):
        self.cache[key] = data
