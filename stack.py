class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)
    
    def __str__(self):
        returnString = ''
        for i in range(0, len(self.stack)):
            returnString += f'{i})\n{self.stack[-i]}\n'
        return returnString
    
class FixedSizeStack:
    def __init__(self, size):
        self.stack = []
        self.maxSize = size

    def push(self, value):
        if len(self.stack)>= self.maxSize:
            self.stack.pop(0)
        self.stack.append(value)

    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)
    
    def __str__(self):
        returnString = ''
        for i in range(0,self.maxSize):
            returnString += f'{i+1})---------------------\n{self.stack[-i]}\n'
        return returnString