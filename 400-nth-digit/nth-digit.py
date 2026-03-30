class Solution:
    def findNthDigit(self, n: int) -> int:
        #9,90,900,9000 and so on
        #9,180,2700,36000
        totalsumdigit=0
        count=0
        while totalsumdigit<n:
            totalsumdigit+=(9*(10**count))*(count+1)
            count+=1
        digitsremaining=n-(totalsumdigit-(9*(10**(count-1)))*(count))
        k=10**(count-1) +(digitsremaining//count)-1
        L=digitsremaining%count
        if L==0:
            return int(str(k)[-1])
        else:
            k=k+1
            k=str(k)
            return int(k[(digitsremaining%count)-1])

        