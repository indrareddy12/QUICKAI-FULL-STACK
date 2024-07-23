from typing import List




class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        res = set()


        def fun(index: int, ds: List[int]):
            if index == len(nums):
                ds.sort()
                res.add(tuple(ds))
                return
            ds.append(nums[index])
            fun(index + 1, ds)
            ds.pop()
            fun(index + 1, ds)
        fun(0, [])
        for it in res:
            ans.append(list(it))
        return ans




if __name__ == "__main__":
    nums = [1, 2, 2]
    obj = Solution()
    ans = obj.subsetsWithDup(nums)
    print("The unique subsets are ")
    print("[ ", end="")
    for i in range(len(ans)):
        print("[ ", end="")
        for j in range(len(ans[i])):
            print(ans[i][j], end=" ")
        print("]", end="")