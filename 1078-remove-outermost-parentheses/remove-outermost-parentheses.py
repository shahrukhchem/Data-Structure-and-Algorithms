class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        brackets=[]
        open=0
        close=0
        ch=''
        for i in s:
            brackets.append(i)
            if i =='(':
                open+=1
            elif i==')':
                close+=1
            if open==close:
                brackets.pop()
                brackets.pop(0)
                open=0
                close=0
                for i in brackets:
                    ch+=i
                brackets=[]
        return ch
       

            

        