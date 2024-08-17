class Node(object):
    value = None
    previousMin = None

class MinStack(object):
    numbers = []
    currentMin = None

    def __init__(self):
        """
        """
        self.currentMin = None

    def push(self, val):
        item = Node()
        item.value = val

        if self.currentMin == None or val <= self.currentMin:
            item.previousMin = self.currentMin
            self.currentMin = val
        else:
            item.previousMin = self.currentMin

        self.numbers.append(item)

    def pop(self):
        item = self.numbers[len(self.numbers)-1]
        self.numbers.pop()
        self.currentMin = item.previousMin

    def top(self):
        item = self.numbers[len(self.numbers)-1]
        return item.value
        

    def getMin(self):
        return self.currentMin
