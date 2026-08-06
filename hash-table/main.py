class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self,paramStr):
        sumUnicode = 0
        for i in paramStr:
            sumUnicode += ord(i)
        return sumUnicode

    def add(self,key,value):
        keyUnicode = self.hash(key)
        if keyUnicode not in self.collection:
            self.collection[keyUnicode] = {}
        self.collection[keyUnicode][key] = value

    def remove(self,key):
        keyUnicode = self.hash(key)        
        if keyUnicode in self.collection and key in self.collection[keyUnicode]:
            del self.collection[keyUnicode][key]
        return None
    def lookup(self,key):
        keyUnicode = self.hash(key)        
        if keyUnicode in self.collection:
            return self.collection[keyUnicode].get(key)
        return None