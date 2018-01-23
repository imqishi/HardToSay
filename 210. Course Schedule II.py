class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # change to mapper for easier use
        graph = []
        for i in range(numCourses):
            graph.append([])

        for e in prerequisites:
            # ensure unique
            if e[0] not in graph[e[1]]:
                graph[e[1]].append(e[0])

        # calculate node's in degree
        degrees = [0] * (numCourses + 1)
        for neighbors in graph:
            for node in neighbors:
                degrees[node] += 1
        
        ret = []
        for i in range(numCourses):
            j = 0
            while j < numCourses:
                if degrees[j] == 0:
                    ret.append(j)
                    break
                j += 1
            # if there's no node with 0 degree, must have a cycle
            if j == numCourses:
                return []
            # begin with 0-degree node
            degrees[j] = -1
            for node in graph[j]:
                degrees[node] -= 1
        
        return ret

obj = Solution()
#print obj.canFinish(3, [[1, 0], [1, 2]])
print obj.findOrder(2, [[1, 0]])
print obj.findOrder(1, [])