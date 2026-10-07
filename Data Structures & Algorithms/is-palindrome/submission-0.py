class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1
        
        while L < R:
            # Skip non-alphanumeric characters from left
            while L < R and not s[L].isalnum():
                L += 1
            # Skip non-alphanumeric characters from right
            while L < R and not s[R].isalnum():
                R -= 1
                
            # Compare lowercase values
            if s[L].lower() != s[R].lower():
                return False
                
            L += 1
            R -= 1
            
        return True