class Solution:
    def isValid(self, s: str) -> bool:
        mapS = {'}':'{',']':'[',')':'('}
        stack = []

        for b in s:
            if b in mapS and stack:
                openB = stack.pop()
                if openB != mapS[b]:
                    return False
            else:
                stack.append(b)
        return False if stack else True

# s = "([{}])"
#         b

# stack = ['(','[',]