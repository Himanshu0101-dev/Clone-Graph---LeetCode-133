# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, neighbors: list = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        # Dictionary to map original node -> cloned node
        visited = {}

        def dfs(curr: 'Node') -> 'Node':
            if curr in visited:
                return visited[curr]

            # Clone the current node
            clone = Node(curr.val)
            visited[curr] = clone

            # Clone all neighbors recursively
            for nei in curr.neighbors:
                clone.neighbors.append(dfs(nei))

            return clone

        return dfs(node)
