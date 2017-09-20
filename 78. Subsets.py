import copy
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        all = []
        if len(nums) == 1:
            all.append([])
            all.append(nums)
            return all
        nums.sort()
        # init subres
        subres = []
        for i in nums:
            subres.append([i])
        all.append(subres)
        for i in range(2, len(nums)):
            newres = []
            for j in subres:
                for k in nums:
                    if k > j[-1]:
                        newres.append(copy.copy(j) + [k])
            all.append(copy.copy(newres))
            subres = newres

        all = reduce(lambda x, y: x + y, all)
        all.append([])
        all.append(nums)

        return all

obj = Solution()
print obj.subsets([1])