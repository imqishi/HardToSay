class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        mapper = {
            1: 1,
            2: 2,
            3: 6,
            4: 24,
            5: 120,
            6: 720,
            7: 5040,
            8: 40320
        }
        numbers = range(1, n+1)
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            index, k = divmod(k, mapper[n])
            permutation += str(numbers[index])
            numbers.remove(numbers[index])

        return permutation

    def test(self, n, k):
        nums = range(1,n+1)
        for i in range(k - 1):
            nums = self.permOnebyOne(nums)
        return nums
        
    def permOnebyOne(self, nums):
        end = len(nums) - 1
        reverse = True
        swap_pos = False
        while end > 0:
            if nums[end-1] < nums[end]:
                reverse = False
                swap_pos = end - 1
                break
            else:
                end -= 1
                continue

        if reverse is True:
            nums.sort()
        else:
            i = swap_pos + 1
            bak_pos = False
            while i < len(nums):
                if nums[i] > nums[swap_pos]:
                    if bak_pos is False:
                        bak_pos = i
                    else:
                        bak_pos = i if nums[i] <= nums[bak_pos] else bak_pos
                i += 1

            nums[swap_pos], nums[bak_pos] = nums[bak_pos], nums[swap_pos]
            bak = nums[swap_pos+1:]
            bak.reverse()
            nums[swap_pos+1:] = bak

        return nums

obj = Solution()
print obj.test(4,7)
print obj.getPermutation(4,2)