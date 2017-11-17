class Node():
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def __str__(self):
    return str(self.value)

  def get_index(self, index):
    current_node = self
    while index > 0:
      current_node = current_node.next
      index -= 1
    return current_node

  # def insert_at(self, node, position):
  #   prev = self.get_index(position-1)
  #   lastNext = None if prev.next is None else prev.next
  #   current = node
  #   prev.next = current
  #   current.next = lastNext
    
  def scan(self, value):
    if self is None:
      return False
    elif self.value == value:
      return True
    elif self.next is None:
      return False
    else:
      return self.next.scan(value)
  
  def count_iterative(self):
    i = 1
    current = self
    while current.next is not None:
      current = current.next
      i += 1
    return i

  def count_recursive(self):
    return 1 if self.next is None else 1 + self.next.count_recursive()

  def insert_front(self, value):
    my_new_list = Node(value)
    my_new_list.next = self
    return my_new_list

  def remove_from_front(self):
    return self.next

my_list = Node(0, Node(1, Node(2, Node(3))))

print(my_list.scan(1))
print(my_list.scan(2))
print(my_list.scan(3))
my_list = my_list.insert_front(5)
print(my_list.scan(5))
my_list = my_list.remove_from_front()
print(my_list.scan(5))
print(my_list.count_iterative())
print(my_list.count_recursive())
print(my_list.get_index(0))
print(my_list.get_index(1))
print(my_list.get_index(2))
