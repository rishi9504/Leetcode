class Solution:
    def maxArea(self, h: List[int]) -> int:
        """
        This function takes a list of integers representing the heights of a
        series of bars on a graph, and returns the maximum area of water that
        can be trapped between two of the bars.

        The approach is to use two pointers, l and r, that start at the
        beginning and end of the list, respectively. We then enter a loop where
        we calculate the area of water that can be trapped between the bars at
        l and r, and update our maximum area if this is the largest area we've
        seen so far.

        We then move the pointer that points to the shorter bar towards the
        other pointer, and repeat the loop until l and r meet.

        The reason we move the shorter bar is that we know that the area of
        water that can be trapped between it and the other bar will decrease if
        we move the taller bar. So if we move the shorter bar, we might be able
        to trap more water, but if we move the taller bar, we definitely won't
        be able to trap more water.

        This algorithm has a time complexity of O(n) and a space complexity of
        O(1), where n is the number of bars in the input list.
        """
        l,r = 0,len(h)-1
        m=0
        while l<r:
            # calculate the height of the current area
            mh = min([h[l],h[r]])
            # calculate the width of the current area
            mw = (r-l)*mh
            # if the current area is larger than the maximum area we've seen
            # so far, update m
            if mw>m:
                m=mw
            # move the pointer that points to the shorter bar towards the other
            # pointer
            if h[r]<h[l]:
                r-=1
            elif h[r]>h[l]:
                l+=1
            else:
                r-=1
                l+=1
        return m

                   
        
