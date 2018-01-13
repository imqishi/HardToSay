class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total = 0
        redundant = 0
        start = 0
        for i in range(len(gas)):
            redundant += gas[i] - cost[i]
            if redundant < 0:
                start = i + 1
                total += redundant
                redundant = 0
        
        return start if total + redundant >= 0 else -1

obj = Solution()
print obj.canCompleteCircuit([1,2,3,3], [2,1,5,1])