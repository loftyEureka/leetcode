class Solution:
    def longestPalindrome(self, s: str) -> str:
        # start small. Given a character c, see if its a palindrome by expanding outwards.
        
        # Time: O(n^2)
        # Space: O(n)
        
        answer = ""
        
        for center in range(len(s)):
            # if length of palindrome is odd. expand about center point
            i, j = center, center
            # expand outwards
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if j - i + 1 > len(answer):
                    answer = s[i : j + 1]
                i -= 1
                j += 1
            
            # if length of palindrome is even. expand about pivot
            i, j = center, center + 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if j - i + 1 > len(answer):
                    answer = s[i : j + 1]
                i -= 1
                j += 1
        
        return answer