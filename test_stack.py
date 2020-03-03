import unittest

from stack import Stack
from collections import deque


class StackTester(unittest.TestCase):

    def test_stack_init(self):
        stack = Stack()
        self.assertEqual(0, stack.size())

    def test_push_check_size(self):
        item = 9
        stack = Stack()
        stack.push(item)
        self.assertEqual(1, stack.size())

    def test_push_one_item(self):
        stack = Stack()
        stack.push(9)
        self.assertEqual(deque([9]), stack.items)

    def test_push_two_item_size(self):
        stack = Stack()
        stack.push(7)
        stack.push(5)
        self.assertEqual(2, stack.size())

    def test_push_check_items(self):
        stack = Stack()
        stack.push(5)
        stack.push(6)
        self.assertEqual(deque([5,6]), stack.items)

    def test_size_after_pop_one_item(self):
        stack = Stack()
        stack.push(9)
        stack.push(3)
        stack.pop()
        self.assertEqual(1, stack.size())

    def test_pop_after_push_two_values(self):
        stack = Stack()
        stack.push(8)
        stack.push(9)
        self.assertEqual(9, stack.pop())

    def test_push_size_string(self):
        stack = Stack()
        stack.push("Duck")
        stack.push("Honk")
        stack.pop()
        stack.pop()
        self.assertEqual(0, stack.size())

    def test_push_two_check_size(self):
        stack = Stack()
        stack.push("Honk")
        stack.push("Duck")
        stack.pop()
        self.assertEqual("Honk", stack.pop())

    def test_is_mpty_init(self):
        stack = Stack()
        self.assertEqual(0, stack.size())

    def test_is_empty_push_one(self):
        stack = Stack()
        stack.push(5)
        self.assertNotEqual(0, stack.size())

    def test_isempty_push_one_pop_one(self):
        stack = Stack()
        stack.push(1)
        stack.pop()
        self.assertEqual(0, stack.size())

    def test_pop_empty(self):
        stack = Stack()
        self.assertRaises(IndexError, stack.pop)


if __name__ == '__main__':
    unittest.main()