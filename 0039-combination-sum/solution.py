class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
    
        def backtrack(start, target, combination):
            # Base case: when the target becomes 0, record the combination
            if target == 0:
                result.append(list(combination))
                return
            # Explore candidates starting from 'start'
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue
                # Choose the current number
                combination.append(candidates[i])
                # Recursive call with the same number (unlimited usage allowed)
                backtrack(i, target - candidates[i], combination)
                # Undo the choice (backtrack)
                combination.pop()
        
        backtrack(0, target, [])
        return result
