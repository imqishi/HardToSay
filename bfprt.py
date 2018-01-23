class BFPRT(object):
    def go(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        numLen = len(nums)
        k = numLen - k + 1
        index = self.bfprt(nums, 0, numLen - 1, k)
        return nums[index]
    
    def insertSort(self, arr, left, right):
        for i in range(left + 1, right + 1):
            t = arr[i]
            j = i - 1
            while j >= left and arr[j] > t:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = t

        return ((right - left) / 2) + left;

    def getPivotIndex(self, arr, left, right):
        if right - left < 5:
            return self.insertSort(arr, left, right)

        i = j = left
        # every 5 elements as a team and find median
        # then put them to left
        while i + 4 <= right:
            index = self.insertSort(arr, i, i + 4)
            arr[j], arr[index] = arr[index], arr[j]
            j += 1
            i += 5
        
        return self.bfprt(arr, left, j, ((j - left + 1) / 2) + 1)
    
    def partition(self, arr, left, right, pivot_index):
        # put pivot element to end
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

        # prepare for put nums which less than pivot to divide_index ++
        divide_index = left
        for i in range(left, right):
            if arr[i] < arr[right]:
                arr[divide_index], arr[i] = arr[i], arr[divide_index]
                divide_index += 1

        # re-put pivot to new-pivot pos
        # here left is all less than pivot and right is all more than pivot
        arr[divide_index], arr[right] = arr[right], arr[divide_index]

        return divide_index

    def bfprt(self, arr, left, right, k):
        pivot_index = self.getPivotIndex(arr, left, right)
        divide_index = self.partition(arr, left, right, pivot_index)
        num = divide_index - left + 1;

        if num == k:
            # find target
            return divide_index
        elif num > k:
            # find in left
            return self.bfprt(arr, left, divide_index - 1, k)
        else:
            # find in right
            return self.bfprt(arr, divide_index + 1, right, k - num)

obj = BFPRT()
print obj.go([1,5,4,6,2,3], 6)
