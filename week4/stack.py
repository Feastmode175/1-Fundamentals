class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    
class Stack:
  def __init__(self):
    self.head = None
    self.num_nodes = 0
    
  def push(self, value):
    #create new node to pop on stack
    new_node = Node(value)
    
    #if there is a current head node link it as next node to new node
    if self.head is not None:
      new_node.next = self.head
    
    #assign new_node as head node
    self.head = new_node
    self.num_nodes += 1
    
  def pop(self):
    # make sure there are items in the stack
    if self.head == None:
      return None
    
    #store value to return before removing
    pop_node = self.head.value
    #move head node to second node in stack (thus deleting first node)
    self.head = self.head.next
    self.num_nodes -= 1
    return pop_node
  
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

#conditional expression
print('Pass' if (stack.num_nodes == 5) else 'Fail')
stack.push(5)
print('Pass' if (stack.num_nodes == 5) else 'Fail')