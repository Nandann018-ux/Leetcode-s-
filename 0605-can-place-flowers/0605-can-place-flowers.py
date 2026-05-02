class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        lenn = len(flowerbed)
        count = 0 
        for i in range(lenn):
            if flowerbed[i]==0:
                check_left = (i==0) or (flowerbed[i-1]==0)
                check_right = (i == lenn - 1) or (flowerbed[i+1] == 0)

                if check_left and check_right:
                    flowerbed[i] = 1
                    count +=1

        return True if count>=n else False
        