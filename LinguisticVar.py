class LinguisticVar:
    def __init__ (self, name,**categories):
        self.name = name
        self.categories = categories
        self.min = min([self.categories[x].a for x in self.categories ])
        self.max = max([self.categories[x].d for x in self.categories ])

    def __getitem__(self, key):
        return self.categories[key]

  
        
