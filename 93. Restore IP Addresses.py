class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res = []
        self.subRestore(s, 1, [])
        return self.res
        
    def subRestore(self, s, level, ip):
        if s == '':
            return
        if level == 4:
            if int(s) < 256:
                if len(s) == 1:
                    self.res.append(".".join(ip) + "." + s)
                elif len(s) > 1 and s[0] != '0':
                    self.res.append(".".join(ip) + "." + s)
            return

        for i in range(1, 4):
            if int(s[:i]) > 255:
                continue
            if s[0] == '0':
                ip.append(s[:1])
                ok = self.subRestore(s[1:], level+1, ip)
                ip.pop()
                break
            else:
                ip.append(s[:i])
                ok = self.subRestore(s[i:], level+1, ip)
                ip.pop()

obj = Solution()
obj.restoreIpAddresses('010010')