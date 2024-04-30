class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # l,r=0,len(nums)-1
        # result = set()
        # ts = set()
        # pos = set()
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i!=j:
        #             ts.add((i,j,nums[i],nums[j],nums[i]+nums[j]))
        #             pos.add((i,j,-nums[i]))
        # for a,b,a1,b1,c in ts:
        #     try:
        #         i = (a,b,-(c)) in pos
        #         if i:
        #             # print(a,b, a1, b1,c,i,'inside')
        #             if i not in [a,b]:
        #                 result.add(tuple(sorted([a1,b1,-c,])))
        #     except Exception as e:
        #         # print(e)
        #         pass
        # # print(result,ts)
        # return result

        res=set()
        neg,pos,zer=[],[],[]
        for num in nums:
            if num>0:
                pos.append(num)
            elif num<0:
                neg.append(num)
            else:
                zer.append(num)
        if len(zer)>=3:
            res.add((0,0,0))

        N,P = set(neg),set(pos)    

        if zer:
            for p in P:
                if -1*p in N:
                    res.add((-1*p,0,p))


        for i in range(len(neg)):
            for j in range(i+1,len(neg)) :
                s=-(neg[i]+neg[j])
                if s in P:
                    res.add(tuple(sorted([neg[i],neg[j],s])))

        for i in range(len(pos)):
            for j in range(i+1,len(pos)) :
                s=-(pos[i]+pos[j])
                if s in N:
                    res.add(tuple(sorted([pos[i],pos[j],s])))

                    

        return res     
        # res=set()
        # nums.sort()
        # for i,x in enumerate(nums):
        #     t = -x
        #     l,r = i,len(nums)-1
        #     while l<r:
        #         if nums[l]+nums[r]==t:
        #             res.add((x,nums[l],nums[r]))
        #         l+=1
        #         r-=1
        # return res





        
