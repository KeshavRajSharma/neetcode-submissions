class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        Rmax = -1

        for k in range(len(arr)-1,-1,-1):
            newMax = max(Rmax,arr[k])
            arr[k] = Rmax
            Rmax = newMax
        return arr

           
        