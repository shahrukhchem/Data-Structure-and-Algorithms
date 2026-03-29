class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        outputs=[]
        for i in s:
            if len(outputs)==0 and i=='#':
                continue
            else:
                if i =='#':
                    outputs.pop()
                else:
                    outputs.append(i)
        outputt=[]
        for i in t:
            if len(outputt)==0 and i=='#':
                continue
            else:
                if i =='#':
                    outputt.pop()
                else:
                    outputt.append(i)
        return outputs==outputt
        
        