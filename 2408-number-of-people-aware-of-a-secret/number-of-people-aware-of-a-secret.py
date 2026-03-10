from collections import deque
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        members = deque()
        members.append((1,1+delay,1+forget))
        for day in range(2,n+1):
            #forgot
            q = deque([t for t in members if t[2] > day])
            #populate
            lqu = list(q)
            nepeople=0
            for t in lqu :
                if t[1] <= day:
                    nepeople+=t[0]
            if nepeople>0:
                q.append((nepeople,day+delay,day+forget))
            members=q
           
        total = sum(c for c,_,_ in members)
        return total%MOD
        


        