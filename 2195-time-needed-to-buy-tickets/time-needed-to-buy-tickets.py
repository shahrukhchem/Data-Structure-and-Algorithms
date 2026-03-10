
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        notbyk=tickets[k]
        currque= deque(range(len(tickets)))
        time=0
        while notbyk!=0:
            if currque:
                x= currque.popleft()
                tickets[x]=tickets[x]-1
                time=time+1
                if x==k:
                    notbyk=notbyk-1
                if tickets[x]!=0:
                    currque.append(x)
        return time
            
            
        
                    


        