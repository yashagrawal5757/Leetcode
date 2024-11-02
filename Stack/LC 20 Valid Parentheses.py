class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            ')':'(',
            ']':'[',
            '}':'{'
                }
        stack = []
        for char in s:
            if char in ['(','[','{']:
                stack.append(char)
            else:
                #only single closing bracket in s
                if len(stack)==0:
                    return False
                popped = stack.pop()
                if popped != map[char]:
                    return False
        #more opening brackets
        if len(stack)!= 0:
            return False
        return True
