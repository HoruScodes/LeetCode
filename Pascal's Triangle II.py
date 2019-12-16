class Solution:
    def getRow(self,k:int) -> list:
        arr = []
        if k < 0:
            return arr
        arr.append(1)
        for i in range(1,k):
            for j in range(len(arr)-1,0,-1):
                arr[j] = arr[j-1] + arr[j]
            arr.append(1)
        return arr
    
if __name__ == '__main__':
    s = Solution()
    print(s.getRow(5))




