class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l=1
        r=len(nums)
        from bisect import bisect_left
        def issubsequencepossible(size):
            tails = []
            for x in nums:
                idx = bisect_left(tails, x)
                if idx < len(tails):
                    tails[idx] = x
                else:
                    tails.append(x)
                if len(tails) >= size:
                    return True
            return False
        for i in range(l,r+1):
            if not issubsequencepossible(i):
                return i-1
        return r


