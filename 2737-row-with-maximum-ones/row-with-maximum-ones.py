class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxro=-1
        count=-1
        for i in mat:
            count+=1
            if maxro<sum(i):
                maxro=sum(i)
                ans=count 
        return [ans,maxro]