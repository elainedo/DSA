import random
class Suffle:
    def __init__(self, nums):
        self.original = nums[:]
        self.suffled = nums[:]

    def suffle(self):
        for i in range(len(self.original)-1):
            index = random.randint(i, len(self.original)-1)
            self.suffled[i], self.suffled[index] =  self.suffled[index], self.suffled[i]
        return self.suffled
    
    def reset(self):
        return self.original

# Testing 

S = Suffle([1, 2, 3])
print(S.suffle())
print(S.reset())