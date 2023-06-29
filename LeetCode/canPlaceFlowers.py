class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        def calcLocal(left, num, right):
            return ceil((num - left - right) / 2)

        cur = 0
        tot = 0
        seen = False
        for i in range(len(flowerbed)):
            if (flowerbed[i] == 0):
                cur += 1
            elif (not seen):
                seen = True
                tot += calcLocal(0, cur, 1)
                cur = 0
            else:
                tot += calcLocal(1, cur, 1)
                cur = 0

            if (tot >= n):
                return True

        if (not seen):
            tot += calcLocal(0, cur, 0)
        else:
            tot += calcLocal(1, cur, 0)

        print(tot)
        return tot >= n