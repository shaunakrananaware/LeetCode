class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        sumation = 0

        for idx in range(len(tickets)):
            if tickets[idx] < tickets[k]:
                sumation += tickets[idx]
                continue
            cal = 1 if idx>k else 0 
            sumation += tickets[k]-cal
        
        return sumation