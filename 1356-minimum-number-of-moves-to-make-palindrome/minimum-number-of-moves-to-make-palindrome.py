class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        moves = 0
        left, right = 0, len(s) - 1

        while left < right:
            # If characters match, move inward
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # Find matching character for s[left] from the right side
                k = right
                while k > left and s[k] != s[left]:
                    k -= 1

                if k == left:  
                    # No matching char found; move this char towards the center
                    s[left], s[left + 1] = s[left + 1], s[left]
                    moves += 1
                else:
                    # Bring the matching char to the right position
                    while k < right:
                        s[k], s[k + 1] = s[k + 1], s[k]
                        k += 1
                        moves += 1
                    left += 1
                    right -= 1

        return moves