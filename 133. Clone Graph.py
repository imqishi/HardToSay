# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    mapper = {}
    def cloneGraph(self, node):
        if node is None:
            return None
        if node in self.mapper:
            return self.mapper[node]

        self.mapper[node] = UndirectedGraphNode(node.label)
        for item in node.neighbors:
            self.mapper[node].neighbors.append(self.cloneGraph(item))
        return self.mapper[node]

    def cloneGraphByBFS(self, node):
        if node is None:
            return None
        head = UndirectedGraphNode(node.label)
        self.mapper[node] = head
        queue = [ node ]
        while len(queue) != 0:
            tmp = queue[0]
            queue = queue[1:]
            for item in tmp.neighbors:
                if item not in self.mapper:
                    self.mapper[item] = UndirectedGraphNode(item.label)
                    queue.append(item)
                self.mapper[tmp].neighbors.append(self.mapper[item])
        
        return head


a = UndirectedGraphNode(1)
b = UndirectedGraphNode(2)
c = UndirectedGraphNode(3)
a.neighbors = [b, c]
b.neighbors = [a, c]
c.neighbors = [a, b, c]
obj = Solution()
dd = obj.cloneGraphByBFS(a)
print dd.label, dd.neighbors[0].label