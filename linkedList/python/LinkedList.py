#Singly Linked List
    
class LinkedList:
    def __eq__(self, other):
        if len(self) != len(other):
           return False
        return set(self) == set(other)
           
    def __init__(self, elements=None):
        self.length = 0
        self.head = None
        if elements is not None:
            self.insertAt(elements, 0)

    def __iter__(self):
        t = self.head
        while t:
            yield t.element
            t = t.next

    def __len__(self):
        return self.length
        
    def insert(self, element):
        self.insertAt(element, 0)

    def insertAt(self, element, index):
        if index < 0 or index > len(self):
            raise IndexError("list index out of range")
        prev = None
        cur = self.head
        for _ in range(index):
            prev = cur
            cur = cur.next
            
        if hasattr(element, '__iter__'):
            if len(element) <= 0:
                return
            t = _Node(element[0])
            last = t
            for e in element[1:]:
                last.next = _Node(e)
                last = last.next
            self.length += len(element)
        else:
            t = _Node(element)
            last = t
            self.length += 1
            
        if prev is None:
            self.head = t
            last.next = cur
        else:
            prev.next = t
            last.next = cur
        
    def remove(self):
        self.removeAt(0)

    def removeAt(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("list index out of range")
        prev = None
        cur = self.head
        for _ in range(index):
            prev = cur
            cur  = cur.next
            
        if prev is None:
            self.head = cur.next
        else:
            prev.next = cur.next
            
            
    def removeElement(self, element):
        if len(self) == 0:
            return
        prev = None
        cur = self.head
        while cur:
            if cur.element == element:
                if prev is None:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                self.length -= 1
                break
            prev = cur
            cur = cur.next
                    
    def search(self, element):
        t = self.head
        for i in range(self.length):
            if element == t.element:
                return t
            t = t.next
        return None
    
class _Node:
    def __init__(self, element):
        self.element = element
        self.next = None

    def __eq__(self, other):
        return self.element == other.element
