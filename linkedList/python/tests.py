import unittest
from linkedList import LinkedList

class tests(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList(range(4))

    def testEmptyLength(self):
        linkedList = LinkedList()
        self.assertEqual(len(linkedList), 0)

    def testElementValues(self):
        elements = range(4)
        self.assertEqual(list(self.list), elements)

    def testInsert(self):
        elements = [4] + range(4)
        self.list.insert(4)
        self.assertEqual(list(self.list), elements)

    def testInsertMultiple(self):
        elements = range(4) * 2
        self.list.insert(range(4))
        self.assertEqual(list(self.list), elements)

    def testInsertAt(self):
        elements = [0, 1, 4, 2, 3]
        self.list.insertAt(4, 2)
        self.assertEqual(list(self.list), elements)

    def testInsertAtMultipe(self):
        elements = [0, 1, 4, 5, 6, 2, 3]
        self.list.insertAt([4, 5, 6], 2)
        self.assertEqual(list(self.list), elements)

    def testInsertAtEnd(self):
        elements = range(4) + range(5)
        self.list.insertAt(range(5), len(self.list))
        self.assertEqual(list(self.list), elements)        

    def testRemove(self):
        elements = [1, 2, 3]
        self.list.remove()
        self.assertEqual(list(self.list), elements)

    def testRemoveAt(self):
        elements = [0, 2, 3]
        self.list.removeAt(1)
        self.assertEqual(list(self.list), elements)

    def testRemoveAtEnd(self):
        elements = [0, 1, 2]
        self.list.removeAt(len(self.list) - 1)
        self.assertEqual(list(self.list), elements)
        
    def testLength(self):
        self.assertEqual(len(self.list), 4)

if __name__ == '__main__':
    unittest.main()
