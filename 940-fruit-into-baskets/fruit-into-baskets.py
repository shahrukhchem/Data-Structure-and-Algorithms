class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        n=len(fruits)
        r=0
        currfruits={}
        maxfruit=0
        for l in range(0,n):
            while  r<n:
                currfruits[fruits[r]] = currfruits.get(fruits[r], 0) + 1
                if len(currfruits)>=3:
                    currfruits[fruits[r]] = currfruits.get(fruits[r], 0) - 1
                    if currfruits[fruits[l]]==0:
                        currfruits.pop(fruits[l])
                    break
                maxfruit=max(maxfruit,r-l+1)
                r=r+1
            currfruits[fruits[l]] = currfruits.get(fruits[l], 0) - 1
            if currfruits[fruits[l]]==0:
                currfruits.pop(fruits[l])
        return maxfruit
            

        