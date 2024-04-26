class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # res = [0]*len(temperatures)
        stack = []
        # highest = 0
        # for i,t in enumerate(temperatures):
        #     if t > highest:
        #         stack.append((i,t))
        #         highest = t
        # print(stack)
        # for  i,t in enumerate(temperatures):
        #     if t :
        #         res[i]=i-j
        res = [0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while stack and stack[-1][0]<t:
                _,previous_i = stack.pop()
                print(i,previous_i)
                res[previous_i] = -(previous_i -i)

            
            
            
            stack.append((t,i))
        return res    
