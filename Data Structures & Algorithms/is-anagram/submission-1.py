class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)
        # s=list(s)
        # t=list(t)
        # s.sort()
        # t.sort()
        # if s==t:
        #     return True
        # else:
        #     return False
