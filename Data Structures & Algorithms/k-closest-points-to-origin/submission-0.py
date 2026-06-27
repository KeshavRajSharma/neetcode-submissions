import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances=list()
        for ps in points:
            x,y=ps
            dis=(x**2+y**2)**0.5
            distances.append((dis,(x,y)))

        heapq.heapify(distances)
        res=[]
        for i in range(k):
            first,second=heapq.heappop(distances)
            print(first,second)
            res.append(list(second))

        return res
        

        
        

        