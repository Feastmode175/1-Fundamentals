class Stack:
  def __init__(self):
    self.items = []
    
  def push(self, value):
    self.items.append(value)
    
  def pop(self):
    if len(self.items) == 0:
      return None
    return self.items.pop()
  
def size(self):
  return len(self.items)