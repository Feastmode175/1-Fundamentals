class Queue:
  def __init__(self):
    self.items = []
    
  def size(self):
    return len(self.items)
  
  def enqueue(self, item):
    self.items.append(item)
    
  def dequeue(self):
    if self.size == 0:
      return None
    return self.items.pop(0)
  
  def show_queue(self):
    print(self.items)


class IceCreamShop:
  def __init__(self, flavors):
    self.flavors = flavors
    self.orders = Queue()
    
  def take_order(self, customer, flavor, scoops):
    if flavor not in self.flavors:
      print('Sorry! We do not have that flavor.')
    
    elif int(scoops) not in range(1, 4):
      print('Please select between 1 and 3 scoops.')
      
    else:
      order = {
        'customer': customer,
        'flavor': flavor,
        'scoops': scoops
        }
      self.orders.enqueue(order)
      print('Order created!')
