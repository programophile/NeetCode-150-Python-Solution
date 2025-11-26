class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        while right>=left:
            mid=(left+right)//2
            if self.hours(piles,mid)>h:
                left=mid+1
            else:
                right=mid-1
        return left
                
    def hours(self,list1,k):
        total_hours=0
        for i in list1:
            total_hours+= math.ceil(i/k)
        return total_hours        
