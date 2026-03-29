class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i in ['+','-','*','/']:
                if i=='+':
                   a= stack[-2]+stack[-1]
                   stack.pop()
                   stack.pop()
                   stack.append(a)
                if i=='-':
                   a= stack[-2]-stack[-1]
                   stack.pop()
                   stack.pop()
                   stack.append(a)
                if i=='*':
                   a= stack[-2]*stack[-1]
                   stack.pop()
                   stack.pop()
                   stack.append(a)
                if i=='/':
                   a= stack[-2]/stack[-1]
                   stack.pop()
                   stack.pop()
                   stack.append(int(a))

            else:
                stack.append(int(i))
        return stack[-1]