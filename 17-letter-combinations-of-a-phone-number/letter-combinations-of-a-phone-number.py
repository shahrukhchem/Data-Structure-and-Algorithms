class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n=len(digits)
        sol,res=[],[]
        representation={}
        representation[2]='abc'
        representation[3]='def'
        representation[4]='ghi'
        representation[5]='jkl'
        representation[6]='mno'
        representation[7]='pqrs'
        representation[8]='tuv'
        representation[9]='wxyz'
        def dfsrecur(i,path):
            if i==len(digits):
                res.append("".join(path))
                return
            for choice in representation[int(digits[i])]:
                path.append(choice)
                dfsrecur(i+1,path)
                path.pop()
        dfsrecur(0,[])
        return res

        