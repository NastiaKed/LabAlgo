import unittest


from main import has_cycle, is_cyclic


class TestCycleDetection(unittest.TestCase):
    def test_cycle_in_graph(self):
        graph = {
            1: [2],
            2: [1, 3],
            3: [2],
        }
        self.assertTrue(has_cycle(graph))

    def test_no_cycle_in_graph(self):
        graph = {
            1: [2, 3],
            2: [1, 3],
            3: [2, 1],
        }
        self.assertFalse(has_cycle(graph))

    def test_single_node_graph(self):
        graph = {
            1: [],
        }
        self.assertFalse(has_cycle(graph))

    def test_cycle_in_large_graph(self):
        graph = {
            1: [2],
            2: [1, 3],
            3: [2, 4],
            4: [3, 5],
            5: [4, 1],
        }
        self.assertTrue(has_cycle(graph))

    def test_no_cycle_in_large_graph(self):
        graph = {
            1: [2, 3],
            2: [1, 4],
            3: [1, 5],
            4: [2, 6],
            5: [3, 6],
            6: [4, 5],
        }
        self.assertFalse(has_cycle(graph))

    def test_is_cyclic_with_cycle(self):
        graph = {
            1: [2, 3],
            2: [1, 3],
            3: [2, 1],
        }
        self.assertTrue(is_cyclic(1, graph, set()))

    def test_is_cyclic_without_cycle(self):
        graph = {
            1: [2, 3],
            2: [1, 4],
            3: [1, 5],
            4: [2, 6],
            5: [3, 6],
            6: [4, 5],
        }
        self.assertFalse(is_cyclic(1, graph, set()))


if __name__ == "__main__":
    unittest.main()
