class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [0] * (2 * n - 1)
        used = [False] * (n + 1)
        length = len(res)

        def backtrack(idx):
            # If we've filled all positions, return True
            if idx == length:
                return True
            
            # If current position already filled, move to next
            if res[idx] != 0:
                return backtrack(idx + 1)

            # Try placing numbers from n down to 1 for lexicographically largest
            for num in range(n, 0, -1):
                if used[num]:
                    continue
                if num == 1:
                    res[idx] = 1
                    used[1] = True
                    if backtrack(idx + 1):
                        return True
                    res[idx] = 0
                    used[1] = False
                else:
                    j = idx + num
                    if j < length and res[j] == 0:
                        res[idx] = res[j] = num
                        used[num] = True
                        if backtrack(idx + 1):
                            return True
                        res[idx] = res[j] = 0
                        used[num] = False
            return False

        backtrack(0)
        return res

        