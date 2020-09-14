class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxStack = [] 

    def empty(self):
        return len(self.stack) == 0

    def get_max(self):
        if self.empty():
            raise IndexError('getMax(): empty stack')
        return self.maxStack[len(self.maxStack)-1]

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        self.maxStack.pop()
        return self.stack.pop()

    def push(self, element):
        self.stack.append(element)
        
        if len(self.stack) == 1:
            self.maxStack.append(element)
            return 
        
        if element > self.maxStack[-1]:
            self.maxStack.append(element)
        else:
            self.maxStack.append(self.maxStack[-1])


st = MaxStack()
#print(st.get_max())
st.push(4)
st.push(3)
st.push(5)

print(st.get_max())

st.pop()
st.pop()

print(st.get_max())

            