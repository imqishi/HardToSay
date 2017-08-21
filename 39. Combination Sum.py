class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # DP
        result = [[]]
        candidates.sort()
        for i in range(1, target+1):
            tmp = []
            j = 0
            while j < len(candidates) and candidates[j] <= i:
                if i == candidates[j]:
                    tmp.append([i])
                else:
                    for arrs in result[i - candidates[j]]:
                        if candidates[j] <= arrs[0]:
                            tmp.append([candidates[j]] + arrs)

                j += 1
            result.append(tmp)

        return result[target]

obj = Solution()
print obj.combinationSum([1,2,3,6,7], 7)
