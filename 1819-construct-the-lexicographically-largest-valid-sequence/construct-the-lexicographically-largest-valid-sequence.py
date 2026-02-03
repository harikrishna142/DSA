class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        # Size of the sequence is 2*n - 1
        size = 2 * n - 1
        result = [0] * size
        used = [False] * (n + 1) # Track numbers 1 to n

        def backtrack(index):
            # If we reached the end of the array, we found a valid sequence
            if index == size:
                return True
            
            # If the current position is already filled, move to the next one
            if result[index] != 0:
                return backtrack(index + 1)
            
            # Try numbers from n down to 1 to ensure lexicographically largest result
            for num in range(n, 0, -1):
                if used[num]:
                    continue
                
                # Handling the number 1 (appears only once)
                if num == 1:
                    result[index] = 1
                    used[1] = True
                    if backtrack(index + 1):
                        return True
                    
                    # Backtrack
                    result[index] = 0
                    used[1] = False
                
                # Handling numbers > 1 (appear twice at distance 'num')
                else:
                    if index + num < size and result[index + num] == 0:
                        result[index] = num
                        result[index + num] = num
                        used[num] = True
                        
                        if backtrack(index + 1):
                            return True
                        
                        # Backtrack
                        result[index] = 0
                        result[index + num] = 0
                        used[num] = False
            
            return False

        backtrack(0)
        return result