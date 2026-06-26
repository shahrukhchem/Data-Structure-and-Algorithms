class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        fruitset={}
        n=len(fruits)
        ans=0
        for right in range(n):
            if fruits[right] in fruitset:
                fruitset[fruits[right]]+=1
            else:
                fruitset[fruits[right]]=1
            while len(fruitset)>=3:
                fruitset[fruits[left]]-=1
                if fruitset[fruits[left]] == 0:
                    del fruitset[fruits[left]]
                left=left+1
            ans=max(ans,right-left+1)
        return ans

        