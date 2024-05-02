class Solution:
    def maxArea(self, h: List[int]) -> int:
        l,r = 0,len(h)-1
        m=0
        while l<r:
            mh = min([h[l],h[r]])
            mw = (r-l)*mh
            if mw>m:
                m=mw
            # print(f'{m=},{mh=}, {mw=}')
            if h[r]<h[l]:
                r-=1
            elif h[r]>h[l]:
                l+=1
            else:
                r-=1
                l+=1
        return m

                   
        
