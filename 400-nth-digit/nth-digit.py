class Solution:
    def findNthDigit(self, n: int) -> int:
        #9,90,900,9000 and so on
        #9,180,2700,36000
        totalsumdigit=0
        count=0
        while totalsumdigit<n:
            totalsumdigit+=(9*(10**count))*(count+1)
            count+=1
        print(totalsumdigit-(9*(10**(count-1)))*(count))
        digitsremaining=n-(totalsumdigit-(9*(10**(count-1)))*(count))
        print(digitsremaining)
        print(count)
        print('digit exhausted of size',count,'-',digitsremaining//count)
        print('digit exhausted uptill',10**(count-1) +(digitsremaining//count)-1)
        print('remaining digit',digitsremaining%count)
        k=10**(count-1) +(digitsremaining//count)-1
        L=digitsremaining%count
        if L==0:
            return int(str(k)[-1])
        else:
            k=k+1
            k=str(k)
            return int(k[(digitsremaining%count)-1])

        '''
        print(9*(10**(count-2)))
        print(9*(10**(count-1)))
        print(9*(10**(count-1))-n)
        print(n//(9*(10**(count-2))))
        print(n%(9*(10**(count-2))))
        '''

        