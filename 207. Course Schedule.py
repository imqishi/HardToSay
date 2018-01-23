class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if len(prerequisites) == 0:
            return True

        # change to mapper for easier use
        edges = []
        for i in range(numCourses):
            edges.append([])

        for e in prerequisites:
            # ensure unique
            if e[0] not in edges[e[1]]:
                edges[e[1]].append(e[0])

        # calculate node's in degree
        degrees = [0] * (numCourses + 1)
        for neighbors in edges:
            for node in neighbors:
                degrees[node] += 1

        for i in range(numCourses):
            j = 0
            while j < numCourses:
                if degrees[j] == 0:
                    break
                j += 1
            # if there's no node with 0 degree, must have a cycle
            if j == numCourses:
                return False
            # begin with 0-degree node
            degrees[j] = -1
            for node in edges[j]:
                degrees[node] -= 1
        
        return True

    def canFinishByDFS(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if len(prerequisites) == 0:
            return True

        visited = onpath = [False] * numCourses

        # change to mapper for easier use
        edges = []
        for i in range(numCourses):
            edges.append([])

        for e in prerequisites:
            # ensure unique
            if e[0] not in edges[e[1]]:
                edges[e[1]].append(e[0])

        for i in range(numCourses):
            if visited[i] is False and self.dfs(edges, i, onpath, visited):
                return False
        
        return True
    
    def dfs(self, edges, node, onpath, visited):
        if visited[node]:
            return False

        onpath[node] = visited[node] = True
        for n in edges[node]:
            if onpath[n] or self.dfs(edges, n, onpath, visited):
                return True
        
        onpath[node] = False
        return False


obj = Solution()
#print obj.canFinish(3, [[1, 0], [1, 2]])
print obj.canFinishByDFS(3, [[1, 2],[1, 0], [0, 1]])