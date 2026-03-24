class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        n=len(fruits)
        r=0
        currfruits={}
        maxfruit=0
        for l in range(0,n):
            while  r<n:
                fr=fruits[r]
                currfruits[fr] = currfruits.get(fr, 0) + 1
                if len(currfruits)>=3:
                    currfruits[fr] = currfruits[fr] - 1
                    if currfruits[fr]==0:
                        currfruits.pop(fr)
                    break
                maxfruit=max(maxfruit,r-l+1)
                r=r+1
            fl=fruits[l]
            currfruits[fl] = currfruits.get(fl, 0) - 1
            if currfruits[fl]==0:
                currfruits.pop(fl)
        return maxfruit
            

        