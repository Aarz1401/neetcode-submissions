class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles_sorted = piles
        max_pile = max(piles)
        min_pile = 1
        while(min_pile <= max_pile):
            mid = (min_pile + max_pile) // 2
            #now test if mid satisfies
            total_time = 0
            for pile in piles_sorted:
                total_time += -(-pile // mid)

            if total_time > h:
                min_pile = mid + 1
            else:
                max_pile = mid - 1
        
        return min_pile
            
            



    


            
            
                



            

                
        