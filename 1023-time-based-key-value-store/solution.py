from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        # self.store_t = defaultdict(lambda : defaultdict(list))
        self.storeT = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if timestamp < self.store[key].get('min',0):
        #     self.store[key]['min']=timestamp
            
        # if timestamp > self.store[key].get('max',0):
        #     self.store[key]['max']=timestamp
            
        # self.store_t[key][timestamp].append(value)
        self.store[key].append(value)
        self.storeT[key].append(timestamp)


    def get(self, key: str, timestamp: int) -> str:
        # d = self.store[key]
        # dt = self.store_t[key]
        # res =  dt.get(timestamp,[])
        # if res:
        #     return res[-1]
        # return
        # mn,mx = dt.get('min'), dt.get('max')
        # while mn<mx:
        #     md = (mn+mx)/2
        #     if dt.get(md,None) is not None:
        #         return dt[md][-1]
        #     # if 

        import bisect
        i = bisect.bisect_right(self.storeT[key],timestamp)
        if i==0:
            return ""
        return self.store[key][i-1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
