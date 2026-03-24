from collections import deque
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n=len(arr)
        l=0
        r=0
        indosize=r-l+1
        currindo=deque()
        totaldisfromx=0
        maxdist=float('inf')
        for l in range(0,n-k+1):
            while r-l+1<k+1:
                currindo.append(arr[r])
                totaldisfromx=totaldisfromx+abs(arr[r]-x)
                r=r+1
            if totaldisfromx<maxdist:
                maxdist=totaldisfromx
                res=currindo.copy()
            totaldisfromx=totaldisfromx-abs(currindo[0]-x)
            currindo.popleft()
        return list(res)
            