class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def dfsrecur(openbracket,closebracket,bracket):
            if len(bracket)==2*n:
                result.append(bracket)
                return
            if openbracket<n:
                dfsrecur(openbracket+1,closebracket,bracket+'(')
            if closebracket<openbracket:
                dfsrecur(openbracket,closebracket+1,bracket+')')
        dfsrecur(0,0,"")
        return result

        
       
            
        backtrack(0,0)
        return res