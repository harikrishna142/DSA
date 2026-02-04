class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        moves = 0
        l, r = 0, len(s) - 1
        
        while l < r:
            # Find the rightmost character index 'k' that matches s[l]
            k = r
            while k > l and s[k] != s[l]:
                k -= 1
            
            if k == l:
                # Case: s[l] is the unique odd-count character.
                # We swap it with its right neighbor to push it toward the center.
                s[l], s[l+1] = s[l+1], s[l]
                moves += 1
                # Note: We do NOT increment l or decrement r here because
                # we haven't successfully matched s[l] yet.
            else:
                # Case: Found a match at index k.
                # Bubble s[k] to the position r
                while k < r:
                    s[k], s[k+1] = s[k+1], s[k]
                    k += 1
                    moves += 1
                # Now that the boundary s[l]...s[r] is palindromic, shrink window
                l += 1
                r -= 1
                
        return moves