class Queue:
  def __init__(self, DefaultSize = 10, head = 0, tail = 0, count = 0):
    self.DefaultSize = DefaultSize
    self.array = [None] * self.DefaultSize
    self.head = head
    self.tail = tail
    self.count = count 

  def Enqueue(self, value):
    if len(self.array) == self.count:
      raise IndexError
    self.array[self.tail] = value
    self.tail = self.tail + 1
    if(self.tail > len(self.array) - 1):
      self.tail = 0
    self.count = self.count + 1

  def Dequeue(self):
    if self.count == 0:
      raise IndexError
    frontVal = self.array[self.head]
    self.head = self.head + 1
    if(self.head > len(self.array) - 1):
      self.head = 0
    self.count = self.count - 1
    return frontVal
    
def Main(): 
  q = Queue(4)
  q.Enqueue(5)
  q.Enqueue(3)
  q.Enqueue(13)
  q.Dequeue()
  q.Enqueue(8)

  while q.count > 0:
    print("Dequeue {0} ".format(q.Dequeue()))

Main()
