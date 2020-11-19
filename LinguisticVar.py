class LinguisticVar:
    def __init__ (self, name,**categories):
        self.name = name
        self.categories = categories

    def __getitem__(self, key):
        return self.categories[key]
        
