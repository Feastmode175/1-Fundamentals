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
        'Customer': customer,
        'Flavor': flavor,
        'Scoops': scoops
        }
      self.orders.enqueue(order)
      print('Order created!')
      
  def show_all_orders(self):
    print('\nAll Pending Ice Cream Orders:')
    for order in self.orders.items:
      print(order)
      
      
  def next_order(self):
    next_order = self.orders.dequeue()
    print('\nNext Order Up!\n', next_order)
    

shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()