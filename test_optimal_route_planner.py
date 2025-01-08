import unittest
from optimal_route_planner import MinHeap


class TestMinHeap(unittest.TestCase):
    def setUp(self):
        # Create a MinHeap instance for testing
        self.heap = MinHeap()

    def test_push_and_pop(self):
        # Add items to the heap
        self.heap.push((10, 'A'))
        self.heap.push((5, 'B'))
        self.heap.push((15, 'C'))

        # Test pop order
        self.assertEqual(self.heap.pop(), (5, 'B'))  # Smallest
        self.assertEqual(self.heap.pop(), (10, 'A'))  # Next smallest
        self.assertEqual(self.heap.pop(), (15, 'C'))  # Largest

    def test_is_empty(self):
        # Test initially empty heap
        self.assertTrue(self.heap.is_empty())

        # Add an item and test
        self.heap.push((1, 'X'))
        self.assertFalse(self.heap.is_empty())

        # Remove the item and test again
        self.heap.pop()
        self.assertTrue(self.heap.is_empty())

    def test_sift_up(self):
        # Test internal heap property after multiple pushes
        self.heap.push((30, 'X'))
        self.heap.push((20, 'Y'))
        self.heap.push((10, 'Z'))

        # The smallest element should be at the root
        self.assertEqual(self.heap.pop(), (10, 'Z'))

    def test_sift_down(self):
        # Test internal heap property after multiple pops
        self.heap.push((50, 'P'))
        self.heap.push((40, 'Q'))
        self.heap.push((30, 'R'))
        self.heap.push((20, 'S'))
        self.heap.push((10, 'T'))

        # Pop and verify the order
        self.assertEqual(self.heap.pop(), (10, 'T'))
        self.assertEqual(self.heap.pop(), (20, 'S'))
        self.assertEqual(self.heap.pop(), (30, 'R'))
        self.assertEqual(self.heap.pop(), (40, 'Q'))
        self.assertEqual(self.heap.pop(), (50, 'P'))

    def test_mixed_operations(self):
        # Test mixed push and pop operations
        self.heap.push((5, 'A'))
        self.heap.push((10, 'B'))
        self.assertEqual(self.heap.pop(), (5, 'A'))  # Smallest first
        self.heap.push((2, 'C'))
        self.assertEqual(self.heap.pop(), (2, 'C'))  # Next smallest
        self.assertEqual(self.heap.pop(), (10, 'B'))  # Remaining element


if __name__ == '__main__':
    unittest.main()
