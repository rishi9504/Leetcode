class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        consecutive_rounds_won = 0
        current_winner = arr[0]
        
        for i in range(1, len(arr)):
            if arr[i] > current_winner:
                consecutive_rounds_won = 1
                current_winner = arr[i]
            else:
                consecutive_rounds_won += 1

            if consecutive_rounds_won == k:
                return current_winner

        return current_winner
            
