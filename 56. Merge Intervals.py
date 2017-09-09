# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    
    def __str__(self):
        return '[' + str(self.start) + ',' + str(self.end) + ']'

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, lambda a,b:a.start-b.start)
        i = 0
        length = len(intervals)
        if length <= 1:
            return intervals
        result = []
        while i < length - 1:
            if intervals[i].end >= intervals[i+1].start:
                tmp = Interval(intervals[i].start, intervals[i].end)
                # find to last can be merged
                while i < length - 1:
                    if tmp.end < intervals[i+1].start:
                        break
                    # this is important
                    if tmp.end < intervals[i+1].end:
                        tmp.end = intervals[i+1].end
                    i += 1
                if tmp.end < intervals[i].end:
                    tmp.end = intervals[i].end
                result.append(tmp)
            else:
                result.append(intervals[i])

            i += 1

        if intervals[length-1].end > result[-1].end and intervals[length-1].end != result[-1].end:
            result.append(intervals[-1])
        
        return result

obj = Solution()
#rtn = obj.merge([Interval(2,3),Interval(4,5),Interval(6,7),Interval(8,9),Interval(1,10)])
#rtn = obj.merge([Interval(1,4), Interval(2,3)])
rtn = obj.merge([Interval(1,3),Interval(2,6),Interval(8,10),Interval(9,18)])
for item in rtn:
    print item