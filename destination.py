class Destination:
    def __init__(self, url, name, country):
        self.url = url
        self.name = name
        self.country = country

    def __eq__(self, other):
        return hash(self.url) == hash(other.url) 

    def __str__(self):
        return f'Nosaukums: {self.name}\nValsts: {self.country}\nSaite: {self.url}'
    
    def __hash__(self):
        return hash(self.url)