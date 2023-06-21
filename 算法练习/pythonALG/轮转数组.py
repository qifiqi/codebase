# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2023/6/1017:18
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : 轮转数组.py
__author__ = 'Small Fu'

'''
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

 

示例 1:

输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释: 
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]
 

提示：

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 '''
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n
        # [n-k-1,n-1]
        tmp = nums[n - k:].copy()
        for i in range(n - k - 1, -1, -1):
            nums[i + k] = nums[i]
        for i in range(0, k):
            nums[i] = tmp[i]
        return nums

if __name__ == '__main__':
    print(Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3))
