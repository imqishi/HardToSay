import copy
class Solution(object):
    result = []

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result = []
        path = []
        candidates.sort()
        self.dfs(candidates, 0, target, path)
        return self.result


    def dfs(self, cands, cur, target, path):
        if target == 0:
            self.result.append(copy.copy(path))
            return
        if target < 0:
            return
        i = cur
        while i < len(cands):
            if i > cur and cands[i] == cands[i-1]:
                i += 1
                continue
            path.append(cands[i])
            self.dfs(cands, i+1, target-cands[i], path)
            path.pop()
            i += 1

    def DP(self, candidates, target):
        candidates.sort()
        table = [None] + [set() for i in range(target)]
        for i in candidates:
            if i > target:
                break
            for j in range(target - i, 0, -1):
                table[i + j] |= {elt + (i,) for elt in table[j]}
            table[i].add((i,))
        return map(list, table[target])


obj = Solution()
print obj.combinationSum2([2], 1)
obj.DP([10, 1, 2, 7, 6, 1, 5], 8)
