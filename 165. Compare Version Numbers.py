class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        versionList1 = version1.split('.')
        versionList2 = version2.split('.')
        if versionList1[0] == versionList2[0] == '':
            return 0
        elif versionList1[0] == '':
            return -1
        elif versionList2[0] == '':
            return 1

        len1 = len(versionList1)
        len2 = len(versionList2)
        if len1 < len2:
            for i in range(len2 - len1):
                versionList1.append(0)
        elif len1 > len2:
            for i in range(len1 - len2):
                versionList2.append(0)
            
        for (i, subVer) in enumerate(versionList1):
            if int(subVer) > int(versionList2[i]):
                return 1
            elif int(subVer) < int(versionList2[i]):
                return -1
        return 0


obj = Solution()
print obj.compareVersion('1.2.2.1', '1.2.2')