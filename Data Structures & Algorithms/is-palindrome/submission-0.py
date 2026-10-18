class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = "".join(char for char in s if char.isalnum())
        if cleaned_text.lower()[::-1] == cleaned_text.lower():
            return True
        return False

        