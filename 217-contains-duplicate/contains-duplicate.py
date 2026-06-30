class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freqdup={}
        for i in nums:
            if i in freqdup:
                return True
            else:
                freqdup[i]=1
        return False

        