class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphanumeric(c):
            return '0' <= c <= '9' or 'a' <= c.lower() <= 'z'
        
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not isAlphanumeric(s[left]):
                left += 1
            while left < right and not isAlphanumeric(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True