class Stack:
     def __init__(self):
         self.stack = []
        
     def Pop(self):
         return self.stack.pop()
      
     def Top(self):
         return self.stack[-1]

     def isEmpty(self):
         return self.stack == []

     def Push(self, item):
         self.stack.append(item)
        
     def Size(self):
         return len(self.stack)

class RPN:
    def __init__(self):
        self.stack = Stack()

    def process(self, str):
        try:
            self.stack.Push(int(str))
        except ValueError:
            top = self.stack.Pop()
            beneath = self.stack.Pop()

            if str == "+":
                result = beneath + top
                self.stack.Push(result)
                self.result()
            elif str == "-":
                result = beneath - top
                self.stack.Push(result)
                self.result()
            elif str == "*":
                result = benath * top
                self.stack.Push(result)
                self.result()
            elif str == "/":
                result = beneath / top
                self.stack.Push(result)
                self.result()

    def result(self):
        print(f"={self.stack.Top()}")


rpn = RPN()

print("RPN Calculator:")
while True:
    rpn.process(input(">"))