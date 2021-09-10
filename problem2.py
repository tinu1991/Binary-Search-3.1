#binary search time comp-O(logn)
#space- O(1)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations)==0:
              return 0
        n=len(citations)
        l=0
        h=len(citations)-1
        while l<=h:
            mid=(l+h)//2
            if citations[mid]==n-mid:
                return n-mid
            elif citations[mid]<n-mid:
                l=mid+1
            else:
                h=mid-1
        return n-l
        
