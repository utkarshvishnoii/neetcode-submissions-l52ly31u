class Solution:
    def isValid(self, s: str) -> bool:
        mapS = {
            '}':'{',
            ')':'(',
            ']':'['
        }
        stack = []
        if len(s)%2 != 0:
            return False
        for p in s:
            if stack and p in mapS:
                openB = stack.pop()
                if mapS[p] != openB:
                    return False
            else:
                stack.append(p)
        return len(stack) == 0

        


#     for p in range(len(s)/2):
#         stack
# stack = [ '(','[','{','}',']',')' ]
