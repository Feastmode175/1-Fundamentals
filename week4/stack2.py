class Stack:
  def __init__(self):
    self.items = []
    
  def push(self, value):
    self.items.append(value)
    
def size(self):
  return len(self.items)

def pop(self):
  if self.size() == 0:
    return None
  return self.items.pop()
  