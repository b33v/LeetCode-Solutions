class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Initialize a dictionary to keep track of characters in t
        target_chars = {}
        for char in t:
            target_chars[char] = target_chars.get(char, 0) + 1

        # Initialize variables for window boundaries
        left = 0
        right = 0

        # Initialize variables for minimum window substring
        min_window = ""
        min_length = float('inf')

        # Initialize a counter to keep track of remaining characters to be found
        remaining = len(t)

        # Slide the window through the string
        while right < len(s):
            # If the current character is in t, decrement the remaining count
            if s[right] in target_chars:
                if target_chars[s[right]] > 0:
                    remaining -= 1
                target_chars[s[right]] -= 1

            # Move the right boundary of the window
            right += 1

            # While all characters in t are found, try to minimize the window
            while remaining == 0:
                # If the current window is smaller, update the minimum window substring
                if right - left < min_length:
                    min_window = s[left:right]
                    min_length = right - left

                # If the left character is in t, increment the remaining count
                if s[left] in target_chars:
                    target_chars[s[left]] += 1
                    if target_chars[s[left]] > 0:
                        remaining += 1

                # Move the left boundary of the window
                left += 1

        return min_window