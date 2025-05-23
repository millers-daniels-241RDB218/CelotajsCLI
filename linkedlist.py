import pickle
from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, destination):
        if self.contains(destination):
            print(f"Destination '{destination.name}' jau ir sarakstā. Netika pievienots.")
            return

        new_node = Node(destination)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def contains(self, destination):
        current = self.head
        while current:
            if current.value == destination:
                return True
            current = current.next
        return False
    
    def delete(self, url):
        current = self.head
        prev = None

        while current and hash(current.destination.url) != hash(url):
            prev = current
            current = current.next

        if not current:
            print("Atrašanās vieta nav atrasta!")
            return
        
        if prev:
            prev.next = current.next
        else:
            self.head = current.next

    def empty(self):
        return self.head == None

    def search(self, url):
        current = self.head
        while current:
            if hash(current.destination.url) == hash(url):
                return current.destination
            current = current.next
        return None
    
    def display(self):
        current = self.head
        while current:
            print(current.destination)
            current = current.next

    def save(self, file):
        with open(file, 'wb') as f:
            pickle.dump(self, f)
    
    def load(file):
        with open(file, 'rb') as f:
            return pickle.load(f)

    
    def __str__(self):
        current = self.head
        returnString = ''
        i = 0
        while current:
            returnString += f'{i+1})---------------------\n{current.value}\n'
            i += 1
            current = current.next
        return returnString    
