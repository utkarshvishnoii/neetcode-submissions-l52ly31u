class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss =''
        for c in s:
            if c.isalnum():
                ss += c.lower()
        return (ss[::]) == (ss[::-1])