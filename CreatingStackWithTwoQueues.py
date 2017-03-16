class Queue:

    def __init__(self):
        self.tab = []

    def isEmpty(self):
        return len(self.tab) == 0

    def enqueue(self, item):
        return self.tab.insert(0, item)

    def dequeue(self):
        if self.isEmpty(): raise IndexError('nie mozna usunac elementy z pustej listy')
        return self.tab.pop()

    def size(self):
        return len(self.tab)

    def printqueue(self):
        print self.tab

    def first(self):
        if self.isEmpty(): raise IndexError('lista pusta')
        return self.tab[-1]


class CreatingStackWithTwoQueues:

    def __init__(self):
        self.kolejka1 = Queue()
        self.kolejka2 = Queue()

    def push(self, val):
        self.kolejka2.enqueue(item)
        while not self.kolejka1.isEmpty():
            self.kolejka2.enqueue(self.kolejka1.dequeue())
        while not self.kolejka2.isEmpty():
            self.kolejka1.enqueue(self.kolejka2.dequeue())

    def pop(self):
        return self.kolejka1.dequeue()

    def top(self):
        return self.kolejka1.first()

    def isEmpty(self):
        return self.kolejka1.isEmpty()

    def size(self):
        return self.kolejka1.size()
