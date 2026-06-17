class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l,r = 0,n-1
        l_max , r_max = height[l] , height[r]
        res = 0
        while r > l:
            if r_max > l_max:
                l += 1
                l_max = max(height[l],l_max)
                res += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max,height[r])
                res += r_max - height[r]
        return res


                

        