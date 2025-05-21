from node import NodeHT
import random

class HashTable:
    def __init__ (self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity
    
    def _hash(self, key):
        return hash(key) % self.capacity
    
    def add(self, key, value):
        index = self._hash(key)
        
        if self.table [index] is None:
            self.table[index] = NodeHT(key, value)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = NodeHT (key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1
        
    def delete(self, key):
        index = self._hash(key)
        
        previous = None
        current = self.table[index]
        
        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
        previous = current
        current = current.next

    def find(self, key):
        index = self._hash(key)
        
        current = self.table[index]
        while current:
            if current.key == key:
                print(current.value)
                return
            current = current.next
        print("not found")
    
    def randomElement(self):
        elements = []

        for element in self.table:
            current = element
            while current:
                elements.append(current.value)
                current = current.next

        if elements:
            return random.choice(elements)
        else:
            return None


    def contains(self, key):
        try: 
          self.find(key) 
          return True
        except KeyError: 
          return False

    def iter(self):
        for element in self.table:
          current = element
          if current:
            yield (current.key, current.value)
            current = current.next
