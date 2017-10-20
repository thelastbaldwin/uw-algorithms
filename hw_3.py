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
            if str == "+":
                result = self.stack.Pop() + self.stack.Pop()
                self.stack.Push(result)
                self.result(result)
            elif str == "-":
                top = self.stack.Pop()
                beneath = self.stack.Pop()
                result = beneath - top
                self.stack.Push(result)
                self.result(result)
            elif str == "*":
                result = self.stack.Pop() * self.stack.Pop()
                self.stack.Push(result)
                self.result(result)
            elif str == "/":
                result = self.stack.Pop() / self.stack.Pop()
                self.stack.Push(result)
                self.result(result)

    def result(self, val):
        print(f"={val}")


rpn = RPN()

print("RPN Calculator:")
print("***************")
while True:
    rpn.process(input(">"))