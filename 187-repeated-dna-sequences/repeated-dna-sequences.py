class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n=len(s)
        print(n)
        if n<=9:
            return []
        else:
            l=0
            r=l+9
            window=r-l+1
            firstdna=s[l:r]
            alldna=set()
            alldna.add(firstdna)
            res=[]
            for i in range(0,n-9):
                print(l,r)
                currdna= firstdna=s[l:r+1]
                if currdna in alldna:
                    res.append(currdna)
                else:
                    alldna.add(currdna)
                l=l+1
                r=l+9
            return list(set(res))
        