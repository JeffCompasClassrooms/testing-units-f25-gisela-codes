import unittest
from search_core import *

class test_search_core(unittest.TestCase):
    def setUp(self):
        self.graph = {}

    def neighbors(self, node):
        return self.graph.get(node, [])

    def test_bfs1(self):
        self.graph = {
            "A": ["B", "C"],
            "B": ["D"],
            "C": [],
            "D": []
        }
        path = bfs("A", "D", self.neighbors)
        self.assertEqual(path, ["A", "B", "D"])

    def test_ids1(self):
        self.graph = {
            "A": ["B", "C"],
            "B": ["D"],
            "C": [],
            "D": []
        }
        path = ids("A", "D", self.neighbors)
        self.assertEqual(path, ["A", "B", "D"])

    def test_bfs2(self):
        self.graph = {
            "A": ["B", "C"],
            "B": ["D"],
            "C": [],
            "D": [],
            "E": ["F"],   # disconnected component
            "F": []
        }
        path = bfs("A", "F", self.neighbors)
        self.assertEqual(path, None)

    def test_ids2(self):
        self.graph = {
            "A": ["B", "C"],
            "B": ["D"],
            "C": [],
            "D": [],
            "E": ["F"],   # disconnected component
            "F": []
        }
        path = ids("A", "F", self.neighbors)
        self.assertEqual(path, None)

    def test_bfs3(self):
        self.graph = {
            "A": ["B"],
            "B": ["A", "C"],  # cycle back to A
            "C": ["D"],
            "D": []
        }
        path = bfs("A", "D", self.neighbors)
        self.assertEqual(path, ["A", "B", "C", "D"])

    def test_ids3(self):
        self.graph = {
            "A": ["B"],
            "B": ["A", "C"],  # cycle back to A
            "C": ["D"],
            "D": []
        }
        path = ids("A", "D", self.neighbors)
        self.assertEqual(path, ["A", "B", "C", "D"])

    def test_bfs4(self):
        self.graph = {
            "A": ["B", "C"],
            "B": [],
            "C": [],
        }
        path = bfs("A", "D", self.neighbors)
        self.assertEqual(path, None)

    def test_ids4(self):
        self.graph = {
            "A": ["B", "C"],
            "B": [],
            "C": [],
        }
        path = ids("A", "D", self.neighbors)
        self.assertEqual(path, None)

    def test_bfs5(self):
        self.graph = {
            "A": ["B", "C"],
            "B": ["D"],
            "C": ["D"],
            "D": []
        }
        path = bfs("A", "D", self.neighbors)
        self.assertEqual(path, ["A", "B", "D"])

    def test_ids5(self):
        self.graph = {
            "A": ["B", "C"],
            "B": ["D"],
            "C": ["D"],
            "D": []
        }
        path = ids("A", "D", self.neighbors)
        self.assertEqual(path, ["A", "B", "D"])
    def test_bfs6(self):
        self.graph = {
            (0, 0): [(0, 1), (1, 0)],
            (0, 1): [(1, 1)],
            (1, 0): [],
            (1, 1): []
        }
        path = bfs((0, 0), (1, 1), self.neighbors)
        self.assertEqual(path, [(0, 0), (0, 1), (1, 1)])      
        
    def test_ids6(self):
        self.graph = {
            (0, 0): [(0, 1), (1, 0)],
            (0, 1): [(1, 1)],
            (1, 0): [],
            (1, 1): []
        }
        path = ids((0, 0), (1, 1), self.neighbors)
        self.assertEqual(path, [(0, 0), (0, 1), (1, 1)])


    def test_bfs7(self):
        self.graph = {
            "New York": ["Chicago", "Boston"],
            "Chicago": ["Denver"],
            "Boston": [],
            "Denver": []
        }
        path = bfs("New York", "Denver", self.neighbors)
        self.assertEqual(path, ["New York", "Chicago", "Denver"])

    def test_ids7(self):
        self.graph = {
            "New York": ["Chicago", "Boston"],
            "Chicago": ["Denver"],
            "Boston": [],
            "Denver": []
        }
        path = ids("New York", "Denver", self.neighbors)
        self.assertEqual(path, ["New York", "Chicago", "Denver"])

    def wgc_actions(self,state):
        neighbors = []
        f,w,g,c = state

        neighbors.append((1-f,w,g,c))

        if f == w:
            neighbors.append((1-f,1-w,g,c))
        if f == g:
            neighbors.append((1-f,w,1-g,c))
        if f == c:
            neighbors.append((1-f, w,g,1-c))

        actions = []

        for n in neighbors:
            f,w,g,c = n
            if f != w == g:
                continue
            if f != g == c:
                continue
            actions.append(n)
        return actions
    
    def test_wgc_bfs1(self):
        path = bfs((0,0,0,0), (1,1,1,1), self.wgc_actions)
        self.assertEqual(path, [(0, 0, 0, 0), (1, 0, 1, 0), (0, 0, 1, 0), (1, 1, 1, 0), (0, 1, 0, 0), (1, 1, 0, 1), (0, 1, 0, 1), (1, 1, 1, 1)])
    def test_wgc_ids1(self):
        path = ids((0,0,0,0), (1,1,1,1), self.wgc_actions)
        self.assertEqual(path, [(0, 0, 0, 0), (1, 0, 1, 0), (0, 0, 1, 0), (1, 1, 1, 0), (0, 1, 0, 0), (1, 1, 0, 1), (0, 1, 0, 1), (1, 1, 1, 1)])

    def test_wgc_bfs2(self):
        path = bfs((0,0,0,1), (1,1,1,1), self.wgc_actions)
        self.assertEqual(path, [(0, 0, 0, 1), (1, 1, 0, 1), (0, 1, 0, 1), (1, 1, 1, 1)])
    def test_wgc_ids2(self):
        path = ids((0,0,0,1), (1,1,1,1), self.wgc_actions)
        self.assertEqual(path, [(0, 0, 0, 1), (1, 1, 0, 1), (0, 1, 0, 1), (1, 1, 1, 1)])

    def test_wgc_bfs3(self):
        path = bfs((0,0,1,1), (1,1,1,1), self.wgc_actions)
        self.assertEqual(path, [(0, 0, 1, 1), (1, 1, 1, 1)])
    def test_wgc_ids3(self):
        path = ids((0,0,1,1), (1,1,1,1), self.wgc_actions)
        self.assertEqual(path, [(0, 0, 1, 1), (1, 1, 1, 1)])

    def test_wgc_bfs4(self):
        path = bfs((0,1,1,1), (1,1,1,1), self.wgc_actions)
        self.assertEqual(path, [(0, 1, 1, 1), (1, 1, 1, 1)])
    def test_wgc_ids4(self):
        path = ids((0,1,1,1), (1,1,1,1), self.wgc_actions)
        self.assertEqual(path, [(0, 1, 1, 1), (1, 1, 1, 1)])

    def test_wgc_bfs5(self):
        path = bfs((0,1,0,1), (1,1,1,1), self.wgc_actions)
        self.assertEqual(path, [(0, 1, 0, 1), (1, 1, 1, 1)])
    def test_wgc_ids5(self):
        path = ids((0,1,0,1), (1,1,1,1), self.wgc_actions)
        self.assertEqual(path, [(0, 1, 0, 1), (1, 1, 1, 1)])

    def test_wgc_ids6(self):
        path = ids((1,0,0,1), (1,1,1,1), self.wgc_actions)
        self.assertEqual(path, [(1, 0, 0, 1), (0, 0, 0, 1), (1, 1, 0, 1), (0, 1, 0, 1), (1, 1, 1, 1)])
    def test_wgc_bfs6(self):
        path = bfs((1,0,0,1), (1,1,1,1), self.wgc_actions)
        self.assertEqual(path, [(1, 0, 0, 1), (0, 0, 0, 1), (1, 1, 0, 1), (0, 1, 0, 1), (1, 1, 1, 1)])

    def test_wgc_ids7(self):
        path = ids((1,1,0,0), (1,1,1,1), self.wgc_actions)
        self.assertEqual(path, [(1, 1, 0, 0), (0, 1, 0, 0), (1, 1, 0, 1), (0, 1, 0, 1), (1, 1, 1, 1)])
    def test_wgc_bfs7(self):
        path = bfs((1,1,0,0), (1,1,1,1), self.wgc_actions)
        self.assertEqual(path, [(1, 1, 0, 0), (0, 1, 0, 0), (1, 1, 0, 1), (0, 1, 0, 1), (1, 1, 1, 1)])

    def test_wgc_ids8(self):
        path = ids((1,1,0,2), (1,1,1,1), self.wgc_actions)
        self.assertEqual(path, None)
    def test_wgc_bfs8(self):
        path = bfs((1,1,0,2), (1,1,1,1), self.wgc_actions)
        self.assertEqual(path, None)

if __name__ == "__main__":
    unittest.main()